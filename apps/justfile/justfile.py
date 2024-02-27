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
    actions.user.zsh_register_watch_file_callback(
        "justfile_commands", update_justfile_commands
    )
    # print("Registered justfile watch callback")


def update_justfile_commands(cwd, flags):
    """Update the available justfile commands based off of a change of working directory"""
    if not settings.get("user.justfile_auto_completion"):
        return
    # print(f"watch_justfile_commands called, with {cwd}")

    try:
        path = actions.user.zsh_completion_base_dir()

        with open(f"{path}/{cwd}", "r") as f:
            commands = f.read().splitlines()
            if len(commands) == 0:
                # print("No justfile commands found")
                ctx.lists["user.justfile_commands"] = {}
            else:
                ctx.lists["user.justfile_commands"] = (
                    actions.user.create_spoken_forms_from_list(commands)
                )
            # print(f"Updated justfile_commands with {len(commands)} entries")
    except Exception:
        pass


@mod.action_class
class Actions:
    def just_dump_completions():
        """Dump add a pretty version of the justfile completions to the log"""
        print("Just Command Completions:")
        print(pprint.pformat(ctx.lists["user.justfile_commands"]))
        print("Enabled: ", settings.get("user.justfile_auto_completion"))


app.register("ready", on_ready)
