# XXX - This file is deprecated. See text/readline.py
from talon import Context, actions

ctx = Context()
ctx.matches = r"""
# this is a set of commands that override common edit actions similar to edit.talon, but that specific
# to running commands inside of his shell, to a lot of the common word
# selection and such doesn't work the same.
#
# This particular set of commands is whom you're running bindkey -e mode
# and not bindkey -v mode.
# of something is missing anyone to add it you can see what the associated
# command is by typing `bindkey` in your shell and looking at the resulting
# list
os: linux
tag: user.shell_edit_emacs
"""
# XXX - change this tag name

@ctx.action_class("edit")
class EditActions:
    def word_left():
        actions.key("shift-left")

    def word_right():
        actions.key("shift-right")

    def line_start():
        actions.key("ctrl-a")

    def line_end():
        actions.key("ctrl-e")

    def delete():
        actions.key("backspace")

    def delete_line():
        actions.key("ctrl-u")


@ctx.action_class("user")
class UserActions:
    def delete_word_left():
        actions.key("ctrl-w")

    def delete_word_right():
        actions.key("ctrl-[ d")
