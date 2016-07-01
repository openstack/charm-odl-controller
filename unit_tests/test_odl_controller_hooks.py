# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mock import patch, call
from test_utils import CharmTestCase

with patch('charmhelpers.core.hookenv.config') as config:
    config.return_value = False
    import odl_controller_hooks as hooks


TO_PATCH = [
    'adduser',
    'apt_install',
    'check_call',
    'config',
    'install_remote',
    'log',
    'mkdir',
    'process_odl_cmds',
    'relation_set',
    'relation_ids',
    'restart_on_change',
    'service_start',
    'shutil',
    'write_mvn_config',
    'init_is_systemd',
    'service',
]


class ODLControllerHooksTests(CharmTestCase):

    def setUp(self):
        super(ODLControllerHooksTests, self).setUp(hooks, TO_PATCH)

        self.config.__getitem__.side_effect = self.test_config.get
        self.config.get.side_effect = self.test_config.get
        self.install_url = 'http://10.10.10.10/distribution-karaf.tgz'
        self.test_config.set('install-url', self.install_url)
        self.test_config.set('profile', 'default')
        self.init_is_systemd.return_value = False

    def _call_hook(self, hookname):
        hooks.hooks.execute([
            'hooks/{}'.format(hookname)])

    @patch('os.symlink')
    @patch('os.path.exists')
    @patch('os.listdir')
    def test_install_hook(self, mock_listdir, mock_path_exists, mock_symlink):
        mock_listdir.return_value = ['random-file', 'distribution-karaf.tgz']
        mock_path_exists.return_value = False
        self._call_hook('install')
        self.apt_install.assert_called_with([
            "default-jre-headless", "python-jinja2"],
            fatal=True
        )
        mock_symlink.assert_called_with('distribution-karaf.tgz',
                                        '/opt/opendaylight-karaf')
        self.adduser.assert_called_with("opendaylight", system_user=True)
        self.mkdir.assert_has_calls([
            call('/home/opendaylight', owner="opendaylight",
                 group="opendaylight", perms=0755),
            call('/var/log/opendaylight', owner="opendaylight",
                 group="opendaylight", perms=0755)
        ])
        self.check_call.assert_called_with([
            "chown", "-R", "opendaylight:opendaylight",
            "/opt/distribution-karaf.tgz"
        ])
        self.write_mvn_config.assert_called_with()
        self.service_start.assert_called_with('odl-controller')
        self.shutil.copy.assert_called_with('files/odl-controller.conf',
                                            '/etc/init')

    @patch('os.symlink')
    @patch('os.path.exists')
    @patch('os.listdir')
    def test_install_hook_systemd(self, mock_listdir,
                                  mock_path_exists, mock_symlink):
        self.init_is_systemd.return_value = True
        mock_listdir.return_value = ['random-file', 'distribution-karaf.tgz']
        mock_path_exists.return_value = False
        self._call_hook('install')
        self.apt_install.assert_called_with([
            "default-jre-headless", "python-jinja2"],
            fatal=True
        )
        mock_symlink.assert_called_with('distribution-karaf.tgz',
                                        '/opt/opendaylight-karaf')
        self.adduser.assert_called_with("opendaylight", system_user=True)
        self.mkdir.assert_has_calls([
            call('/home/opendaylight', owner="opendaylight",
                 group="opendaylight", perms=0755),
            call('/var/log/opendaylight', owner="opendaylight",
                 group="opendaylight", perms=0755)
        ])
        self.check_call.assert_called_with([
            "chown", "-R", "opendaylight:opendaylight",
            "/opt/distribution-karaf.tgz"
        ])
        self.write_mvn_config.assert_called_with()
        self.service_start.assert_called_with('odl-controller')
        self.shutil.copy.assert_called_with('files/odl-controller.service',
                                            '/lib/systemd/system')
        self.service.assert_called_with('enable', 'odl-controller')

    def test_ovsdb_manager_joined_hook(self):
        self._call_hook('ovsdb-manager-relation-joined')
        self.relation_set.assert_called_with(port=6640, protocol="tcp")

    def test_controller_api_relation_joined_hook(self):
        self._call_hook('controller-api-relation-joined')
        self.relation_set.assert_called_with(relation_id=None, port=8080,
                                             username="admin",
                                             password="admin")

    @patch.object(hooks, 'controller_api_joined')
    def test_config_changed_hook(self, mock_controller_api_joined):
        self.relation_ids.return_value = ['controller-api:2']
        self._call_hook('config-changed')
        self.write_mvn_config.assert_called_with()
        mock_controller_api_joined.assert_called_with('controller-api:2')
        self.process_odl_cmds.assert_called_with({
            'feature:install': [
                'odl-base-all', 'odl-aaa-authn', 'odl-restconf', 'odl-nsf-all',
                'odl-adsal-northbound', 'odl-mdsal-apidocs',
                'odl-ovsdb-openstack', 'odl-ovsdb-northbound',
                'odl-dlux-core'
            ],
            'port': 8080
        })
