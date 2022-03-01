from talon import Context, Module, actions, settings, ui, app

mod = Module()

mod.tag("i3wm", desc="tag for loading i3wm related files")
mod.setting(
    "i3_config_path",
    type=str,
    default="~/.i3/config",
    desc="Where to find the configuration path",
)
mod.setting(
    "i3_mod_key",
    type=str,
    default="super",
    desc="The default key to use for i3wm commands",
)

# XXX - this should use i3-msg commands instead
def i3wm_window_resize(size, grow=True):
    """resizes the selected window by the specified number of key movements"""
    actions.user.system_command('i3-msg mode "resize"')
    if grow:
        actions.key(f"right:{size}")
        actions.key(f"down:{size}")
    else:
        actions.key(f"left:{size}")
        actions.key(f"up:{size}")
    # escape resize mode
    actions.key("escape")
    # center window
    actions.user.system_command("i3-msg move position center")


@mod.action_class
class Actions:
    def i3wm_launch():
        """Trigger the i3 launcher: ex rofi"""
        key = settings.get("user.i3_mod_key")
        actions.key(f"{key}-d")

    def i3wm_shell():
        """Launch a shell"""
        key = settings.get("user.i3_mod_key")
        actions.key(f"{key}-enter")

    def i3wm_testing_shell():
        """Launch a shell"""
        key = settings.get("user.i3_mod_key")
        actions.key(f"{key}-shift-enter")

    def i3wm_lock():
        """Trigger the lock screen"""
        key = settings.get("user.i3_mod_key")
        actions.key(f"{key}-shift-x")

    def i3wm_window_grow(times: int =1):
        """Resize the focused window larger"""
        i3wm_window_resize(10*times, grow=True)

    def i3wm_window_shrink(times: int =1):
        """Resize the focused window smaller"""
        i3wm_window_resize(10*times, grow=False)

    def i3wm_window_adjust_height_up(size: int):
        """resizes the selected window by the specified number of key movements"""
        actions.user.system_command(f"i3-msg 'resize grow height {size}px'")

    def i3wm_window_adjust_height_down(size: int):
        """resizes the selected window by the specified number of key movements"""
        actions.user.system_command(f"i3-msg 'resize shrink height {size}px'")

    def i3wm_window_adjust_width_out(size: int):
        """resizes the selected window by the specified number of key movements"""
        actions.user.system_command(f"i3-msg 'resize grow width {size}px'")

    def i3wm_window_adjust_width_in(size: int):
        """resizes the selected window by the specified number of key movements"""
        actions.user.system_command(f"i3-msg 'resize shrink width {size}px'")

    # Other people often use actions.user.notify() so we need to supply
    # something... here I just rely on my monkey patch, to redirected
    # through to dunst
    def notify(text: str):
        """Show notification"""
        app.notify(subtitle=text)
