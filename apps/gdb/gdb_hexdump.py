from talon import Context, Module, actions, app, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
not tag: user.gef
and not tag: user.pwndbg
"""

def handle_hexdump_count(fmt, number, register):
    count = settings.get("user.debug_default_hexdump_count")
    if number:
        count = number

    actions.auto_insert(f"x/{count}{fmt}x ")
    if len(register):
        actions.auto_insert(f"${register}\n")

@ctx.action_class("user")
class UserActions:
    # Code execution
    def debugger_hexdump_help():
        actions.auto_insert("help x\n")

    def debugger_hexdump(number:int, register:str):
        handle_hexdump_count("g", number, register)

    def debugger_hexdump_bytes(number:int, register:str):
        handle_hexdump_count("b", number, register)

    def debugger_hexdump_word(number:int, register:str):
        handle_hexdump_count("h", number, register)

    def debugger_hexdump_dword(number:int, register:str):
        handle_hexdump_count("d", number, register)

    def debugger_hexdump_qword(number:int, register:str):
        handle_hexdump_count("g", number, register)
