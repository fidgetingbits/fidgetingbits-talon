import pprint

from talon import Context, Module, actions, app, settings

mod = Module()
mod.setting(
    "justfile_auto_completion",
    type=bool,
    default=False,
    desc="Whether or not to automatically complete just commands with justfile contents",
)

ctx = Context()
ctx.matches = r"""
tag: user.just_commands
"""

mod.list("justfile_commands", desc="Just commands.")


def on_ready():
    actions.user.zsh_register_watch_file_callback_basic(
        "justfile_commands", "user.justfile_auto_completion", "user.justfile_commands"
    )


app.register("ready", on_ready)
