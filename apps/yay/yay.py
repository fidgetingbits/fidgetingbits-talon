from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.packager_yay
"""


@ctx.action_class("user")
class UserActions:
    # see yay.py for additional actions
    def packager():
        actions.insert("yay ")

    def package_search():
        actions.insert("yay -sS ")

    def package_install():
        actions.insert("yay -S ")

    def package_update_all():
        actions.insert("yay -Su ")

    def package_update(name: str):
        actions.insert("yay -S ")
        if name and name != "":
            actions.insert(name)

    def package_remove():
        actions.insert("yay -R ")

    def package_help():
        actions.insert("yay --help\n")

    def package_list():
        actions.insert("yay -Qe\n")

    def package_list_contents():
        actions.insert("yay -Ql ")

    def package_dependencies():
        actions.insert("yay -Si ")

    def package_search_by_name(name: str):
        actions.insert(f"yay -sS {name}")

    def package_install_by_name(name: str):
        actions.insert(f"yay -S {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"yay -R {name}")

    def package_update_by_name(name: str):
        actions.insert(f"yay -U {name}")
