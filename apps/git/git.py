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


@mod.capture(rule="{user.git_conventional_commits} [cat <user.word>]")
def git_conventional_commits(m) -> str:
    """A non-empty sequence of git command arguments, preceded by a space."""
    if len(list(m)) == 3:
        return f"{m.git_conventional_commits}({m.word}): "
    return f"{m.git_conventional_commits}: "


mod.list("git_branch", desc="Branches in the current git repository.")
mod.list("git_tag", desc="Tags in the current git repository.")
mod.list("git_remote", desc="Remotes in the current git repository.")
mod.list("git_modified_file", desc="Git tracked files that have been modified")
mod.list("git_untracked_file", desc="Git untracked files")
mod.list("git_staged_file", desc="Git tracked files that have been staged")


def git_status():
    return subprocess.check_output(
        ("git", "status", "-s"), cwd=actions.user.get_cwd()
    ).decode("utf-8")


@ctx.dynamic_list("user.git_staged_file")
def user_git_staged_file(m) -> dict[str, str]:
    """A dynamic list of staged git files"""

    print("dynamic_list")
    # print("user_git_staged_file()")
    output = git_status()
    if not output:
        print("user_git_staged_file(): no output")
        return {}

    commands = []
    # print(output)
    for line in output.splitlines():
        # man git status for more info
        if line[:1] in ["A", "M", "D", "R", "C", "U"]:
            line = line.split(" ")[-1]
            commands.append(line.strip())
    # print(commands)
    return actions.user.create_spoken_forms_from_list(commands)


@mod.capture(rule="{user.git_staged_file}")
def git_staged_file(m) -> str:
    """Returns one git staged file"""
    return m


@mod.capture(rule="<user.git_staged_file> [and <user.git_staged_file>]")
def git_staged_files(m) -> str:
    """Returns one or more git staged files"""
    return " ".join([str(s) for s in m.git_staged_file_list])


@ctx.dynamic_list("user.git_untracked_file")
def user_git_untracked_file(m) -> dict[str, str]:
    """A dynamic list of untracked git files"""

    output = git_status()
    if not output:
        return {}

    commands = []
    for line in output.splitlines():
        if line.startswith("?"):
            line = line.split(" ")[-1]
            commands.append(line.strip())

    return actions.user.create_spoken_forms_from_list(commands)


@mod.capture(rule="{user.git_untracked_file}")
def git_untracked_file(m) -> str:
    """Returns one git untracked tile"""
    return m


@mod.capture(rule="<user.git_untracked_file> [and <user.git_untracked_file>]")
def git_untracked_files(m) -> str:
    """Returns one or more git untracked files"""
    return " ".join([str(s) for s in m.git_untracked_file_list])


@ctx.dynamic_list("user.git_modified_file")
def user_git_modified_file(m) -> dict[str, str]:
    """A dynamic list of modified tracked git files"""
    print("user_git_modified_files")
    output = git_status()
    if not output:
        return {}

    commands = []
    for line in output.splitlines():
        if line.startswith(" M ") or line.startswith("MM"):
            line = line.split(" ")[-1]
            commands.append(line.strip())
    # print(commands)
    return actions.user.create_spoken_forms_from_list(commands)


@mod.capture(rule="{user.git_modified_file}")
def git_modified_file(m) -> str:
    """Returns modified tracked git file"""
    return m


@mod.capture(rule="<user.git_modified_file> [and <user.git_modified_file>]")
def git_modified_files(m) -> str:
    """Returns one or more modified tracked git files"""
    return " ".join([str(s) for s in m.git_modified_file_list])


@ctx.dynamic_list("user.git_branch")
def user_git_branch(m) -> dict[str, str]:
    """A dynamic list of available git branches"""

    output = subprocess.check_output(
        ("git", "branch", "-a"), cwd=actions.user.get_cwd()
    ).decode("utf-8")
    if not output:
        print("users_git_branch(): no output")
        return {}

    commands = []
    for line in output.splitlines():
        if line.startswith("*"):
            line = line.split("*")[1]
        if "remotes/" in line:
            # remotes/origin that already exist, we skip
            if line.startswith("remotes/origin"):
                line = line.split("/")[-1]
                if line in commands:
                    continue
            else:
                line = line[len("  remotes/") :]

            # Deal with this remotes/origin/HEAD -> origin/dev
            if line.startswith("HEAD"):
                line = "head"
        if line not in commands:
            commands.append(line.strip())
    # print(commands)
    return actions.user.create_spoken_forms_from_list(commands)


@mod.capture(rule="{user.git_branch}")
def git_branch(m) -> str:
    """Returns one git branch"""
    return m


@mod.capture(rule="<user.git_branch> [and <user.git_branch>]")
def git_branches(m) -> str:
    """Returns one or more git branches"""
    return " ".join([str(s) for s in m.git_branch_list])


@ctx.dynamic_list("user.git_tag")
def user_git_tag(m) -> dict[str, str]:
    """A dynamic list of available git tags"""

    output = subprocess.check_output(("git", "tag"), cwd=actions.user.get_cwd()).decode(
        "utf-8"
    )
    if not output:
        print("no output")
        return {}

    commands = []
    for line in output.splitlines():
        commands.append(line.strip())
    return actions.user.create_spoken_forms_from_list(commands)


@mod.capture(rule="{user.git_tag}")
def git_tag(m) -> str:
    """Returns one or more git staged files"""
    return m


@mod.capture(rule="<user.git_tag> [and <user.git_tag>]")
def git_tages(m) -> str:
    """Returns one or more git tags"""
    return " ".join([str(s) for s in m.git_tag_list])


@ctx.dynamic_list("user.git_remote")
def user_git_remote(m) -> dict[str, str]:
    """A dynamic list of available git branches"""

    output = subprocess.check_output(
        ("git", "remote"), cwd=actions.user.get_cwd()
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


@mod.capture(rule="{user.git_remote} [and {user.git_remote}]")
def git_remote(m) -> str:
    """Returns one git remote"""
    return " ".join(m.git_remote_list)


@mod.capture(rule="<user.git_remote> [and <user.git_remote>]")
def git_remotes(m) -> str:
    """Returns one or more git remotes"""
    return " ".join([str(s) for s in m.git_remote_list])
