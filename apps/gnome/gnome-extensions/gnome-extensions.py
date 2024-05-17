import subprocess

from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: terminal
and tag: user.gnome-shell
"""

mod.list("gnome_extensions", desc="Extensions currently installed in Gnome shell")


@ctx.dynamic_list("user.gnome_extensions")
def user_gnome_extensions(m) -> dict[str, str]:
    """A dynamic list of installed gnome extensions"""
    output = subprocess.check_output(("gnome-extensions", "list")).decode("utf-8")
    if not output:
        print("no output")
        return {}

    return actions.user.create_spoken_forms_from_list(output.splitlines())
