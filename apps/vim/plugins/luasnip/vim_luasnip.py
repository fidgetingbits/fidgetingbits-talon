from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.vim_luasnip
"""

mod.tag("luasnip", desc="a tag to load luasnip")


@ctx.action_class("user")
class user_actions:
    def snippet_search(text: str):
        actions.user.vim_command_mode_exterm(':exe ":Telescope snippets snippets"\n')
        actions.insert(text)

    def snippet_insert(text: str):
        """Inserts a snippet"""
        actions.user.vim_insert_mode(text)
        actions.key("ctrl-k")

    def snippet_reload():
        """Reloads the snippets list"""
        actions.user.vim_command_mode_exterm(
            ':lua require("luasnip/loaders/from_lua").load({paths="/home/aa/.config/nvim/snippets/"})\n'
        )
