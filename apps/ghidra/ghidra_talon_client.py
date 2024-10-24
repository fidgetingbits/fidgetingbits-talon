import pathlib
from talon import Context, Module, actions, clip

mod = Module()
ctx = Context()

ctx.matches = r"""
app: ghidra
"""

# Allow us to use RPC
ctx.tags = ["user.command_client"]
# Ghidra doesn't support python extensions, meaning the first time our command server runs will be after we trigger the
# command. This means we have to pre create the communication directory here, as a hack, since the command client will
# otherwise fail if it doesn't exist.
folder = actions.user.get_full_communication_path()
pathlib.Path(folder).mkdir(parents=True, exist_ok=True)


class GhidraTalon:
    def _copy_value(self, cmd, arg):
        result = actions.user.run_rpc_command_get(cmd, arg)
        if not result:
            print(f"WARNING: Didn't get result back from {cmd}({arg})...")
            return
        print(f"GhidraTalon DEBUG: {result}")
        clip.set_text(result)


@ctx.action_class("user")
class UserActions:.
    def command_server_directory() -> str:
        return "ghidra-talon"

    def trigger_command_server_command_execution():
        actions.key("alt-shift-t")
