import os
import pprint
import subprocess
import typing
from pathlib import Path

from talon import Context, Module, actions, app

# path to community/knausj root directory
REPO_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.join(REPO_DIR, "settings")
CURSORLESS_SETTINGS_DIR = os.path.join(SETTINGS_DIR, "cursorless-settings")
CURSORLESS_SETTINGS_EXPERIMENTAL_DIR = os.path.join(
    CURSORLESS_SETTINGS_DIR, "experimental"
)

mod = Module()
ctx = Context()

# FIXME: These to just use this speakable API and be automated
mod.list("talon_settings_csv", desc="Absolute paths to talon user settings csv files.")
settings_folders = [
    SETTINGS_DIR,
    CURSORLESS_SETTINGS_DIR,
    CURSORLESS_SETTINGS_EXPERIMENTAL_DIR,
]

def on_ready():
    speakable = {}
    for folder in settings_folders:
        for file_name in os.listdir(folder):
            if file_name.endswith(".csv"):
                name = file_name[:-4]
                speakable[name] = os.path.join(folder, file_name)
    # pprint.pprint(actions.user.create_spoken_forms_from_map(speakable))
    ctx.lists["self.talon_settings_csv"] = actions.user.create_spoken_forms_from_map(
        speakable
    )
app.register("ready", on_ready)

@mod.action_class
class ModuleActions:
    def edit_text_file(path: typing.Optional[str]):
        """Tries to open a file in the user's preferred text editor."""


winctx, linuxctx, macctx = Context(), Context(), Context()
winctx.matches = "os: windows"
linuxctx.matches = "os: linux"
macctx.matches = "os: mac"


@winctx.action_class("self")
class WinActions:
    def edit_text_file(path):
        # If there's no applications registered that can open the given type
        # of file, 'edit' will fail, but 'open' always gives the user a
        # choice between applications.
        try:
            os.startfile(path, "edit")
        except OSError:
            os.startfile(path, "open")


@macctx.action_class("self")
class MacActions:
    def edit_text_file(path):
        # -t means try to open in a text editor.
        open_with_subprocess(
            path, ["/usr/bin/open", "-t", Path(path).expanduser().resolve()]
        )


@linuxctx.action_class("self")
class LinuxActions:
    def edit_text_file(path):
        # we use xdg-open for this even though it might not open a text
        # editor. we could use $EDITOR, but that might be something that
        # requires a terminal (eg nano, vi).
        open_with_subprocess(
            path, ["/usr/bin/xdg-open", Path(path).expanduser().absolute()]
        )


# Helper for linux and mac.
def open_with_subprocess(path, args):
    """Tries to open a file using the given subprocess arguments."""
    try:
        return subprocess.run(args, timeout=0.5, check=True)
    except subprocess.TimeoutExpired:
        app.notify(f"Timeout trying to open file for editing: {path}")
        raise
    except subprocess.CalledProcessError:
        app.notify(f"Could not open file for editing: {path}")
        raise
