from talon import Context, Module, actions

mod = Module()
mod.tag("gdb", desc="tag for running the gdb debugger")
mod.tag("gef", desc="Gef gdb plugin")
mod.tag("pwndbg", desc="pwndbg gdb plugin")
mod.tag("retsync", desc="retsync gdb/ida plugin")
mod.tag("libptmalloc", desc="libptmalloc gdb plugin")
mod.tag("libdlmalloc", desc="libdlmalloc gdb plugin")
mod.tag("libheap", desc="libheap gdb plugin")
mod.tag("muslheap", desc="muslheap gdb plugin")

ctx = Context()

ctx.matches = r"""
tag: user.gdb
"""


# see gdb_generic.py for actions that can also be overridden by other plugins
@ctx.action_class("user")
class UserActions:
    # Code execution

    def debugger_step_line():
        actions.auto_insert("step\n")

    def debugger_step_over_line():
        actions.auto_insert("next\n")

    def debugger_step_out():
        actions.auto_insert("finish\n")

    def debugger_continue():
        actions.auto_insert("c\n")

    def debugger_stop():
        actions.key("ctrl-c")

    def debugger_start():
        actions.auto_insert("run\n")

    def debugger_restart():
        actions.auto_insert("run\n")

    # XXX -
    def debugger_detach():
        actions.auto_insert("")

    # Registers
    def debugger_register_variable(register: str):
        actions.auto_insert(f"${register}")

    def debugger_set_register(register: str):
        actions.insert(f"set ${register}=")

    # Breakpoints
    def debugger_show_breakpoints():
        actions.auto_insert("info breakpoints\n")

    def debugger_add_sw_breakpoint():
        actions.auto_insert("break ")

    def debugger_show_registers():
        actions.auto_insert("info registers\n")

    def debugger_get_register(register: str):
        actions.auto_insert(f"r {register}")

    # XXX -
    def debugger_add_hw_breakpoint():
        actions.auto_insert("")

    def debugger_break_now():
        actions.key("ctrl-c")

    def debugger_break_here():
        actions.auto_insert("break\n")

    def debugger_clear_all_breakpoints():
        actions.auto_insert("d br\n")

    def debugger_clear_breakpoint():
        actions.insert("d br ")

    def debugger_enable_all_breakpoints():
        actions.insert("enable br\n")

    def debugger_enable_breakpoint():
        actions.insert("enable br ")

    def debugger_disable_all_breakpoints():
        actions.insert("disable br\n")

    def debugger_disable_breakpoint():
        actions.insert("disable br  ")

    def debugger_clear_breakpoint_id(number_small: int):
        actions.insert(f"d br {number_small}\n")

    def debugger_disable_breakpoint_id(number_small: int):
        actions.insert(f"disable br {number_small}\n")

    def debugger_enable_breakpoint_id(number_small: int):
        actions.insert(f"enable br {number_small}\n")

    # XXX - Now that I'm using pop again with control mouse, this becomes pretty
    # annoying, so need to rely on quick actions instead...
    #    def pop():
    #        """Optional way of pressing enter via pop sound"""
    #        actions.key("enter")

    def debugger_backtrace():
        actions.auto_insert("bt\n")

    def debugger_exit():
        actions.auto_insert("quit\n")

    def debugger_exit_force():
        actions.key("ctrl-c")
        actions.auto_insert("quit\ny\n")

    def debugger_disassemble_here(lines: int):
        actions.insert(f"x/{lines}i $pc\n")
        # Type inspection

    def debugger_disassemble(lines: int):
        actions.insert(f"x/{lines}i ")
        # Type inspection

    # XXX - Technically this should just be part of generic_debugger.talon
    # since it will follow the same pattern for all debuggers?
    def debugger_disassemble_clipboard(lines: int):
        actions.insert(f"x/{lines}i ")
        actions.edit.paste()
        actions.key("enter")

    def debugger_inspect_type():
        actions.insert("ptype ")

    def debugger_inspect_type_clip():
        actions.insert("ptype ")
        actions.edit.paste()
        actions.key("enter")

    def debugger_show_binary_sections():
        actions.user.paste("maintenance info sections")
        actions.key("enter")

    def debugger_show_memory_sections():
        actions.user.paste("info proc mappings")
        actions.key("enter")

    def debugger_access_register(register: str):
        actions.user.paste(f"${register}")

    def debugger_set_variable():
        actions.insert("set $=")
        actions.edit.left()

    # XXX - This might be able to use insert_cursor to let us get right on the
    # variable name
    def debugger_set_variable():
        actions.insert("set $=")
        actions.edit.paste()
