from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.packager_yum
"""


@ctx.action_class("user")
class UserActions:
    # see yay.py per additional actions
    def packager():
        actions.auto_insert("yum ")

    def package_search():
        actions.auto_insert("yum search ")

    def package_install():
        actions.auto_insert("yum install ")

    def package_remove():
        actions.auto_insert("yum remove ")

    def package_search_by_name(name: str):
        actions.insert(f"yum search {name}")

    def package_install_by_name(name: str):
        actions.insert(f"yum install {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"yum remove {name}")

    def package_update_by_name(name: str):
        actions.insert(f"yum upgrade {name}")
