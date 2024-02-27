import csv
import pprint
from pathlib import Path

from talon import Context, Module, actions, app, resource, settings

mod = Module()
ctx = Context()

mod.list("git_command", desc="Git commands.")
mod.list("git_argument", desc="Command-line git options and arguments.")
mod.list("git_conventional_commits", desc="Git conventional_commits.")
mod.list("git_branches", desc="Git conventional_commits.")
mod.setting(
    "git_branch_auto_completion",
    type=bool,
    default=False,
    desc="Enable git branch auto completion",
)

ctx.lists["user.git_branches"] = {}
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


@mod.capture(rule="{user.git_argument}+")
def git_arguments(m) -> str:
    """A non-empty sequence of git command arguments, preceded by a space."""
    return " " + " ".join(m.git_argument_list)


@mod.action_class
class Actions:
    def git_dump_completions():
        """Dump add a pretty version of the git branch completions to the log"""
        print("git Branch Completions:")
        print(pprint.pformat(ctx.lists["user.git_branches"]))
        print("Enabled: ", settings.get("user.git_branch_auto_completion"))


# FIXME: This should just be a default function for basic parsing and we pass the list name in, since it duplicates
# everywhere?
# It won't work for all, but for ones with just basic unmodified lists it should be fine.
def update_git_branches(file, flags):
    """Update the available git branches based off of a change of working directory"""
    # print("calling update_git_branches")
    # actions.user.update_completion_list(ctx.lists["user.git_branches"], path)
    try:
        path = actions.user.zsh_completion_base_dir()
        with open(f"{path}/{file}", "r") as f:
            commands = f.read().splitlines()
            if len(commands) == 0:
                ctx.lists["user.git_branches"] = {}
            else:
                ctx.lists[
                    "user.git_branches"
                ] = actions.user.create_spoken_forms_from_list(commands)
    except Exception:
        pass


def on_ready():
    if settings.get("user.git_branch_auto_completion"):
        actions.user.zsh_register_watch_file_callback(
            "git_branches", update_git_branches
        )


app.register("ready", on_ready)
