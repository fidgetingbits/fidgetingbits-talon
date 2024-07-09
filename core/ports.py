from talon import Context, Module

mod = Module()
mod.list("ports", desc="Common ports")

ctx = Context()
# TODO: We could probably just auto populate this with some file
ctx.lists["user.ports"] = {
    "F T P": "21",
    "S S H": "22",
    "web": "80",
    "T L S": "443",
    "remote desktop": "3389",
    "redis": "6379",
    "sync thing": "8384",
}


@mod.capture(rule="{user.ports}")
def ports(m) -> str:
    "One port"
    return m.ports
