from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: linux
tag: terminal
and tag: user.packager_yay
"""


@ctx.action_class("user")
class UserActions:
    # see yay.py for additional actions
    def packager():
        actions.auto_insert("yay ")

    def package_search():
        actions.auto_insert("yay -sS ")

    def package_install():
        actions.auto_insert("yay -S ")

    def package_update():
        actions.auto_insert("yay -Su ")

    def package_remove():
        actions.auto_insert("yay -R ")

    def package_help():
        actions.auto_insert("yay --help\n")

    def package_list():
        actions.auto_insert("yay -Qe\n")

    def package_list_contents():
        actions.auto_insert("yay -Ql ")

    def package_search_by_name(name: str):
        actions.insert(f"yay -sS {name}")

    def package_install_by_name(name: str):
        actions.insert(f"yay -S {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"yay -R {name}")

    def package_update_by_name(name: str):
        actions.insert(f"yay -U {name}")
