from talon import Context, Module

mod = Module()
mod.tag("borg", desc="tag for enabling borg commands in your terminal")
borg = "borg"

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.borg
"""

mod.list("borg_commands", "List of borg commands")

ctx.lists["user.borg_commands"] = {
    "benchmark": "benchmark",
    "break lock": "break-lock",
    "check": "check",
    "compact": "compact",
    "config": "config",
    "create": "create",
    "debug": "debug",
    "delete": "delete",
    "diff": "diff",
    "export tar": "export-tar",
    "extract": "extract",
    "info": "info",
    "init": "init",
    "key": "key",
    "list": "list",
    "mount": "mount",
    "prune": "prune",
    "recreate": "recreate",
    "rename": "rename",
    "serve": "serve",
    "unmount": "umount",
    "upgrade": "upgrade",
    "with lock": "with-lock",
    "import tar": "import-tar",
}
mod.list("borg_servers", desc="List of borg servers")
mod.list("borg_private_servers", desc="List of private borg servers")
mod.list("borg_hosts", desc="List of backed up hosts")
mod.list("borg_private_hostss", desc="List of private backed up hosts")

ctx.lists["user.borg_servers"] = {}
ctx.lists["user.borg_private_servers"] = {}
ctx.lists["user.borg_hosts"] = {}
ctx.lists["user.borg_private_hosts"] = {}


@mod.action_class("user")
class Actions:
    def borg_command() -> str:
        """Default borg command to run"""
        return "borg"
