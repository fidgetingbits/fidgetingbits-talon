from talon import Module, Context, actions, ui, imgui, clip, settings

ctx = Context()
ctx.matches = r"""
mode: user.gdb
mode: user.auto_lang 
and code.language: gdb
"""

@ctx.action_class("user")
class UserActions:

    def code_comment_line_prefix():
        actions.auto_insert("# ")

