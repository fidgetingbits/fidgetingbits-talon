import os
import socket
import subprocess

from talon import app, imgui, ui


def monkey_notify(body="", title="", subtitle="", *kwargs):
    subprocess.Popen(
        ["notify-send.sh", "-t", "3000", "-f", "-u", "low", f'"{subtitle}"']
    )


def monkey_focus(self, *kwargs):
    if self.active_window.id == -1:
        os.system(f"i3-msg '[class=\"(?){self.name}\"] focus'")
    else:
        os.system(f"i3-msg '[id=\"{self.active_window.id}\"] focus'")


def install_monkey_show():
    """On i3wm the pop up windows often minimize to unviewable size

    Also no way to actually resize them. show() auto refreshes,
    so is more cpu intensive, but does not have this problem
    """

    print("Installing fidget imgui.GUI freeze override monkey patch")
    imgui.GUI.freeze = imgui.GUI.show


def install_monkey_focus():
    """Install a monkey patch to use i3 to focus windows."""

    out = None
    try:
        out = subprocess.check_output("which i3-msg", shell=True)
    except subprocess.CalledProcessError:
        print("WARNING: i3-msg not found. Skipping monkey patch")
    if out:
        print("Installing fidget i3-msg focus monkey patch")
        ui.App.focus = monkey_focus


def install_monkey_notify():
    """Install a monkey patch to use dunst instead of qt notifications.

    This is mostly useful for things like i3, or if you just generally think
    the notifications are too hard to notice.
    """

    out = None
    try:
        out = subprocess.check_output("which notify-send.sh", shell=True)
    except subprocess.CalledProcessError:
        print("WARNING: notify-send.sh not found. Skipping monkey patch")
    if out:
        print("Installing fidget notify-send.sh notify monkey patch")
        app.notify = monkey_notify


def install_monkey_patches():
    """Installs a number of monkey patches if the associated tools are found"""

    hostname = socket.gethostname()
    if hostname in host_patches:
        print(f"Installing fidget monkey patches for {hostname}")
        for func in host_patches[hostname]:
            func()
    else:
        print(
            f"WARNING: host: {hostname} not found in host_patches list. If you need monkey patch, modify monkey_patching.py"
        )
    # install_monkey_notify()
    # install_monkey_focus()
    # install_monkey_show()


# I have mutliple hosts and currently some aren't using i3 and notify-send now, so I
# need to break out who gets what.

host_patches = {"oedo": [install_monkey_focus]}

install_monkey_patches()
