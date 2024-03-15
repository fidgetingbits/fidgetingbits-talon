from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = r"""
tag: user.packager_apt
"""


@ctx.action_class("user")
class UserActions:
    def packager():
        actions.insert("apt ")

    def package_search():
        actions.insert("apt search ")

    def package_install():
        actions.insert("apt install ")

    def package_update_all():
        actions.insert("apt update")

    def package_update(name: str):
        actions.insert("apt update ")
        if name and name != "":
            actions.insert(name)

    def package_remove():
        actions.insert("apt remove ")

    def package_help():
        actions.insert("apt --help\n")

    def package_list():
        actions.insert("apt list --installed\n")

    def package_list_contents():
        actions.insert("apt list --installed\n")

    def package_dependencies():
        actions.insert("apt show ")

    def package_search_by_name(name: str):
        actions.insert(f"apt search {name}")

    def package_install_by_name(name: str):
        actions.insert(f"apt install {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"apt remove {name}")

    def package_update_by_name(name: str):
        actions.insert(f"apt update {name}")
