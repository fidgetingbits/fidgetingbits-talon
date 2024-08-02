from talon import Context, Module, actions

mod = Module()
mod.apps.zathura = """
os: linux
app.name: Zathura
app.name: zathura
"""

ctx = Context()
ctx.matches = r"""
app: zathura
"""


@ctx.action_class("edit")
class UserActions:
    # user.zoom tag, but edit.zoom_xxx actions
    def zoom_in():
        actions.key("shift-+")

    def zoom_out():
        actions.key("-")


@ctx.action_class("user")
class UserActions:
    # user.pages
    def page_current():
        pass

    def page_next():
        actions.key("J")

    def page_previous():
        actions.key("K")

    def page_jump(number: int):
        actions.insert(f"{number}G")

    def page_final():
        actions.key("G")
