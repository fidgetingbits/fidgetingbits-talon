from pathlib import Path
from talon import Module, actions, ui

mod = Module()


# FIXME: Test starting folder, using something like /^<path>/
@mod.scope
def scope():
    return {"working_folder": {working_folder()}}


def working_folder():
    try:
        cwd = str(actions.user.get_cwd())
        # None means action failed
        if cwd:
            if cwd.startswith(str(Path.home())):
                cwd = cwd.replace(str(Path.home()), "~")
        return cwd
    except Exception as e:
        # print(f"working_folder() threw exception: {e}")
        return None


ui.register("win_title", scope.update)
ui.register("win_focus", scope.update)
