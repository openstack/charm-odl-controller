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

import subprocess
from os import environ
import urlparse

from charmhelpers.core.templating import render
from charmhelpers.core.hookenv import config
from charmhelpers.core.decorators import retry_on_exception


PROFILES = {
    "cisco-vpp": {
        "feature:install": ["cosc-cvpn-ovs-rest",
                            "odl-netconf-connector-all"],
        "log:set": {
            "TRACE": ["cosc-cvpn-ovs-rest",
                      "odl-netconf-connector-all"],
        },
        "port": 8181
    },
    "openvswitch-odl": {
        "feature:install": ["odl-base-all", "odl-aaa-authn",
                            "odl-restconf", "odl-nsf-all",
                            "odl-adsal-northbound",
                            "odl-mdsal-apidocs",
                            "odl-ovsdb-openstack",
                            "odl-ovsdb-northbound",
                            "odl-dlux-core"],
        "port": 8080
    },
    "openvswitch-odl-lithium": {
        "feature:install": ["odl-ovsdb-openstack"],
        "port": 8080
    },
    "openvswitch-odl-beryllium": {
        "feature:install": ["odl-ovsdb-openstack",
                            "odl-restconf",
                            "odl-aaa-authn",
                            "odl-dlux-all"],
        "port": 8080
    },
    "openvswitch-odl-beryllium-l3": {
        "feature:install": ["odl-ovsdb-openstack"],
        "port": 8080
    },
    "openvswitch-odl-beryllium-sfc": {
        "feature:install": ["odl-ovsdb-openstack",
                            "odl-sfc-core",
                            "odl-sfc-sb-rest",
                            "odl-sfc-ui",
                            "odl-sfc-netconf",
                            "odl-sfc-ovs",
                            "odl-sfcofl2",
                            "odl-sfc-test-consumer"],
        "port": 8080
    },
    "openvswitch-odl-beryllium-vpn": {
        "feature:install": ["odl-ovsdb-openstack",
                            "odl-vpnservice-api",
                            "odl-vpnservice-impl",
                            "odl-vpnservice-impl-rest",
                            "odl-vpnservice-impl-ui",
                            "odl-vpnservice-core"],
        "port": 8080
    },
    "openvswitch-odl-boron": {
        "feature:install": ["odl-netvirt-openstack",
                            "odl-dlux-all"],
        "port": 8080
    },
    "openvswitch-odl-boron-sfc": {
        "feature:install": ["odl-ovsdb-sfc-rest",
                            "odl-dlux-all"],
        "port": 8080
    },
}
PROFILES["default"] = PROFILES["openvswitch-odl"]


def mvn_ctx():
    ctx = {}
    ctx.update(mvn_proxy_ctx("http"))
    ctx.update(mvn_proxy_ctx("https"))
    return ctx


def mvn_proxy_ctx(protocol):
    ctx = {}
    proxy = config("{}-proxy".format(protocol))
    key = protocol + "_proxy"
    if proxy:
        url = urlparse.urlparse(proxy)
    elif key in environ:
        url = urlparse.urlparse(environ[key])
    else:
        url = None

    if url:
        hostname = url.hostname
        if hostname:
            ctx[key] = True
            ctx[protocol + "_proxy_host"] = hostname
            port = url.port
            ctx[protocol + "_proxy_port"] = port if port else 80
            username = url.username
            if username:
                ctx[protocol + "_proxy_username"] = username
                ctx[protocol + "_proxy_password"] = url.password
            no_proxy = []
            if "no_proxy" in environ:
                np = environ["no_proxy"]
                if np:
                    no_proxy = np.split(",")
            ctx[protocol + "_noproxy"] = no_proxy
    return ctx


def write_mvn_config():
    ctx = mvn_ctx()
    render("settings.xml", "/home/opendaylight/.m2/settings.xml", ctx,
           "opendaylight", "opendaylight", 0400)


@retry_on_exception(5, base_delay=10, exc_type=subprocess.CalledProcessError)
def run_odl(cmds, host="localhost", port=8101, retries=20, user="karaf"):
    run_cmd = ["/opt/opendaylight-karaf/bin/client", "-r", str(retries),
               "-h", host, "-a", str(port), "-u", str(user)]
    run_cmd.extend(cmds)
    output = subprocess.check_output(run_cmd)
    return output


def installed_features():
    installed = []
    out = run_odl(["feature:list"])
    for line in out.split("\n"):
        columns = line.split("|")
        if len(columns) > 2:
            install_flag = columns[2].replace(" ", "")
            if install_flag == "x":
                installed.append(columns[0].replace(" ", ""))
    return installed


def filter_installed(features):
    installed = installed_features()
    whitelist = [feature for feature in features if feature not in installed]
    return whitelist


def process_odl_cmds(odl_cmds):
    features = filter_installed(odl_cmds.get("feature:install", []))
    if features:
        run_odl(["feature:install"] + features)
    logging = odl_cmds.get("log:set")
    if logging:
        for log_level in logging.keys():
            for target in logging[log_level]:
                run_odl(["log:set", log_level, target])
