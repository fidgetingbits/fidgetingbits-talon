from talon import Context, Module, actions

mod = Module()
apps = mod.apps
apps.obsidian = "app.name: Obsidian"

ctx = Context()
ctx.matches = r"""
app: obsidian
"""

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
