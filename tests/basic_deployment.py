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

import amulet
import os

from neutronclient.v2_0 import client as neutronclient

from charmhelpers.contrib.openstack.amulet.deployment import (
    OpenStackAmuletDeployment
)

from charmhelpers.contrib.openstack.amulet.utils import (
    OpenStackAmuletUtils,
    DEBUG,
    # ERROR
)

from novaclient import exceptions


class NovaOpenStackAmuletUtils(OpenStackAmuletUtils):
    """Nova based helper extending base helper for creation of flavors"""

    def create_flavor(self, nova, name, ram, vcpus, disk, flavorid="auto",
                      ephemeral=0, swap=0, rxtx_factor=1.0, is_public=True):
        """Create the specified flavor."""
        try:
            nova.flavors.find(name=name)
        except (exceptions.NotFound, exceptions.NoUniqueMatch):
            self.log.debug('Creating flavor ({})'.format(name))
            nova.flavors.create(name, ram, vcpus, disk, flavorid,
                                ephemeral, swap, rxtx_factor, is_public)


# Use DEBUG to turn on debug logging
u = NovaOpenStackAmuletUtils(DEBUG)

ODL_PROFILES = {
    'helium': {
        'location': 'AMULET_ODL_LOCATION',
        'profile': 'openvswitch-odl'
    },
    'beryllium': {
        'location': 'AMULET_ODL_BE_LOCATION',
        'profile': 'openvswitch-odl-beryllium'
    },
    'boron': {
        'location': 'AMULET_ODL_BO_LOCATION',
        'profile': 'openvswitch-odl-boron'
    },
}


