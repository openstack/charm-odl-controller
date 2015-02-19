from os import environ
import urlparse

from charmhelpers.core.templating import render

def mvn_ctx():
    ctx = {}
    ctx.update(mvn_proxy_ctx("http"))
    ctx.update(mvn_proxy_ctx("https"))
    return ctx

def mvn_proxy_ctx(protocol):
    ctx = {}
    key = protocol + "_proxy"
    if key in environ:
        url = urlparse.urlparse(environ[key])
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
