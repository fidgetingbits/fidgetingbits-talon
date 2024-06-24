import json
import pathlib
from talon import Context, Module, actions, settings

node_ctx = Context()
packager_ctx = Context()
mod = Module()
mod.tag("nodejs", desc="Tag for enabling nodejs commands in terminal")

mod.setting(
    "nodejs_packager_default",
    type=str,
    default="pnpm",
    desc="Default node package manager to use (npm or pnpm)",
)
mod.list("nodejs_scripts", desc="List of scripts defined in package.json")


packager_ctx.matches = r"""
tag: user.packager_nodejs
"""

node_ctx.matches = r"""
tag: user.nodejs
tag: user.packager_nodejs
"""


@node_ctx.dynamic_list("user.nodejs_scripts")
def user_node_scripts(m) -> dict[str, str]:
    """A dynamic list of nodejs scripts defined in package.json"""

    package = pathlib.Path(actions.user.get_cwd(), "package.json")
    if package.exists():
        with open(package) as f:
            data = json.load(f)
            scripts = data.get("scripts", {})
            return actions.user.create_spoken_forms_from_list(scripts.keys())


def _nodejs_packager_binary() -> str:
    return settings.get("user.nodejs_packager_default")


# We have an extra level of indirection because npm.talon itself can be used to call similar
# functions when the packager manager isn't set.
@mod.action_class
class UserActions:
    def nodejs_packager_binary() -> str:
        """Returns the default nodejs package manager"""
        return _nodejs_packager_binary()

    def nodejs_packager() -> str:
        """Inserts the default nodejs package manager"""
        actions.insert(_nodejs_packager_binary())

    def nodejs_package_search():
        """Search for a package"""
        actions.user.nodejs_package_search_by_name("")

    def nodejs_package_search_by_name(name: str):
        """Search for a package by name"""
        actions.insert(f"{actions.user.nodejs_packager()} search {name}")

    def nodejs_package_install():
        """Install a package"""
        actions.user.nodejs_package_install_by_name("")

    def nodejs_package_install_by_name(name: str):
        """Install a package by name"""
        actions.insert(f"{actions.user.nodejs_packager()} -g install {name}")

    def nodejs_package_local_install():
        """Install a package locally"""
        actions.user.nodejs_package_local_install_by_name("")

    def nodejs_package_local_install_by_name(name: str):
        """Install a package locally by name"""
        actions.insert(f"{actions.user.nodejs_packager()} install {name}")

    def nodejs_package_update_all():
        """Update all packages"""
        actions.insert(f"{actions.user.nodejs_packager()} -g update")

    def nodejs_package_update():
        """Update a package"""
        actions.user.nodejs_package_update_by_name("")

    def nodejs_package_update_by_name(name: str):
        """Update a package by name"""
        actions.insert(f"{actions.user.nodejs_packager()} -g update {name}")

    def nodejs_package_remove():
        """Remove a package"""
        actions.user.nodejs_package_remove_by_name("")

    def nodejs_package_remove_by_name(name: str):
        """Remove a package by name"""
        actions.insert(f"{actions.user.nodejs_packager()} -g remove {name}")

    def nodejs_package_help():
        """Show help for the package manager"""
        actions.insert(f"{actions.user.nodejs_packager()} --help\n")

    def nodejs_package_list():
        """List installed packages"""
        actions.insert(f"{actions.user.nodejs_packager()} -g list --installed\n")

    def nodejs_package_list_contents():
        """List the contents of a package"""
        actions.insert(f"{actions.user.nodejs_packager()} -g  list --installed\n")

    def nodejs_package_dependencies():
        """Show package dependencies"""
        actions.insert(f"{actions.user.nodejs_packager()} show ")


@packager_ctx.action_class("user")
class PackagerActions:
    def packager():
        actions.user.nodejs_packager()

    def package_search_by_name(name: str):
        actions.user.nodejs_package_search_by_name(name)

    def package_install_by_name(name: str):
        actions.user.nodejs_package_install_by_name(name)

    def package_remove_by_name(name: str):
        actions.user.nodejs_package_remove_by_name(name)

    def package_update_by_name(name: str):
        actions.user.nodejs_package_update_by_name(name)

    def package_update_all():
        actions.user.nodejs_package_update_all()

    def package_help():
        actions.user.nodejs_package_help()

    def package_list():
        actions.user.nodejs_package_list()

    def package_list_contents():
        actions.user.nodejs_package_list_contents()

    def package_dependencies():
        actions.user.nodejs_package_dependencies()
