from pathlib import Path

from talon import Context, Module, actions, settings

mod = Module()
mod.setting(
    "justfile_auto_populate",
    type=bool,
    default=False,
    desc="Whether or not try to find a justfile in a git project and auto populate commands.",
)


# FIXME: Apparently this isn't perfect, but I don't want to import git
def find_justfile(path):
    "Find repository root from the path's parents"

    for path in [Path(path)] + list(Path(path).parents):
        justfile = path / Path("justfile").resolve()
        print(f"Testing {justfile}")
        if justfile.is_file():
            return justfile
    return None


@mod.action_class
class Actions:
    def justfile_populate_commands(cwd: str):
        """Populate commands from justfile"""
        if not settings.get("user.justfile_auto_populate"):
            print("disabled")
            return

        justfile = find_justfile(cwd)
        if not justfile:
            print("No justfile found")
            return
        print("Found justfile, populating commands")
