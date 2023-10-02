from talon import Context, Module, actions, clip

mod = Module()
ctx = Context()

ctx.matches = r"""
app: ida
"""

# Allow us to use RPC
ctx.tags = ["user.command_client"]


class IDATalon:
    def _copy_value(self, cmd, arg):
        result = actions.user.run_rpc_command_get(cmd, arg)
        if not result:
            print(f"WARNING: Didn't get result back from {cmd}({arg})...")
            return
        print(f"IDATalon DEBUG: {result}")
        clip.set_text(result)

    def copy_address(self, location):
        """Copies the address at location into the clipboard"""
        self._copy_value("copy_address", location)

    def copy_label(self, location):
        """Copies the label at location into the clipboard"""
        self._copy_value("copy_label", location)

    def copy_demangled_label(self, location):
        """Copies the label at location into the clipboard"""
        self._copy_value("copy_demangled_label", location)

    def copy_relative_offset(self, location):
        """Copies the label at location into the clipboard"""
        self._copy_value("copy_relative_offset", location)


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
        """Copies the current cursor address into the clipboard"""
        ida.copy_address("cursor")

    def ida_copy_address_function():
        """Copies the current address into the clipboard"""
        ida.copy_address("function")

    def ida_copy_address_base():
        """Copies the current base address into the clipboard"""
        ida.copy_address("base")

    def ida_copy_label_cursor():
        """Copies the current cursor label into the clipboard"""
        ida.copy_label("cursor")

    def ida_copy_label_function():
        """Copies the current function label into the clipboard"""
        ida.copy_label("function")

    def ida_copy_demangled_label_cursor():
        """Copies the current demangled cursor label into the clipboard"""
        ida.copy_demangled_label("cursor")

    def ida_copy_demangled_label_function():
        """Copies the current demangled function label into the clipboard"""
        ida.copy_demangled_label("function")

    def ida_copy_relative_offset_cursor():
        """Copies the relative offset of the cursor into the clipboard"""
        ida.copy_relative_offset("cursor")

    def ida_copy_relative_offset_function():
        """Copies the relative offset of the function into the clipboard"""
        ida.copy_relative_offset("function")

    def ida_modify_raw_datatype(datatype: str):
        """Convert data at cursor to the specified datatype"""
        actions.user.run_rpc_command("modify_raw_datatype", datatype)
