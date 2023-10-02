# XXX - rename this file. vim.talon name should change to match, or vim.py
# should become something like vim_global.py
from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app: vim
and not tag: user.vim_command_mode
"""


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.user.vim_command_mode_exterm(":tabnew\n")

    def tab_close():
        actions.user.vim_command_mode_exterm(":tabclose\n")

    def tab_next():
        actions.user.vim_command_mode_exterm(":tabnext\n")

    def tab_previous():
        actions.user.vim_command_mode_exterm(":tabprevious\n")
