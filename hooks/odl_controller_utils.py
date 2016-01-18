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
    }
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
