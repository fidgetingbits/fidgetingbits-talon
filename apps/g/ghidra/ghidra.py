import time

from talon import Context, Module, actions

mod = Module()
mod.apps.ghidra = """
app.name: Ghidra
app.name: ghidra-Ghidra
"""

ctx = Context()
ctx.matches = r"""
app: ghidra
"""


def delayed_clipboard_paste_enter():
    actions.sleep("100ms")
    actions.edit.paste()
    actions.sleep("100ms")
    actions.key("enter")


@ctx.action_class("user")
class UserActions:
    # Navigation
    def disassembler_function_start():
        actions.key("ctrl-up")

    def disassembler_jump_address():
        actions.key("g")

    def disassembler_jump_clipboard():
        actions.user.disassembler_jump_address()
        delayed_clipboard_paste_enter()

    def disassembler_next_function():
        actions.key("ctrl-down")

    def disassembler_previous_function():
        # FIXME: This fails if you're already on the start of a function
        actions.user.disassembler_function_start()
        actions.user.disassembler_function_start()

    # Documenting
    def disassembler_change_label():
        actions.key("l")

    def disassembler_change_label_clipboard():
        actions.user.disassembler_change_label()
        delayed_clipboard_paste_enter()

    def disassembler_change_function_name():
        # FIXME: This only works from assembly view, as decompilation will attempt to relabel the return
        actions.user.disassembler_function_start()
        actions.user.disassembler_change_label()
