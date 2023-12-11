from talon import Context, Module

mod = Module()
mod.list("ports", desc="Common ports")

ctx = Context()
ctx.lists["user.ports"] = {
    "web": "80",
    "T L S": "443",
    "remote desktop": "3389",
    "redis": "6379",
}


@mod.capture(rule="{user.ports}")
def ports(m) -> str:
    "One port"
    return m.ports
