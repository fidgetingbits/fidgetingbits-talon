from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

ctx.matches = r"""
app: virtualbox_manager
"""


# Generic menu interaction code for talon
@mod.action_class
class Actions:
    def menu_key(key: str, release: bool = True, count: int = 1):
        """Access some menu entry via alt-based key press."""
        actions.key("alt:down")
        actions.key(f"{key}:{count}")
        if release:
            actions.key("alt:up")


def mouse_safe_menu_access(func):
    """Decorator to disable mouse control before accessing a menu and re-enable afterwards."""

    def wrapper():
        """Disable and re-enable mouse if required"""
        reenable_control_mouse = False
        reenable_control_zoom_mouse = False
        if actions.tracking.control_enabled():
            actions.user.mouse_toggle_control_mouse()
            reenable_control_mouse = True
        if actions.tracking.control_zoom_enabled():
            actions.user.mouse_toggle_zoom_mouse()
            reenable_control_zoom_mouse = True
        func()
        if reenable_control_mouse:
            actions.user.mouse_toggle_control_mouse()
        if reenable_control_zoom_mouse:
            actions.user.mouse_toggle_zoom_mouse()

    return wrapper


# Note we do wrapped indirection here for now because if we wrap a action
# function, it doesn't get exposed correctly through talon.
@mouse_safe_menu_access
def vm_power_off():  # type: () -> None
    """Machine->Stop->Power Off"""
    actions.user.machine_stop_menu_key("w")


@mod.action_class
class Actions:
    def machine_menu(release: bool = True):
        """Access the Machine menu."""
        actions.user.menu_key("m", release=release, count=3)

    def machine_stop_menu(release: bool = True):
        """Machine->Stop"""
        actions.user.machine_menu(release=False)
        actions.user.menu_key("s", release=release, count=2)

    def machine_stop_menu_key(key: str):
        """Machine->Stop->key"""
        actions.user.machine_stop_menu(release=False)
        actions.key(key)
        actions.key("alt:up")

    def vm_power_off():  # type: () -> None
        """Machine->Stop->Power Off"""
        vm_power_off()
