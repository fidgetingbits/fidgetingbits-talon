from talon import Context, Module, actions, app, imgui, registry, settings, ui

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.package_manager
"""
pinned_contexts = []
mod.setting(
    "package_manager_default",
    type=str,
    default=None,
    desc="Default package manager to use",
)
mod.setting(
    "package_manager_pinning",
    type=bool,
    default=False,
    desc="Pins package tags to shell-specific PID contexts. Requires vim terminals atm.",
)

mod.mode("packager_picker_open")

mod.tag("package_manager", desc="linux package manager")
packager_list = [
    {"tag": "packager_brew", "desc": "Mac homebrew packager"},
    {"tag": "packager_yay", "desc": "Arch Linux YAY packager"},
    {"tag": "packager_pacman", "desc": "Arch Linux core packager"},
    {"tag": "packager_pamac", "desc": "Manjaro Linux packager"},
    {"tag": "packager_apk", "desc": "Alpine Linux packager"},
    {"tag": "packager_apt", "desc": "Debian/Ubuntu Linux packager"},
    {"tag": "packager_snap", "desc": "Snap packager"},
    {"tag": "packager_zypper", "desc": "SuSE packager"},
    {"tag": "packager_dnf", "desc": "Fedora/Redhat DNF packager"},
    {"tag": "packager_yum", "desc": "Fedora/Redhat YUM packager"},
    {"tag": "packager_npm", "desc": "Node package manager"},
    {"tag": "packager_nix", "desc": "Nix package manager"},
]
mod.list("package_managers", "List of common package managers for Darwin/Linux")

ctx.lists["user.package_managers"] = {
    "brew": "packager_brew",
    "yay": "packager_yay",
    "pack man": "packager_pacman",
    "pam": "packager_pamac",
    "alpine": "packager_apk",
    "debian": "packager_apt",
    "ubuntu": "packager_apt",
    "snap": "packager_snap",
    "suse": "packager_zypper",
    "zipper": "packager_zypper",
    "D N F": "packager_dnf",
    "yum": "packager_yum",
    "node": "packager_npm",
    "N P M": "packager_npm",
    "nix": "packager_nix",
}

for packager in packager_list:
    mod.tag(packager["tag"], packager["desc"])
current_packager = None

main_screen = ui.main_screen()
last_title = None


def close_packager_picker():
    gui.hide()
    actions.mode.disable("user.packager_picker_open")


@imgui.open(y=0, x=main_screen.width / 2.6)
def gui(gui: imgui.GUI):
    gui.line()
    gui.text("Active Packager:")

    gui.line()

    if gui.button("Hide"):
        close_packager_picker()


@mod.action_class
class UserActions:
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

    def package_dependencies():
        """List packages dependent on a specific package"""

    def package_help():
        """List the packages help menu"""


@mod.action_class
class PackageManagerActions:
    def package_manager_reset():
        """Reset the package manager to the default"""
        # print("package_manager_reset")
        default_packager = settings.get(
            "user.package_manager_default",
            "brew" if app.platform == "mac" else "apt",
        )
        # Prefer people to just use the name of the packager, but don't break if someone uses the full tag name
        if default_packager.startswith("user."):
            default_packager = default_packager[5:]
        elif default_packager.startswith("packager_"):
            default_packager = default_packager[9:]
        elif default_packager.startswith("user.packager_"):
            default_packager = default_packager[14:]

        if settings.get("user.package_manager_pinning", False):
            actions.user.pin_tag(f"user.packager_{default_packager}", "package_manager")
        else:
            global current_packager
            current_packager = default_packager
            ctx.tags = [f"user.packager_{current_packager}"]
            app.notify(f"Package manager set to {current_packager}")

    def package_manager_set(packager: str):
        """Set the package manager to the specified packager"""
        if settings.get("user.package_manager_pinning", False):
            actions.user.pin_tag(f"user.{packager}", "package_manager")
            app.notify(f"Pinned package manager to {packager}")
        else:
            global current_packager
            current_packager = packager
            ctx.tags = [f"user.{current_packager}"]
            app.notify(f"Package manager set to {packager}")

    def package_manager_show():
        """Show the current package manager"""
        if settings.get("user.package_manager_pinning", False):
            packager = actions.user.find_pinned_tag("package_manager")
            if packager is not None:
                app.notify(f"Current pinned package manager: {packager}")
            else:
                app.notify("No package manager set")
        else:
            global current_packager
            if current_packager is None:
                app.notify("No package manager set")
            else:
                app.notify(f"Current package manager: {current_packager}")


def on_ready():
    actions.user.package_manager_reset()


def win_title(window):
    global last_titlei
    # FIXME: Eventually this should just be any terminal and we pull out the pid even if it's not zsh, but need to test
    if "user.zsh" not in registry.tags:
        return
    global last_title
    if window == ui.active_window() and window.title != last_title:
        last_title = window.title
        actions.user.package_manager_reset()


app.register("ready", on_ready)
ui.register("win_title", win_title)
