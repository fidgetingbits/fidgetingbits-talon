from talon import Context, Module, actions, clip

mod = Module()
ctx = Context()

ctx.matches = r"""
app: ida
"""

# Allow us to use RPC
ctx.tags = ["user.command_client"]


class IDATalon:
    def copy_address(self, location):
        """Copies the address at location into the clipboard"""
        address = actions.user.run_rpc_command_get("copy_address", location)
        if not address:
            print("WARNING: Didn't get address back...")
            return
        print(address)
        clip.set_text(address)


ida = IDATalon()

# These ones are specific too an API exposed through the ida-talon plugin
@ctx.action_class("user")
class UserActions:
    def command_server_directory() -> str:
        return "ida-talon"

    def trigger_command_server_command_execution():
        actions.key("alt-shift-T")

@mod.action_class
class IDATalonActions:
    def ida_copy_address_cursor():
        """Copies the current address into the clipboard"""
        ida.copy_address("cursor")

    def ida_copy_address_function():
        """Copies the current address into the clipboard"""
        ida.copy_address("function")

    def ida_copy_address_base():
        """Copies the current address into the clipboard"""
        ida.copy_address("base")


