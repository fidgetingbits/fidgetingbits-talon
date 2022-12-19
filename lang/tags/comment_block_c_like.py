from talon import Context, Module, actions

c_like_ctx = Context()
mod = Module()

mod.tag("code_comment_block_c_like", desc="Denotes usage of C-style block comments")

c_like_ctx.matches = """
tag: user.code_comment_block_c_like
"""
c_like_ctx.tags = ["user.code_comment_block"]


@c_like_ctx.action_class("user")
class CActions:
    def code_comment_block():
        actions.insert("/*\n\n*/")
        actions.edit.up()

    def code_comment_block_prefix():
        actions.auto_insert("/*")

    def code_comment_block_suffix():
        actions.auto_insert("*/")
