from talon import Context, actions

ctx = Context()
ctx.matches = r"""
# A lot of this was taken from the fireeye voiceattackprofile, under the
# assumption either people might already be familiar with the commands
# https://fireeye.github.io/IDA_Pro_VoiceAttack_profile/Reference_sheet.html
# XXX - remove the mode
mode: user.ida
"""


@ctx.action_class("user")
class UserActions:
    def disassembler_open_file():
        actions.key("alt-f")
        actions.sleep("100ms")
        actions.key("down enter")

    # Formatting
    def disassembler_make_array():
        actions.key("shift-8")

    def disassembler_make_binary():
        actions.key("b")

    def disassembler_make_character():
        actions.key("r")

    def disassembler_make_code():
        actions.key("c")

    def disassembler_make_data():
        actions.key("d")

    def disassembler_make_decimal():
        actions.key("h")

    def disassembler_make_enum():
        actions.key("m")

    def disassembler_make_hex():
        actions.key("q")

    def disassembler_make_string():
        actions.key("a")

    def disassembler_make_structure_variable():
        actions.key("alt-q")

    def disassembler_make_unicode():
        actions.key("alt-a")

    # Navigation
    def disassembler_entry_point():
        actions.key("ctrl-e")

    def disassembler_jump_back():
        actions.key("escape")

    def disassembler_jump_address():
        actions.key("g")

    def disassembler_next_call():
        actions.key("ctrl-alt-shift-6")

    def disassembler_previous_call():
        actions.key("ctrl-alt-shift-7")

    def disassembler_function_start():
        actions.key("ctrl-alt-shift-1")

    def disassembler_function_end():
        actions.key("ctrl-alt-shift-2")

    def disassembler_false_branch():
        actions.key("ctrl-down")
        actions.sleep("100ms")
        actions.key("enter")

    def disassembler_true_branch():
        actions.key("ctrl-down")
        actions.sleep("100ms")
        actions.key("down enter")

    def disassembler_close_window():
        actions.key("alt-f3")

    def disassembler_cross_references_to():
        actions.key("ctrl-x")

    def disassembler_cross_references_from():
        actions.key("ctrl-j")

    # Windowing
    def disassembler_focus_disassembly():
        actions.key("alt-2")

    # Searching
    def disassembler_search_bytes():
        actions.key("alt-b")

    def disassembler_search_text():
        actions.key("alt-t")

    def disassembler_search_value():
        actions.key("alt-i")

    def disassembler_next_bytes():
        actions.key("ctrl-b")

    def disassembler_next_code():
        actions.key("alt-c")

    def disassembler_next_data():
        actions.key("ctrl-d")

    def disassembler_next_explored():
        actions.key("ctrl-a")

    def disassembler_next_text():
        actions.key("ctrl-t")

    def disassembler_next_unexplored():
        actions.key("ctrl-u")

    def disassembler_next_value():
        actions.key("ctrl-i")

    def disassembler_next_void():
        actions.key("ctrl-v")
