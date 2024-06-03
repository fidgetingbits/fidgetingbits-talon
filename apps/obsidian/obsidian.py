from talon import Context, Module, actions

mod = Module()
apps = mod.apps
apps.obsidian = "app.name: Obsidian"

ctx = Context()
ctx.matches = r"""
app: obsidian
"""
ctx.tags = ["user.code_language_forced"]

macCtx = Context()
macCtx.matches = r"""
os: mac
app: obsidian
"""

linuxCtx = Context()
linuxCtx.matches = r"""
os: linux
app: obsidian
"""


@mod.action_class
class Actions:
    def obsidian_open_themes():
        """Open the themes pane in Obsidian"""


# TODO: Implement per-platform actions to override


@ctx.action_class("user")
class UserActions:
    def code_get_forced_language():
        return actions.user.code_get_forced_language_with_fallback("markdown")
