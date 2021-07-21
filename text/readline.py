from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.readline
"""


@ctx.action_class("edit")
class EditActions:
    def undo():
        actions.key("ctrl-x ctrl-u")

    def up():
        actions.key("up")

    def down():
        actions.key("down")

    def left():
        actions.key("ctrl-b")

    def right():
        actions.key("ctrl-f")

    def word_left():
        actions.key("alt-b")

    def word_right():
        actions.key("alt-f")

    def line_start():
        actions.key("ctrl-a")

    def line_end():
        actions.key("ctrl-e")

    def delete_line():
        actions.key("ctrl-a")
        actions.key("ctrl-k")


@ctx.action_class("user")
class UserActions:
    def delete_line_beginning():
        actions.key("ctrl-u")

    def delete_line_remaining():
        actions.key("ctrl-k")

    def delete_word_right():
        actions.key("alt-d")

    def delete_word_left():
        actions.key("ctrl-w")
        # XXX - make this generic

    def line_find_forward(key: str):
        actions.key("ctrl-]")
        actions.key(key)

    def line_find_backward(key: str):
        actions.key("alt-ctrl-]")
        actions.key(key)
