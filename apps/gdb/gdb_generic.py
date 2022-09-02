# This file handles generic debug actions that may be overridden by gdb plugins
# such as pwndbg
from talon import Context, Module, actions, app, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
not tag: user.gef
and not tag: user.pwndbg
"""


def handle_hexdump_count(fmt, number, register, clip=False, copy=False):
    """
    :param fmt: The gdb analysis format string
    :param number: The number of given data type too dump
    :param register: The cpu register to dump from
    :param clip: Whether or not to paste source address from the clipboard
    :param copy: Whether or not to copy a highlighted string before pasting
    """
    count = settings.get("user.debug_default_hexdump_count")
    if number:
        count = number

    actions.auto_insert(f"x/{count}{fmt} ")
    if len(register):
        actions.auto_insert(f"${register}\n")
    elif clip:
        if copy:
            actions.edit.copy()
        actions.edit.paste()
        actions.key("enter")

# These are specifically functions that can be overridden by other plugins,
# like pwndbg or gef
@ctx.action_class("user")
class UserActions:

    ###
    # REGISTERS
    ###
    def debugger_show_registers():
        actions.auto_insert("info registers\n")

    def debugger_get_register(register: str):
        actions.auto_insert("i r ")
        if len(register):
            actions.auto_insert(f"{register}\n")

    ###
    # EXECUTION
    ###
    def debugger_step_into():
        actions.auto_insert("stepi\n")

    def debugger_step_over():
        actions.auto_insert("nexti\n")

    ###
    # MEMORY ANALYSIS
    ###
    def debugger_hexdump_help():
        actions.auto_insert("help x\n")

    def debugger_hexdump(number: int, register: str):
        handle_hexdump_count("gx", number, register)

    def debugger_hexdump_bytes(number: int, register: str):
        handle_hexdump_count("bx", number, register)

    def debugger_hexdump_word(number: int, register: str):
        handle_hexdump_count("hx", number, register)

    def debugger_hexdump_dword(number: int, register: str):
        handle_hexdump_count("dx", number, register)

    def debugger_hexdump_qword(number: int, register: str):
        handle_hexdump_count("gx", number, register)

    def debugger_dump_ascii_string(number: int, register: str):
        # XXX - this doesn't actually support counts
        handle_hexdump_count("s", number, register)

    def debugger_hexdump_clip(number: int):
        handle_hexdump_count("gx", number, "", clip=True)

    def debugger_hexdump_bytes_clip(number: int):
        handle_hexdump_count("bx", number, "", clip=True)

    def debugger_hexdump_word_clip(number: int):
        handle_hexdump_count("hx", number, "", clip=True)

    def debugger_hexdump_dword_clip(number: int):
        handle_hexdump_count("dx", number, "", clip=True)

    def debugger_hexdump_qword_clip(number: int):
        handle_hexdump_count("gx", number, "", clip=True)

    def debugger_dump_ascii_string_clip(number: int):
        # XXX - this doesn't actually support counts
        handle_hexdump_count("s", number, "", clip=True)
