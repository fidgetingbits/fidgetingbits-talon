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

mod.list("justfile_commands", desc="justfile command completions")
ctx.lists["user.justfile_commands"] = {}


def on_ready():
    actions.user.zsh_register_watch_file_callback_basic(
        "justfile_commands", "user.justfile_auto_completion", "user.justfile_commands"
    )


@mod.action_class
class Actions:
    def just_dump_completions():
        """Dump add a pretty version of the justfile completions to the log"""
        print("Just Command Completions:")
        print(pprint.pformat(ctx.lists["user.justfile_commands"]))
        print("Enabled: ", settings.get("user.justfile_auto_completion"))


app.register("ready", on_ready)
