from talon import Context, actions

ctx = Context()
ctx.matches = r"""
code.language: toml
"""


@ctx.action_class("user")
class UserActions:
    ##
    # tag: comment_line
    ##
    def code_comment_line_prefix():
        actions.auto_insert("# ")

    ##
    # code_operators_assignment
    ##
    def code_operator_assignment():
        actions.insert(" = ")
