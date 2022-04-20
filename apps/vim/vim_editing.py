# File is for any sort of generic file editing that works in most modes. If you
# want to add something with more restricted modes than you should pick one of
# the different by them files.
from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app:vim
and not tag: user.vim_command_mode
"""

# Since this file includes anything that could by running in terminal mode or
# other modes, they should use the exterm version of the API in almost all
# cases.
@ctx.action_class("edit")
class EditActions:
    def find(text: str = None):
        actions.user.vim_normal_mode_exterm_key("/")

    def page_down():
        actions.user.vim_normal_mode_exterm_key("ctrl-f")

    def page_up():
        actions.user.vim_normal_mode_exterm_key("ctrl-b")
        # selecting (see generic_editor.talon)

    def left():
        actions.key("left")

    def right():
        actions.key("right")

    def up():
        actions.key("up")

    def down():
        actions.key("down")

    def zoom_out():
        actions.key("ctrl-shift--")

    def zoom_in():
        actions.key("ctrl-shift-+")
