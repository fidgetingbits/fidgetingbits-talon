from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.scheme
"""


@ctx.action_class("user")
class UserActions:
    # tag-related actions listed first, indicated by comment. corresponds to
    # the tag(): user.code_imperative style declaration in the language .talon
    # file

    ##
    # code_comment_line
    ##
    def code_comment_line_prefix():
        actions.insert(";;")
