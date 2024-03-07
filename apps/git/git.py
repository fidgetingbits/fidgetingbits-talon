import csv
import pprint
from pathlib import Path

from talon import Context, Module, actions, app, resource, settings

GIT_COMMAND = "(git|G)"

mod = Module()
ctx = Context()

mod.list("git_command", desc="Git commands.")
mod.list("git_argument", desc="Command-line git options and arguments.")
mod.list("git_conventional_commits", desc="Git conventional_commits.")
mod.list("git_branches", desc="Git branches in current repo.")
mod.list("git_remotes", desc="Git remotes in current repo.")
mod.setting(
    "git_auto_completion",
    type=bool,
    default=False,
    desc="Enable git auto completion for branches, remotes, etc",
)

ctx.lists["self.git_conventional_commits"] = {
    "feature": "feat",
    "feet": "feat",
    "fix": "fix",
    "documentation": "docs",
    "docks": "docs",
    "style": "style",
    "refactor": "refactor",
    "performance": "perf",
    "test": "test",
    "chore": "chore",
    "revert": "revert",
    "breaking": "BREAKING CHANGE",
}

dirpath = Path(__file__).parent
arguments_csv_path = str(dirpath / "git_arguments.csv")
commands_csv_path = str(dirpath / "git_commands.csv")


def make_list(path):
    with resource.open(path, "r") as f:
        rows = list(csv.reader(f))
    mapping = {}
    # ignore header row
    for row in rows[1:]:
        if len(row) == 0:
            continue
        if len(row) == 1:
            row = row[0], row[0]
        if len(row) > 2:
            print("{path!r}: More than two values in row: {row}. Ignoring the extras.")
        output, spoken_form = row[:2]
        spoken_form = spoken_form.strip()
        mapping[spoken_form] = output
    return mapping


ctx.lists["self.git_argument"] = make_list(arguments_csv_path)
ctx.lists["self.git_command"] = make_list(commands_csv_path)


@mod.capture(rule=GIT_COMMAND)
def git(m) -> str:
    """Verbs to use for git commands"""
    return str(m)


@mod.capture(rule="{user.git_argument}+")
def git_arguments(m) -> str:
    """A non-empty sequence of git command arguments, preceded by a space."""
    return " " + " ".join(m.git_argument_list)


@mod.action_class
class Actions:
    def git_dump_completions():
        """Dump add a pretty version of the git branch completions to the log"""
        print("git Auto Completions:")
        print("Branches:")
        print(pprint.pformat(ctx.lists["user.git_branches"]))
        print("Remotes:")
        print(pprint.pformat(ctx.lists["user.git_remotes"]))
        print("Enabled: ", settings.get("user.git_auto_completion"))


def on_ready():
    actions.user.zsh_register_watch_file_callback_basic(
        "git_branches", "user.git_auto_completion", "user.git_branches"
    )
    actions.user.zsh_register_watch_file_callback_basic(
        "git_remotes", "user.git_auto_completion", "user.git_remotes"
    )


app.register("ready", on_ready)
