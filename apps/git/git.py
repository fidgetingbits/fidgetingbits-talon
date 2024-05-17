import csv
import subprocess
from pathlib import Path

from talon import Context, Module, actions, resource

GIT_COMMAND = "(git|G)"

mod = Module()
ctx = Context()

mod.list("git_command", desc="Git commands.")
mod.list("git_argument", desc="Command-line git options and arguments.")
mod.list("git_conventional_commits", desc="Git conventional_commits.")
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


mod.list("git_branches", desc="Branches in the current git repository.")
mod.list("git_remotes", desc="Remotes in the current git repository.")


@ctx.dynamic_list("user.git_branches")
def users_git_branches(m) -> dict[str, str]:
    """A dynamic list of available git branches"""

    output = subprocess.check_output(
        ("git", "branch", "-a"), cwd=actions.user.zsh_get_cwd()
    ).decode("utf-8")
    if not output:
        print("no output")
        return {}

    commands = []
    for line in output.splitlines():
        if line.startswith("*"):
            line = line.split("*")[1]
        if "remotes/" in line:
            line = line.split("/")[-1]
            # Deal with this remotes/origin/HEAD -> origin/dev
            if line.startswith("HEAD"):
                line = "head"
        if line not in commands:
            commands.append(line.strip())
    # print(commands)
    return actions.user.create_spoken_forms_from_list(commands)


@ctx.dynamic_list("user.git_remotes")
def user_git_remotes(m) -> dict[str, str]:
    """A dynamic list of available git branches"""

    output = subprocess.check_output(
        ("git", "remote"), cwd=actions.user.zsh_get_cwd()
    ).decode("utf-8")
    if not output:
        print("no output")
        return {}

    commands = []
    for line in output.splitlines():
        if line.startswith("*"):
            line = line.split("*")[1]
        commands.append(line.strip())
    return actions.user.create_spoken_forms_from_list(commands)
