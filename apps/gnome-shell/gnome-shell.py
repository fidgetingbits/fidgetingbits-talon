import subprocess
from typing import Optional, Union

from talon import Context, Module, actions, app, settings

mod = Module()
ctx = Context()

mod.tag("gnome-shell", desc="tag for loading gnome-shell related files")

ctx.matches = """
tag: user.gnome-shell
"""