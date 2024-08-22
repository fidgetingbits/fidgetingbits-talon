# Match when we're stuck in an application using a pager like less
from talon import Context, Module, actions, settings, ui

ctx = Context()
mod = Module()


mod.apps.pager = """
win.title: /TERM:less/
win.title: /TERM:.*|less/
win.title: /TERM:.*| less/

win.title: /TERM:more/
win.title: /TERM:.*|more/
win.title: /TERM:.*| more/

win.title: /TERM:git diff/
win.title: /TERM:git log/
win.title: /TERM:git show/

win.title: /TERM:nix log/
"""

ctx.matches = r"""
app: pager
"""


@ctx.action_class("user")
class UserActions:
    def scroll_start():
        actions.key("g")

    def scroll_end():
        actions.key("G")
