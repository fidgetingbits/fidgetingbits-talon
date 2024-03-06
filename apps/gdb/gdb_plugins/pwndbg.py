from talon import Context, Module, actions, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.pwndbg
"""


def handle_hexdump_count(cmd, number, register, clip=False, copy=False):
    count = settings.get("user.debug_default_hexdump_count")
    if number:
        count = number

    actions.auto_insert(f"{cmd} ")
    if register:
        actions.auto_insert(f"${register} {count}\n")
    elif clip:
        if copy:
            actions.edit.copy()
        actions.edit.paste()
        actions.auto_insert(f" {count}\n")
    else:
        actions.user.insert_between("", f" {count}")


@ctx.action_class("user")
class UserActions:
    ###
    # REGISTERS
    ###
    def debugger_show_registers():
        actions.auto_insert("regs\n")

    def debugger_get_register(register: str):
        actions.auto_insert("regs ")
        if register:
            actions.auto_insert(f"{register}\n")

    ###
    # EXECUTION
    ###
    def debugger_step_into():
        actions.auto_insert("nextproginstr\n")

    def debugger_step_over():
        actions.auto_insert("stepover\n")

    def debugger_step_jump():
        actions.auto_insert("nextjump\n")

    def debugger_step_call():
        actions.auto_insert("nextcall\n")

    def debugger_step_ret():
        actions.auto_insert("nextret\n")

    def debugger_step_syscall():
        actions.auto_insert("nextsc\n")

    ###
    # MEMORY ANALYSIS
    ###
    def debugger_hexdump_help():
        actions.auto_insert("hexdump -h\n")

    def debugger_hexdump(number: int, register: str):
        handle_hexdump_count("hexdump", number, register)

    def debugger_hexdump_bytes(number: int, register: str):
        handle_hexdump_count("hexdump", number, register)

    def debugger_hexdump_word(number: int, register: str):
        handle_hexdump_count("dw", number, register)

    def debugger_hexdump_dword(number: int, register: str):
        handle_hexdump_count("dd", number, register)

    def debugger_hexdump_qword(number: int, register: str):
        handle_hexdump_count("dq", number, register)

    def debugger_dump_pointers(register: str):
        actions.auto_insert("dps ")
        if register:
            actions.auto_insert(f"${register}\n")

    def debugger_dump_ascii_string(number: int, register: str):
        handle_hexdump_count("da", number, register)

    def debugger_hexdump_clip(number: int):
        handle_hexdump_count("hexdump", number, "", clip=True)

    def debugger_hexdump_bytes_clip(number: int):
        handle_hexdump_count("hexdump", number, "", clip=True)

    def debugger_hexdump_word_clip(number: int):
        handle_hexdump_count("dw", number, "", clip=True)

    def debugger_hexdump_dword_clip(number: int):
        handle_hexdump_count("dd", number, "", clip=True)

    def debugger_hexdump_qword_clip(number: int):
        handle_hexdump_count("dq", number, "", clip=True)

    def debugger_dump_pointers_clip():
        actions.auto_insert("dps ")
        actions.edit.paste()
        actions.key("enter")

    def debugger_dump_ascii_string_clip(number: int):
        handle_hexdump_count("da", number, "", clip=True)
