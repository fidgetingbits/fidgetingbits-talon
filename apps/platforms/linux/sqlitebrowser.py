from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app.name: sqlitebrowser
"""


@ctx.action_class("app")
class AppActions:
    # Execute SQL

    def tab_open():
        actions.key("ctrl-t")
