#!/usr/bin/env python

import os
import re
import shutil
from subprocess import check_call
import sys
import urlparse

from charmhelpers.core.hookenv import (
    Hooks,
    UnregisteredHookError,
    config,
    log
)

from charmhelpers.core.host import (
    adduser,
    mkdir,
    restart_on_change,
    service_restart,
    service_start
)

from charmhelpers.fetch import apt_install, install_remote

from odl_controller_utils import write_mvn_config

PACKAGES = [ "default-jre-headless", "python-jinja2" ]

hooks = Hooks()
config = config()

@hooks.hook("config-changed")
@restart_on_change({"/home/opendaylight/.m2/settings.xml": ["odl-controller"]})
def config_changed():
    write_mvn_config()

@hooks.hook()
def install():
    # install dependencies
    apt_install(PACKAGES, fatal=True)

    # install opendaylight
    install_url = config["install-url"]
    install_remote(install_url, dest="/opt")
    filename = re.sub("^.*/", "", urlparse.urlparse(install_url)[2])
    name = re.sub("\.tar\.gz$|\.tar$|\.gz$|\.zip$", "", filename)
    os.symlink(name, "/opt/opendaylight-karaf")
    shutil.copy("files/odl-controller.conf", "/etc/init")
    adduser("opendaylight", system_user=True)
    mkdir("/home/opendaylight", owner="opendaylight", group="opendaylight", perms=0755)
    check_call(["chown", "-R", "opendaylight:opendaylight", "/opt/" + name])
    mkdir("/var/log/opendaylight", owner="opendaylight", group="opendaylight", perms=0755)

    # install features
    write_mvn_config()
    service_start("odl-controller")
    check_call(["/opt/opendaylight-karaf/bin/client", "-r", "31",
                "feature:install", "odl-base-all", "odl-aaa-authn",
                "odl-restconf", "odl-nsf-all", "odl-adsal-northbound",
                "odl-mdsal-apidocs", "odl-ovsdb-openstack",
                "odl-ovsdb-northbound", "odl-dlux-core"])

def main():
    try:
        hooks.execute(sys.argv)
    except UnregisteredHookError as e:
        log("Unknown hook {} - skipping.".format(e))

@hooks.hook("upgrade-charm")
def upgrade_charm():
    pass

if __name__ == "__main__":
    main()
