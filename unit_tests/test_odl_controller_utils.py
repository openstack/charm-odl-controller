from mock import patch, call
from test_utils import CharmTestCase

import odl_controller_utils as utils
import odl_outputs

TO_PATCH = [
    'subprocess',
    'render',
    'config',
    'retry_on_exception',
]


class ODLControllerUtilsTests(CharmTestCase):

    def setUp(self):
        super(ODLControllerUtilsTests, self).setUp(utils, TO_PATCH)
        self.config.side_effect = self.test_config.get
        self.test_config.set('http-proxy', 'http://proxy.int:3128')

    def test_mvn_proxy_ctx(self):
        expect = {
            'http_noproxy': [],
            'http_proxy': True,
            'http_proxy_host': 'proxy.int',
            'http_proxy_port': 3128
        }
        self.assertEqual(utils.mvn_proxy_ctx('http'), expect)

    def test_mvn_ctx(self):
        self.test_config.set('http-proxy', 'http://proxy.int:3128')
        expect = {
            'http_noproxy': [],
            'http_proxy': True,
            'http_proxy_host': 'proxy.int',
            'http_proxy_port': 3128
        }
        self.assertEqual(utils.mvn_ctx(), expect)

    def test_mvn_ctx_unset(self):
        self.test_config.set('http-proxy', '')
        self.assertEqual(utils.mvn_ctx(), {})

    def test_write_mvn_config(self):
        self.test_config.set('http-proxy', '')
        self.test_config.set('https-proxy', '')
        utils.write_mvn_config()
        self.render.assert_called_with(
            "settings.xml", "/home/opendaylight/.m2/settings.xml", {},
            "opendaylight", "opendaylight", 0400
        )

    def test_run_odl(self):
        utils.run_odl(["feature:list"])
        self.subprocess.check_output.assert_called_with(
            ["/opt/opendaylight-karaf/bin/client", "-r", '20', "-h",
             'localhost', "-a", '8101', "-u", "karaf", 'feature:list']
        )

    def test_installed_features(self):
        self.subprocess.check_output.return_value = \
            odl_outputs.ODL_023_FEATURE_LIST
        installed = utils.installed_features()
        for feature in utils.PROFILES["openvswitch-odl"]["feature:install"]:
            self.assertTrue(feature in installed)
        self.assertFalse('odl-l2switch-hosttracker' in installed)

    def test_filter_installed(self):
        self.subprocess.check_output.return_value = \
            odl_outputs.ODL_023_FEATURE_LIST
        self.assertEqual(
            utils.filter_installed(['odl-l2switch-hosttracker']),
            ['odl-l2switch-hosttracker']
        )
        self.assertEqual(utils.filter_installed(['odl-config-api']), [])

    @patch.object(utils, 'run_odl')
    @patch.object(utils, 'filter_installed')
    def test_process_odl_cmds(self, mock_filter_installed, mock_run_odl):
        test_profile = {
            "feature:install": ["odl-l2switch-all"],
            "log:set": {
                "TRACE": ["cosc-cvpn-ovs-rest"],
            },
            "port": 1181
        }
        mock_filter_installed.return_value = ["odl-l2switch-all"]
        utils.process_odl_cmds(test_profile)
        mock_run_odl.assert_has_calls([
            call(["feature:install", "odl-l2switch-all"]),
            call(['log:set', 'TRACE', 'cosc-cvpn-ovs-rest'])
        ])
