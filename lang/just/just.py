from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: just
"""


@ctx.action_class("user")
class UserActions:
    # tag: comment_line

    def code_comment_line_prefix():
        actions.auto_insert("# ")
