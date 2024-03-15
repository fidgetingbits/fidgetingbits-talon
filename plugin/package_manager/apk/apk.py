from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.packager_apk
"""


@ctx.action_class("user")
class UserActions:
    def package_search_by_name(name: str):
        actions.insert(f"apk search -v {name}")

    def package_install_by_name(name: str):
        actions.insert(f"apk install {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"apk remove {name}")

    def package_update_by_name(name: str):
        actions.insert(f"apk update {name}")

    def packager():
        actions.auto_insert("apk ")
