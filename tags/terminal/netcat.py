from talon import Context, Module, actions

mod = Module()
# rust specific grammar

ctx = Context()
ctx.matches = r"""
tag: terminal
"""


@mod.action_class
class Actions:
    def bind_nc_listener(port: str):
        """Bind a netcat listener"""
        prefix = ""
        if int(port) > 65535:
            print("bind_nc_listener() - ERROR: invalid port: {port}")
        if int(port) < 1024:
            prefix = "sudo "
        cmd = f"{prefix}nc -v -l -p {port} "
        actions.insert(cmd)
