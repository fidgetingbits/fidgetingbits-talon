from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
os: linux
tag: terminal
and tag: user.packager_pacman
"""


@ctx.action_class("user")
class UserActions:
    # see yay.py per additional actions
    def packager():
        actions.auto_insert("pacman ")

    def package_search():
        actions.auto_insert("pacman -sS ")

    def package_install():
        actions.auto_insert("pacman -S ")

    def package_remove():
        actions.auto_insert("pacman -R ")

    def package_search_by_name(name: str):
        actions.insert(f"pacman -sS {name}")

    def package_install_by_name(name: str):
        actions.insert(f"pacman -S {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"pacman -R {name}")

    def package_update_by_name(name: str):
        actions.insert(f"pacman -U {name}")
