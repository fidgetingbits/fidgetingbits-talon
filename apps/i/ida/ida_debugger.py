from talon import Context, actions

ctx = Context()
ctx.matches = r"""
# A lot of this was taken from the fireeye voiceattackprofile, under the
# assumption either people might already be familiar with the commands
# https://fireeye.github.io/IDA_Pro_VoiceAttack_profile/Reference_sheet.html
mode: user.ida_debugger
"""
ctx.tags = ["ida", "debugger"]


@ctx.action_class("user")
class UserActions:
    def debugger_add_sw_breakpoint():
        actions.key("f2")
