#!/usr/bin/env python

import os
import shutil
from subprocess import check_call
import sys

from charmhelpers.core.hookenv import (
    Hooks,
    UnregisteredHookError,
    config,
    log,
    relation_set,
    relation_ids,
)

from charmhelpers.core.host import (
    adduser,
    mkdir,
    restart_on_change,
    service_start
)

from charmhelpers.fetch import (
    configure_sources, apt_install, install_remote)

from odl_controller_utils import write_mvn_config, process_odl_cmds
from odl_controller_utils import PROFILES

PACKAGES = ["default-jre-headless", "python-jinja2"]
KARAF_PACKAGE = "opendaylight-karaf"

hooks = Hooks()
config = config()


@hooks.hook("config-changed")
@restart_on_change({"/home/opendaylight/.m2/settings.xml": ["odl-controller"]})
def config_changed():
    process_odl_cmds(PROFILES[config["profile"]])
    for r_id in relation_ids("controller-api"):
        controller_api_joined(r_id)
    write_mvn_config()


@hooks.hook("controller-api-relation-joined")
def controller_api_joined(r_id=None):
    relation_set(relation_id=r_id,
                 port=PROFILES[config["profile"]]["port"],
                 username="admin", password="admin")


@hooks.hook()
def install():
    if config.get("install-sources"):
        configure_sources(update=True, sources_var="install-sources")

    # install packages
    apt_install(PACKAGES, fatal=True)

    install_url = config["install-url"]
    if install_url:
        # install opendaylight from tarball

        # this extracts the archive too
        install_remote(install_url, dest="/opt")
        # The extracted dirname. Look at what's on disk instead of mangling, so
        # the distribution tar.gz's name doesn't matter.
        install_dir_name = [
            f for f in os.listdir("/opt")
            if f.startswith("distribution-karaf")][0]
        if not os.path.exists("/opt/opendaylight-karaf"):
            os.symlink(install_dir_name, "/opt/opendaylight-karaf")
    else:
        apt_install([KARAF_PACKAGE], fatal=True)
        install_dir_name = "opendaylight-karaf"

    shutil.copy("files/odl-controller.conf", "/etc/init")
    adduser("opendaylight", system_user=True)
    mkdir("/home/opendaylight", owner="opendaylight", group="opendaylight",
          perms=0755)
    check_call(
        ["chown", "-R", "opendaylight:opendaylight",
         os.path.join("/opt", install_dir_name)])
    mkdir("/var/log/opendaylight", owner="opendaylight", group="opendaylight",
          perms=0755)

    # install features
    write_mvn_config()
    service_start("odl-controller")


def main():
    try:
        hooks.execute(sys.argv)
    except UnregisteredHookError as e:
        log("Unknown hook {} - skipping.".format(e))


@hooks.hook("ovsdb-manager-relation-joined")
def ovsdb_manager_joined():
    relation_set(port=6640, protocol="tcp")


@hooks.hook("upgrade-charm")
def upgrade_charm():
    pass

if __name__ == "__main__":
    main()
