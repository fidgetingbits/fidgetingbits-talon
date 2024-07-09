import json
import pathlib
import socket

from talon import Context, Module, fs, actions
from talon_init import TALON_HOME

mod = Module()
mod.list("domains", desc="Commonly used domains")

ctx = Context()


class Domain:
    db = None

    def __init__(self):
        # assumes separate ~/.talon/user/private/ directory
        cwd = pathlib.Path(TALON_HOME, "user/private/settings/domains_private.json")
        self.domain_file = cwd.absolute()
        self.update_commands()
        fs.watch(self.domain_file, self.__on_fs_change)

    def __on_fs_change(self, name, flags):
        print("updating domain info commands")
        self.update_commands()

    def update_commands(self):
        with open(self.domain_file) as f:
            global ctx
            ctx.lists["user.domains"] = json.loads(f.read())


domain = Domain()


@mod.capture(rule="{user.domains}")
def domains(m) -> str:
    "One domains"
    return m.domains


@mod.action_class
class Actions:
    def domain_resolve_ip(domain: str) -> str:
        """Resolve the IP address of a domain"""
        actions.insert(repr(socket.gethostbyname(domain)).replace("'", ""))
