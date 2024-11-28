from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.packager_brew
"""


@ctx.action_class("user")
class UserActions:
    def packager():
        actions.insert("brew ")

    def package_search():
        actions.insert("brew search ")

    def package_install():
        actions.insert("brew install ")

    def package_update_all():
        actions.insert("brew update ")

    def package_update(name: str):
        actions.insert("brew upgrade ")
        if name and name != "":
            actions.insert(name)

    def package_remove():
        actions.insert("brew uninstall ")

    def package_help():
        actions.insert("brew --help\n")

    def package_list():
        actions.insert("brew list\n")

    # def package_list_contents():
    #     actions.insert("brew  ")

    # def package_dependencies():
    #     actions.insert("brew ")

    def package_search_by_name(name: str):
        actions.insert(f"brew search {name}")

    def package_install_by_name(name: str):
        actions.insert(f"brew install {name}")

    def package_remove_by_name(name: str):
        actions.insert(f"brew uninstall {name}")

    def package_update_by_name(name: str):
        actions.insert(f"brew upgrade {name}")