class ODLControllerBasicDeployment(OpenStackAmuletDeployment):
    """Amulet tests on a basic OVS ODL deployment."""

    def __init__(self, series, openstack=None, source=None, git=False,
                 stable=True, odl_version='helium'):
        """Deploy the entire test environment."""
        super(ODLControllerBasicDeployment, self).__init__(series, openstack,
                                                           source, stable)
        self.odl_version = odl_version
        self._add_services()
        self._add_relations()
        self._configure_services()
        self._deploy()
        exclude_services = ['odl-controller', 'neutron-api-odl']
        self._auto_wait_for_status(exclude_services=exclude_services)
        self.d.sentry.wait()
        self._initialize_tests()

    def _add_services(self):
        """Add services

           Add the services that we're testing, where odl-controller is local,
           and the rest of the service are from lp branches that are
           compatible with the local charm (e.g. stable or next).
           """
        this_service = {
            'name': 'odl-controller',
            'constraints': {'mem': '8G'},
        }
        other_services = [
            {'name': 'percona-cluster', 'constraints': {'mem': '3072M'}},
            {'name': 'rabbitmq-server'},
            {'name': 'keystone'},
            {'name': 'nova-cloud-controller'},
            {'name': 'neutron-gateway'},
            {'name': 'neutron-api-odl'},
            {'name': 'openvswitch-odl'},
            {'name': 'neutron-api'},
            {'name': 'nova-compute'},
            {'name': 'glance'},
        ]

        super(ODLControllerBasicDeployment, self)._add_services(
            this_service, other_services)

    def _add_relations(self):
        """Add all of the relations for the services."""
        relations = {
            'keystone:shared-db': 'percona-cluster:shared-db',
            'neutron-gateway:amqp': 'rabbitmq-server:amqp',
            'nova-cloud-controller:quantum-network-service':
            'neutron-gateway:quantum-network-service',
            'nova-cloud-controller:shared-db': 'percona-cluster:shared-db',
            'nova-cloud-controller:identity-service': 'keystone:'
                                                      'identity-service',
            'nova-cloud-controller:amqp': 'rabbitmq-server:amqp',
            'neutron-api:shared-db': 'percona-cluster:shared-db',
            'neutron-api:amqp': 'rabbitmq-server:amqp',
            'neutron-api:neutron-api': 'nova-cloud-controller:neutron-api',
            'neutron-api:identity-service': 'keystone:identity-service',
            'neutron-api:neutron-plugin-api-subordinate':
            'neutron-api-odl:neutron-plugin-api-subordinate',
            'neutron-gateway:juju-info': 'openvswitch-odl:container',
            'openvswitch-odl:ovsdb-manager': 'odl-controller:ovsdb-manager',
            'neutron-api-odl:odl-controller': 'odl-controller:controller-api',
            'glance:identity-service': 'keystone:identity-service',
            'glance:shared-db': 'percona-cluster:shared-db',
            'glance:amqp': 'rabbitmq-server:amqp',
            'nova-compute:image-service': 'glance:image-service',
            'nova-compute:amqp': 'rabbitmq-server:amqp',
            'nova-cloud-controller:cloud-compute': 'nova-compute:'
                                                   'cloud-compute',
            'nova-cloud-controller:image-service': 'glance:image-service',
        }
        super(ODLControllerBasicDeployment, self)._add_relations(relations)

    def _configure_services(self):
        """Configure all of the services."""
        neutron_gateway_config = {
            'plugin': 'ovs-odl',
            'instance-mtu': '1400',
        }
        neutron_api_config = {
            'neutron-security-groups': 'True',
            'manage-neutron-plugin-legacy-mode': 'False',
        }
        neutron_api_odl_config = {
            'overlay-network-type': 'vxlan gre',
        }

        odl_controller_config = {}
        if os.environ.get(ODL_PROFILES[self.odl_version]['location']):
            odl_controller_config['install-url'] = \
                os.environ.get(ODL_PROFILES[self.odl_version]['location'])
        if os.environ.get('AMULET_HTTP_PROXY'):
            odl_controller_config['http-proxy'] = \
                os.environ['AMULET_HTTP_PROXY']
        if os.environ.get('AMULET_HTTP_PROXY'):
            odl_controller_config['https-proxy'] = \
                os.environ['AMULET_HTTP_PROXY']
        odl_controller_config['profile'] = \
            ODL_PROFILES[self.odl_version]['profile']

        keystone_config = {
            'admin-password': 'openstack',
            'admin-token': 'ubuntutesting'
        }
        nova_cc_config = {
            'network-manager': 'Neutron'
        }
        pxc_config = {
            'dataset-size': '25%',
            'max-connections': 1000,
            'root-password': 'ChangeMe123',
            'sst-password': 'ChangeMe123',
        }
        configs = {
            'neutron-gateway': neutron_gateway_config,
            'neutron-api': neutron_api_config,
            'neutron-api-odl': neutron_api_odl_config,
            'odl-controller': odl_controller_config,
            'keystone': keystone_config,
            'nova-cloud-controller': nova_cc_config,
            'percona-cluster': pxc_config,
        }
        super(ODLControllerBasicDeployment, self)._configure_services(configs)

    def _initialize_tests(self):
        """Perform final initialization before tests get run."""
        # Access the sentries for inspecting service units
        self.pxc_sentry = self.d.sentry['percona-cluster'][0]
        self.keystone_sentry = self.d.sentry['keystone'][0]
        self.rmq_sentry = self.d.sentry['rabbitmq-server'][0]
        self.nova_cc_sentry = self.d.sentry['nova-cloud-controller'][0]
        self.neutron_gateway_sentry = self.d.sentry['neutron-gateway'][0]
        self.neutron_api_sentry = self.d.sentry['neutron-api'][0]
        self.odl_controller_sentry = self.d.sentry['odl-controller'][0]
        self.neutron_api_odl_sentry = self.d.sentry['neutron-api-odl'][0]
        self.openvswitch_odl_sentry = self.d.sentry['openvswitch-odl'][0]

        # Authenticate admin with keystone
        self.keystone = u.authenticate_keystone_admin(self.keystone_sentry,
                                                      user='admin',
                                                      password='openstack',
                                                      tenant='admin')
        # Authenticate admin with neutron
        ep = self.keystone.service_catalog.url_for(service_type='identity',
                                                   interface='publicURL')
        self.neutron = neutronclient.Client(auth_url=ep,
                                            username='admin',
                                            password='openstack',
                                            tenant_name='admin',
                                            region_name='RegionOne')
        # Authenticate admin with glance endpoint
        self.glance = u.authenticate_glance_admin(self.keystone)
        # Create a demo tenant/role/user
        self.demo_tenant = 'demoTenant'
        self.demo_role = 'demoRole'
        self.demo_user = 'demoUser'
        if not u.tenant_exists(self.keystone, self.demo_tenant):
            tenant = self.keystone.tenants.create(tenant_name=self.demo_tenant,
                                                  description='demo tenant',
                                                  enabled=True)
            self.keystone.roles.create(name=self.demo_role)
            self.keystone.users.create(name=self.demo_user,
                                       password='password',
                                       tenant_id=tenant.id,
                                       email='demo@demo.com')

        # Authenticate demo user with keystone
        self.keystone_demo = \
            u.authenticate_keystone_user(self.keystone, user=self.demo_user,
                                         password='password',
                                         tenant=self.demo_tenant)

        # Authenticate demo user with nova-api
        self.nova_demo = u.authenticate_nova_user(self.keystone,
                                                  user=self.demo_user,
                                                  password='password',
                                                  tenant=self.demo_tenant)

        # Authenticate admin with nova endpoint
        self.nova = u.authenticate_nova_user(self.keystone,
                                             user='admin',
                                             password='openstack',
                                             tenant='admin')

    def test_100_services(self):
        """Verify the expected services are running on the corresponding
           service units."""
        neutron_services = ['neutron-dhcp-agent',
                            'neutron-lbaas-agent',
                            'neutron-metadata-agent',
                            'neutron-metering-agent',
                            'neutron-l3-agent']

        odl_c_services = ['odl-controller']

        commands = {
            self.neutron_gateway_sentry: neutron_services,
            self.odl_controller_sentry: odl_c_services,
        }

        if self._get_openstack_release() >= self.xenial_newton:
            commands[self.neutron_gateway_sentry].remove(
                'neutron-lbaas-agent'
            )
            commands[self.neutron_gateway_sentry].append(
                'neutron-lbaasv2-agent'
            )

        ret = u.validate_services_by_name(commands)
        if ret:
            amulet.raise_status(amulet.FAIL, msg=ret)

    def test_102_service_catalog(self):
        """Verify that the service catalog endpoint data is valid."""
        u.log.debug('Checking keystone service catalog...')
        endpoint_check = {
            'adminURL': u.valid_url,
            'id': u.not_null,
            'region': 'RegionOne',
            'publicURL': u.valid_url,
            'internalURL': u.valid_url
        }
        expected = {
            'network': [endpoint_check],
            'compute': [endpoint_check],
            'identity': [endpoint_check]
        }
        actual = self.keystone.service_catalog.get_endpoints()

        ret = u.validate_svc_catalog_endpoint_data(expected, actual)
        if ret:
            amulet.raise_status(amulet.FAIL, msg=ret)

    def test_104_network_endpoint(self):
        """Verify the neutron network endpoint data."""
        u.log.debug('Checking neutron network api endpoint data...')
        endpoints = self.keystone.endpoints.list()
        admin_port = internal_port = public_port = '9696'
        expected = {
            'id': u.not_null,
            'region': 'RegionOne',
            'adminurl': u.valid_url,
            'internalurl': u.valid_url,
            'publicurl': u.valid_url,
            'service_id': u.not_null
        }
        ret = u.validate_endpoint_data(endpoints, admin_port, internal_port,
                                       public_port, expected)

        if ret:
            amulet.raise_status(amulet.FAIL,
                                msg='glance endpoint: {}'.format(ret))

    def test_110_users(self):
        """Verify expected users."""
        u.log.debug('Checking keystone users...')
        expected = [
            {'name': 'admin',
             'enabled': True,
             'tenantId': u.not_null,
             'id': u.not_null,
             'email': 'juju@localhost'},
            {'name': 'neutron',
             'enabled': True,
             'tenantId': u.not_null,
             'id': u.not_null,
             'email': 'juju@localhost'}
        ]

        if self._get_openstack_release() >= self.xenial_ocata:
            # Ocata or later
            expected.append({
                'name': 'placement_nova',
                'enabled': True,
                'tenantId': u.not_null,
                'id': u.not_null,
                'email': 'juju@localhost'
            })
        elif self._get_openstack_release() >= self.trusty_kilo:
            # Kilo or later
            expected.append({
                'name': 'nova',
                'enabled': True,
                'tenantId': u.not_null,
                'id': u.not_null,
                'email': 'juju@localhost'
            })
        else:
            # Juno and earlier
            expected.append({
                'name': 's3_ec2_nova',
                'enabled': True,
                'tenantId': u.not_null,
                'id': u.not_null,
                'email': 'juju@localhost'
            })

        actual = self.keystone.users.list()
        ret = u.validate_user_data(expected, actual)
        if ret:
            amulet.raise_status(amulet.FAIL, msg=ret)

    def test_200_odl_controller_controller_api_relation(self):
        """Verify the odl-controller to neutron-api-odl relation data"""
        u.log.debug('Checking odl-controller to neutron-api-odl relation data')
        unit = self.odl_controller_sentry
        relation = ['controller-api', 'neutron-api-odl:odl-controller']
        expected = {
            'private-address': u.valid_ip,
            'username': 'admin',
            'password': 'admin',
            'port': '8080',
        }

        ret = u.validate_relation_data(unit, relation, expected)
        if ret:
            message = u.relation_error('odl-controller controller-api', ret)
            amulet.raise_status(amulet.FAIL, msg=message)

    def test_201_neutron_api_odl_odl_controller_relation(self):
        """Verify the odl-controller to neutron-api-odl relation data"""
        u.log.debug('Checking odl-controller to neutron-api-odl relation data')
        unit = self.neutron_api_odl_sentry
        relation = ['odl-controller', 'odl-controller:controller-api']
        expected = {
            'private-address': u.valid_ip,
        }

        ret = u.validate_relation_data(unit, relation, expected)
        if ret:
            message = u.relation_error('neutron-api-odl odl-controller', ret)
            amulet.raise_status(amulet.FAIL, msg=message)

    def test_202_odl_controller_ovsdb_manager_relation(self):
        """Verify the odl-controller to openvswitch-odl relation data"""
        u.log.debug('Checking odl-controller to openvswitch-odl relation data')
        unit = self.odl_controller_sentry
        relation = ['ovsdb-manager', 'openvswitch-odl:ovsdb-manager']
        expected = {
            'private-address': u.valid_ip,
            'protocol': 'tcp',
            'port': '6640',
        }

        ret = u.validate_relation_data(unit, relation, expected)
        if ret:
            message = u.relation_error('odl-controller openvswitch-odl', ret)
            amulet.raise_status(amulet.FAIL, msg=message)

    def test_203_openvswitch_odl_ovsdb_manager_relation(self):
        """Verify the openvswitch-odl to odl-controller relation data"""
        u.log.debug('Checking openvswitch-odl to odl-controller relation data')
        unit = self.openvswitch_odl_sentry
        relation = ['ovsdb-manager', 'odl-controller:ovsdb-manager']
        expected = {
            'private-address': u.valid_ip,
        }

        ret = u.validate_relation_data(unit, relation, expected)
        if ret:
            message = u.relation_error('openvswitch-odl to odl-controller',
                                       ret)
            amulet.raise_status(amulet.FAIL, msg=message)

    def test_400_create_network(self):
        """Create a network, verify that it exists, and then delete it."""
        u.log.debug('Creating neutron network...')
        self.neutron.format = 'json'
        net_name = 'ext_net'

        # Verify that the network doesn't exist
        networks = self.neutron.list_networks(name=net_name)
        net_count = len(networks['networks'])
        if net_count != 0:
            msg = "Expected zero networks, found {}".format(net_count)
            amulet.raise_status(amulet.FAIL, msg=msg)

        # Create a network and verify that it exists
        network = {'name': net_name}
        self.neutron.create_network({'network': network})

        networks = self.neutron.list_networks(name=net_name)
        u.log.debug('Networks: {}'.format(networks))
        net_len = len(networks['networks'])
        if net_len != 1:
            msg = "Expected 1 network, found {}".format(net_len)
            amulet.raise_status(amulet.FAIL, msg=msg)

        u.log.debug('Confirming new neutron network...')
        network = networks['networks'][0]
        if network['name'] != net_name:
            amulet.raise_status(amulet.FAIL, msg="network ext_net not found")

        # Cleanup
        u.log.debug('Deleting neutron network...')
        self.neutron.delete_network(network['id'])

    def test_400_gateway_bridges(self):
        """Ensure that all bridges are present and configured with the
           ODL controller as their NorthBound controller URL."""
        odl_ip = self.odl_controller_sentry.relation(
            'ovsdb-manager',
            'openvswitch-odl:ovsdb-manager'
        )['private-address']
        # NOTE: 6633 is legacy 6653 is IANA assigned
        if self.odl_version == 'helium':
            controller_url = "tcp:{}:6633".format(odl_ip)
            check_bridges = ['br-int', 'br-ex', 'br-data']
        else:
            controller_url = "tcp:{}:6653".format(odl_ip)
            # NOTE: later ODL releases only manage br-int
            check_bridges = ['br-int']
        cmd = 'ovs-vsctl list-br'
        output, _ = self.neutron_gateway_sentry.run(cmd)
        bridges = output.split()
        u.log.debug('Checking bridge configuration...')
        for bridge in check_bridges:
            if bridge not in bridges:
                amulet.raise_status(
                    amulet.FAIL,
                    msg="Missing bridge {} from gateway unit".format(bridge)
                )
            u.log.debug('Validating ...')
            cmd = 'ovs-vsctl get-controller {}'.format(bridge)
            br_controllers, _ = self.neutron_gateway_sentry.run(cmd)
            br_controllers = list(set(br_controllers.strip().split('\n')))
            if len(br_controllers) != 1 or br_controllers[0] != controller_url:
                status, _ = self.neutron_gateway_sentry.run('ovs-vsctl show')
                amulet.raise_status(
                    amulet.FAIL,
                    msg="Controller configuration on bridge"
                        " {} incorrect: !{}! not in !{}!\n"
                        "{}".format(bridge,
                                    br_controllers,
                                    controller_url,
                                    status)
                )

    def test_400_image_instance_create(self):
        """Create an image/instance, verify they exist, and delete them."""

        u.log.debug('Checking nova instance creation...')

        image = u.create_cirros_image(self.glance, "cirros-image")
        if not image:
            amulet.raise_status(amulet.FAIL, msg="Image create failed")

        # NOTE(jamespage): ensure require flavor exists, required for >= newton
        u.create_flavor(nova=self.nova,
                        name='m1.tiny', ram=512, vcpus=1, disk=1)

        instance = u.create_instance(self.nova_demo, "cirros-image", "cirros",
                                     "m1.tiny")
        if not instance:
            amulet.raise_status(amulet.FAIL, msg="Instance create failed")

        found = False
        for instance in self.nova_demo.servers.list():
            if instance.name == 'cirros':
                found = True
                if instance.status != 'ACTIVE':
                    msg = "cirros instance is not active"
                    amulet.raise_status(amulet.FAIL, msg=msg)

        if not found:
            message = "nova cirros instance does not exist"
            amulet.raise_status(amulet.FAIL, msg=message)

        u.delete_resource(self.glance.images, image.id,
                          msg="glance image")

        u.delete_resource(self.nova_demo.servers, instance.id,
                          msg="nova instance")
