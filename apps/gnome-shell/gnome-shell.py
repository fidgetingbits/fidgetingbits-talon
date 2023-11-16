import subprocess
from typing import Optional, Union

from talon import Context, Module, actions, app, settings

mod = Module()
ctx = Context()

mod.tag("gnome-shell", desc="tag for loading gnome-shell related files")

ctx.matches = """
tag: user.gnome-shell
"""


@ctx.action_class("app")
class AppActions:
    def window_open():
        actions.key("ctrl-shift-n")

    def window_close():
        actions.key("ctrl-shift-w")


@ctx.action_class("user")
class UserActions:
    def window_maximize():
        actions.key("alt-f10")
