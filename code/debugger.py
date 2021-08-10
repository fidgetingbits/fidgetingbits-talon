# XXX - execute until line number/cursor
# XXX - more memory printing
# XXX - need a way to disable the architecture modes, maybe be on context
# destruction

from talon import Context, Module, actions, app

mod = Module()
mod.tag("debugger", desc="Tag for enabling generic debugger commands")
# this list is updated by architecture specific python files
mod.list("registers", desc="A list of architecture registers")

ctx = Context()
ctx.matches = r"""
tag: user.debugger
"""

ctx.lists["user.registers"] = {}


# This is more generic than debugger, I should move somewhere else. assembly.py maybe
@mod.capture(rule="{self.registers}")
def register(m) -> str:
    "Returns a register"
    return m.registers


class Debugger:
    def __init__(self, mod):
        self.arch_index = 0
        self.architectures = ["x86", "x64"]
        for arch in self.architectures:
            mod.tag(arch, desc="Tag for enabling {arch} architecture")
        self.architecture = self.architectures[self.arch_index]

    def cycle_architecture(self):
        """Switch between supported architectures"""
        # actions.mode.disable(f"user.{self.architecture}")
        self.arch_index += 1
        if self.arch_index == len(self.architectures):
            self.arch_index = 0
        self.architecture = self.architectures[self.arch_index]
        # XXX - debugger ever has more tags, this will be a problem
        ctx.tags = [f"user.{self.architecture}"]
        # XXX - modes don't work for dynamic context loading it seems,
        # as a:
        # ```
        # ctx.matches = r"""
        # mode: user.x64
        # """
        # ```
        # won't activate...
        # actions.mode.disable(f"user.{self.architecture}")
        app.notify(subtitle=f"Debug architecture: {self.architecture}")

    def current_architecture(self):
        """Display the current architecture"""
        app.notify(subtitle=f"Debug architecture: {self.architecture}")


debugger = Debugger(mod)

# XXX - pass by windbg to dump
windows_x64_register_parameters = ["rcx", "rdx", "r8", "r9"]


@mod.action_class
class Actions:
    def debugger_step_into():
        """Step into an instruction in the debugger"""

    def debugger_step_over():
        """Step over an instruction in the debugger"""

    def debugger_step_line():
        """Step into a source line in the debugger"""

    def debugger_step_over_line():
        """Step over a source line in the debugger"""

    def debugger_step_out():
        """Step until function exit in the debugger"""

    def debugger_continue():
        """Continue execution in the debugger"""

    def debugger_restart():
        """Restart execution in the debugger"""

    def debugger_start():
        """Start debugging"""

    def debugger_stop():
        """Stop the debugger"""

    def debugger_exit():
        """Exit the debugger"""

    def debugger_exit_force():
        """Force exit the debugger"""

    def debugger_detach():
        """Detach the debugger"""

    def debugger_backtrace():
        """Print a back trace in the debugger"""

    def debugger_get_register():
        """Print specific register in the debugger"""

    def debugger_set_register():
        """Set specific register in the debugger"""

    def debugger_show_registers():
        """Print the current registers in the debugger"""

    def debugger_break_now():
        """Break into the debugger"""

    def debugger_break_here():
        """Set a break on the current line"""

    def debugger_show_breakpoints():
        """Print the current breakpoints in the debugger"""

    def debugger_add_sw_breakpoint():
        """Add one software breakpoint in the debugger"""

    def debugger_add_hw_breakpoint():
        """Add one hardware breakpoint in the debugger"""

    def debugger_clear_all_breakpoints():
        """Clear all breakpoints in the debugger"""

    def debugger_clear_breakpoint():
        """Clear one breakpoint in the debugger"""

    def debugger_clear_breakpoint_id(number_small: int):
        """Clear one breakpoint id in the debugger"""

    def debugger_disable_breakpoint_id(number_small: int):
        """Disable one breakpoint id in the debugger"""

    def debugger_disable_breakpoint():
        """Disable one breakpoint in the debugger"""

    def debugger_disable_all_breakpoints():
        """Disable all breakpoints in the debugger"""

    def debugger_enable_breakpoint():
        """Enable one breakpoint in the debugger"""

    def debugger_enable_breakpoint_id(number_small: int):
        """Enable one breakpoint id in the debugger"""

    def debugger_enable_all_breakpoints():
        """Enable all breakpoints in the debugger"""

    def debugger_disassemble():
        """Preps the disassemble command in the debugger"""

    def debugger_disassemble_here():
        """Disassembles instructions at the current instruction pointer"""

    def debugger_disassemble_clipboard():
        """Disassemble instructions at an address in the clipboard"""

    def debugger_goto_address():
        """Jump to a specific address in the debugger"""

    def debugger_goto_clipboard():
        """Jump to a specific address stored in the clipboard"""

    def debugger_goto_highlighted():
        """Jump to a specific highlighted address in the debugger"""

    def debugger_dump_ascii_string():
        """Display as specific address as an ascii string in the debugger"""

    def debugger_dump_unicode_string():
        """Display as specific address as an unicode string in the debugger"""

    def debugger_dump_pointers():
        """Display as specific address as a list of pointers in the debugger"""

    def debugger_inspect_type():
        """Inspect a specific data type in the debugger"""

    def debugger_inspect_type_clip():
        """Inspect a specific data type stored in the clipboard"""

    def debugger_clear_line():
        """Clear unwanted data from the command line"""

    def debugger_list_modules():
        """List the loaded modules in the debuggee memory space"""

    def debugger_show_binary_sections():
        """List the loaded modules and binary sections"""

    def debugger_show_memory_sections():
        """List the memory mapping of the target memory space"""

    def debugger_cycle_architecture():
        """Switch to the next architecture mode"""
        global debugger
        debugger.cycle_architecture()

    def debugger_current_architecture():
        """displayed the current architecture mode"""
        global debugger
        debugger.current_architecture()

    def debugger_access_register(register:str):
        """display the register using the debugger specific variable syntax"""

