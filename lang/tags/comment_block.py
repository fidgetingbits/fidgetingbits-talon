from talon import Context, Module, actions

ctx = Context()
mod = Module()

mod.tag("code_comment_block", desc="Tag for enabling generic block comment commands")

ctx.matches = """
tag: user.code_comment_block
"""

@mod.action_class
class Actions:
    def code_comment_block():
        """Block comment"""

    def code_comment_block_prefix():
        """Block comment start syntax"""

    def code_comment_block_suffix():
        """Block comment end syntax"""
