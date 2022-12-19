from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
os: linux
tag: user.packager_apt
"""


@ctx.action_class("user")
class UserActions:
    def package_search_by_name(name: str):
        actions.insert(f"apt search {name}")

    def package_install_by_name(name: str):
        actions.insert(f"apt install {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"apt remove {name}")

    def package_update_by_name(name: str):
        actions.insert(f"apt update {name}")

    def packager():
        actions.auto_insert("apt ")
