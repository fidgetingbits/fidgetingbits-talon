# This allows you to switch the operating system paths for a given window, so if you're using a vim or are tunneled into
# a different operating system you can use its paths

from talon import Context, Module, actions, app, settings, ui

mod = Module()
ctx = Context()

mod.setting(
    "path_manager_pinning",
    type=bool,
    default=False,
    desc="Pins path os tags to shell-specific PID contexts. Requires vim terminals atm.",
)

path_os_list = [
    {"tag": "path_os_darwin", "desc": "Darwin paths"},
    {"tag": "path_os_linux", "desc": "Linux paths"},
    {"tag": "path_os_windows", "desc": "Windows paths"},
]

mod.list("path_os", "List of operating system path options")
ctx.lists["user.path_os"] = {
    "mac": "path_os_darwin",
    "darwin": "path_os_darwin",
    "linux": "path_os_linux",
    "windows": "path_os_windows",
}

for path in path_os_list:
    mod.tag(path["tag"], path["desc"])

if app.platform == "mac":
    default_path_os = "path_os_darwin"
elif app.platform == "linux":
    default_path_os = "path_os_linux"
elif app.platform == "windows":
    default_path_os = "path_os_windows"
current_path_os = default_path_os

last_title = None


@mod.action_class
class PathManagerActions:
    def path_manager_reset():
        """Resets the current path to the operating system's default"""
        if settings.get("user.path_manager_pinning", False):
            actions.user.pin_tag(f"user.{default_path_os}", "path_manager")
        else:
            global current_os_version
            current_os_version = default_path_os
            ctx.tags = [f"user.{current_os_version}"]
            app.notify(f"Path manager set to {current_os_version}")

    def path_manager_set(path_os: str):
        """Set the path manager to the specified path_os"""
        if settings.get("user.path_manager_pinning", False):
            actions.user.pin_tag(f"user.{path_os}", "path_manager")
            app.notify(f"Pinned path manager to {path_os}")
        else:
            global current_path_os
            current_path_os = path_os
            ctx.tags = [f"user.{current_path_os}"]
            app.notify(f"Path manager set to {path_os}")

    def path_manager_show():
        """Show the current path manager"""
        if settings.get("user.path_manager_pinning", False):
            path_os = actions.user.find_pinned_tag("path_manager")
            if path_os is not None:
                app.notify(f"Current pinned path manager: {path_os}")
            else:
                app.notify("No path manager set")
        else:
            global current_path_os
            if current_path_os is None:
                app.notify("No path manager set")
            else:
                app.notify(f"Current path manager: {current_path_os}")


def on_ready():
    actions.user.path_manager_reset()


def win_title(window):
    # FIXME: Eventually this should just be any terminal and we pull out the pid even if it's not zsh, but need to test
    # if "user.zsh" not in registry.tags:
    #     return
    global last_title
    if settings.get("user.path_manager_pinning", False):
        if window == ui.active_window() and window.title != last_title:
            last_title = window.title
            actions.user.path_manager_reset()


app.register("ready", on_ready)
ui.register("win_title", win_title)
