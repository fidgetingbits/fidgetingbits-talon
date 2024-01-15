import pathlib
import subprocess
from talon import Module, actions, app, settings

mod = Module()
mod.setting(
    "notify_use_notify_send",
    type=bool,
    default=False,
    desc="Override the default notification to use notifies_end",
)

first = True
has_notify_send = False
icon_path = pathlib.Path(__file__).parent / "talon.png"


@mod.action_class
class Actions:
    def notify(text: str):
        """Show notification"""
        if settings.get("user.notify_use_notify_send"):
            actions.user.notify_send_notify(text)
        else:
            app.notify(text)

    # FIXME: Replace with notify-send.py
    # Update logic to check if the tool exists after initial start, assuming someone sets the setting, but
    # installs it after the fact.
    # Add a warning the first time that the tool isn't installed, if the tag is set.
    # Also add a warning for if the user is not on Linux, but has the setting
    def notify_send_notify(text: str):
        """Show notification using notify-send"""
        if first:
            # Make sure the tool exists
            if app.platform != "linux":
                has_notify_send = False
            else:
                try:
                    subprocess.check_output(["which", "notify-send"])
                    has_notify_send = True
                except subprocess.CalledProcessError:
                    has_notify_send = False
        if has_notify_send:
            subprocess.Popen(["notify-send", "Talon", f'"{text}", "-i", "{icon_path}"'])
        else:
            app.notify(text)
