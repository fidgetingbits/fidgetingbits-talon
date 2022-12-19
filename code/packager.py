from talon import Context, Module, actions, imgui, ui

mod = Module()
ctx = Context()
ctx.matches = r"""
os: linux
tag: terminal
and tag: user.package_manager
"""

mod.mode("packager_picker_open")

mod.tag("package_manager", desc="linux package manager")
packager_list = [
    {"tag": "packager_yay", "desc": "Arch Linux YAY packager"},
    {"tag": "packager_pacman", "desc": "Arch Linux YAY packager"},
    {"tag": "packager_pamac", "desc": "Manjaro Linux packager"},
    {"tag": "packager_apt", "desc": "Debian/Ubuntu Linux packager"},
    {"tag": "packager_snap", "desc": "Snap packager"},
    {"tag": "packager_zypper", "desc": "SuSE packager"},
    {"tag": "packager_dnf", "desc": "Fedora DNF packager"},
    {"tag": "packager_yum", "desc": "Fedora YUM packager"},
    {"tag": "packager_npm", "desc": "Node package manager"},
]

for packager in packager_list:
    mod.tag(packager["tag"], packager["desc"])

main_screen = ui.main_screen()


def close_packager_picker():
    gui.hide()
    actions.mode.disable("user.packager_picker_open")


@imgui.open(y=0, x=main_screen.width / 2.6)
def gui(gui: imgui.GUI):
    gui.line()
    gui.text("Active Packager:")
    gui.text("replay <number>")
    gui.text("Select New Active Packager:")
    gui.text("replay save <number>")
    gui.text("replay yank <number>")
    gui.line()
    index = 1

    if gui.button("Hide"):
        close_packager_picker()


@mod.action_class
class Actions:
    def packager():
        """Run the default packager"""

    def package_search():
        """Search the package database"""

    def package_search_by_name(name: str):
        """Search for the specified package in the package database"""

    def package_install():
        """Install from the package database"""

    def package_install_by_name(name: str):
        """Install specified package from the package database"""

    def package_remove():
        """Uninstall the package"""

    def package_remove_by_name(name: str):
        """Uninstall the package by name"""

    def package_update(name: str):
        """Update from the package database"""

    def package_update_by_name(name: str):
        """Update specified package from the package database"""

    def package_update_all():
        """Update everything from the package database"""

    def package_upgrade_system():
        """Update the entire system point release"""

    def package_list():
        """List installed packages"""

    def package_list_contents():
        """List a packages local contents"""

    def package_help():
        """List the packages help menu"""
