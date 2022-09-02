# XXX - execute until line number/cursor

from talon import Context, Module, actions, app, settings, ui

mod = Module()
mod.tag("debugger", desc="Tag for enabling generic debugger commands")
# this list is updated by architecture specific python files
mod.setting(
    "debug_default_architecture",
    type=str,
    default="x64",
    desc="The default cpu architecture to use for debugging",
)
mod.setting(
    "debug_default_hexdump_count",
    type=int,
    default=256,
    desc="The default number of bytes to dump in hexdumps",
)

ctx = Context()
ctx.matches = r"""
tag: user.debugger
"""


def parse_debugger_title(window):
    if window != ui.active_window() or "ARCH" not in window.title:
        return
    index = window.title.find("ARCH:")
    arch = window.title[index + len("ARCH:") :].split(" ")[0]
    ctx.tags = [f"user.{arch}"]


def win_title_hook(window):
    #print(f"debugger.py win_title_hook: {window.title}")
    parse_debugger_title(window)


def win_focus_hook(window):
    #print("debugger.py win_focus_hook")
    parse_debugger_title(window)


ui.register("win_title", win_title_hook)
ui.register("win_focus", win_focus_hook)

# This is more generic than debugger, I should move somewhere else. assembly.py maybe
@mod.capture(rule="{self.registers}")
def register(m) -> str:
    "Returns a register"
    return m.registers


class Debugger:
    def __init__(self, mod):
        self.arch_index = 0
        self.architectures = ["x86", "x64", "arm32", "arm64"]
        for arch in self.architectures:
            mod.tag(arch, desc="Tag for enabling {arch} architecture")
        self.architecture = settings.get("user.debug_default_architecture")

    def cycle_architecture(self):
        """Switch between supported architectures"""
        self.arch_index += 1
        if self.arch_index == len(self.architectures):
            self.arch_index = 0
        self.architecture = self.architectures[self.arch_index]
        ctx.tags = [f"user.{self.architecture}"]
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

    def debugger_step_jump():
        """Step until the next jump in the debugger"""

    def debugger_step_call():
        """Step until the next call in the debugger"""

    def debugger_step_ret():
        """Step until the next ret in the debugger"""

    def debugger_step_syscall():
        """Step until the next syscall in the debugger"""

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

    def debugger_register_variable(register: str):
        """Print register as variable in the debugger"""

    def debugger_get_register(register: str):
        """Print specific register in the debugger"""

    def debugger_set_register(register: str):
        """Set specific register in the debugger"""

    def debugger_show_registers():
        """Print the current registers in the debugger"""

    def debugger_set_variable():
        """Set some variable"""

    def debugger_set_variable_clip():
        """Set some variable to clipboard value"""


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

    def debugger_access_register(register: str):
        """display the register using the debugger specific variable syntax"""

    ###
    # MEMORY ANALYSIS
    ###
    def debugger_hexdump_help():
        """hexdump help"""

    def debugger_hexdump(number: int, register: str):
        """The default hexdump functionality"""

    def debugger_hexdump_bytes(number: int, register: str):
        """Dump memory as bytes"""

    def debugger_hexdump_word(number: int, register: str):
        """Dump memory as half ward"""

    def debugger_hexdump_dword(number: int, register: str):
        """Dump memory as dword"""

    def debugger_hexdump_qword(number: int, register: str):
        """Dump memory as qword"""

    def debugger_dump_pointers(register: str):
        """Dump memory as a series of pointers"""

    def debugger_dump_ascii_string(number: int, register: str):
        """Dump memory as a strings"""

    def debugger_dump_unicode_string(number: int, register: str):
        """Display as specific address as an unicode string in the debugger"""

    def debugger_hexdump_clip(number: int):
        """Hex dump count bytes from the clipboard"""

    def debugger_hexdump_bytes_clip(number: int):
        """Dump memory as bytes"""

    def debugger_hexdump_word_clip(number: int):
        """Dump memory as half ward"""

    def debugger_hexdump_dword_clip(number: int):
        """Dump memory as dword"""

    def debugger_hexdump_qword_clip(number: int):
        """Dump memory as qword"""

    def debugger_dump_pointers_clip():
        """Dump memory as a series of pointers"""

    def debugger_dump_ascii_string_clip(number: int):
        """Dump the memory as a string"""

    def debugger_dump_unicode_string_clip(number: int):
        """Display as specific address as an unicode string in the debugger"""

    def debugger_hexdump_highlighted(count: int):
        """Hex dump highlighted address"""
