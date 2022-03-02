from talon import Context, Module, actions, app, settings

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.pwndbg
"""

def handle_hexdump_count(number, register):
    count = settings.get("user.debug_default_hexdump_count")
    if number:
        count = number

    if len(register):
        actions.auto_insert(f"${register} {count}\n")
    elif number != 0 and not len(register): 
        actions.user.insert_cursor(f"[|] {count}")

@ctx.action_class("user")
class UserActions:
    # Code execution
    def debugger_hexdump_help():
        actions.auto_insert("hexdump -h\n")

    def debugger_hexdump(number:int, register:str):
        actions.auto_insert("hexdump ")
        handle_hexdump_count(number, register)

    def debugger_hexdump_bytes(number:int, register:str):
        actions.auto_insert("hexdump ")
        handle_hexdump_count(number, register)

    def debugger_hexdump_word(number:int, register:str):
        actions.auto_insert("dw ")
        handle_hexdump_count(number, register)

    def debugger_hexdump_dword(number:int, register:str):
        actions.auto_insert("dd ")
        handle_hexdump_count(number, register)

    def debugger_hexdump_qword(number:int, register:str):
        actions.auto_insert("dq ")
        handle_hexdump_count(number, register)

    def debugger_hexdump_register(register:str):
        actions.auto_insert(f"hexdump ${register}\n")

    def debugger_hexdump_register_count(register:str, count:int):
        actions.auto_insert(f"hexdump ${register} {count}\n")
