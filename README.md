# Overview

OpenDaylight (www.opendaylight.org) is a fully featured Software Defined Networking (SDN) solution for private clouds. It provides a Neutron plugin to
integrate with OpenStack.

This charm is designed to be used in conjunction with the rest of the OpenStack related charms in the charm store to virtualize the network that Nova Compute instances plug into.

This charm provides the controller component of an OpenDayLight installation.

Only OpenStack Icehouse or newer is supported.

# Usage

To deploy the OpenDayLight controller:

    juju deploy odl-controller

To integrate OpenDayLight into an OpenStack Cloud (subset of commands):

    juju deploy neutron-api-odl
    juju deploy openvswitch-odl

The neutron-gateway charm must also be deployed with 'ovs-odl' as the plugin configuration option:

    cat > config.yaml << EOF
    neutron-gateway:
        plugin: ovs-odl
    EOF
    juju deploy --config neutron-gateway

And then add relations between services to complete the deployment:

    juju add-relation neutron-api neutron-api-odl
    juju add-relation neutron-api-odl odl-controller

    juju add-relation openvswitch-odl nova-compute
    juju add-relation openvswitch-odl neutron-gateway
    juju add-relation openvswitch-odl odl-controller

# Contact Information

Report bugs on [Launchpad](http://bugs.launchpad.net/charms/+source/odl-controller/+filebug)
