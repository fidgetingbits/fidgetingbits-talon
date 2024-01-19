import logging
import os
import pathlib
import pprint

from talon import Context, Module, actions, app, fs, ui
from talon_init import TALON_HOME

ctx = Context()
mod = Module()

ctx.matches = r"""
tag: user.zsh
"""

mod.tag("zsh", desc="Tag for enabling zsh shell support")

plugin_tag_list = [
    "zsh_cd_gitroot",
    "zsh_folder_completion",
    "zsh_zhooks",
]

for entry in plugin_tag_list:
    mod.tag(entry, f"tag to load {entry} zsh plugin commands")


mod.list("zsh_folder_completion", desc="zsh folder completions")
ctx.lists["user.zsh_folder_completion"] = {}

mod.list("zsh_file_completion", desc="zsh file completions")
ctx.lists["user.zsh_file_completion"] = {}


@mod.capture(rule="{user.zsh_folder_completion}")
def zsh_folder_completion(m) -> str:
    """Returns a speakable folder name"""
    return m


@mod.capture(rule="{user.zsh_file_completion}")
def zsh_file_completion(m) -> str:
    """Returns a speakable file name"""
    return m


@mod.capture(rule="({user.zsh_folder_completion} | {user.zsh_file_completion})")
def zsh_path_completion(m) -> str:
    """Returns a speakable file name"""
    return m


if app.platform == "linux":
    completion_base = (
        pathlib.Path(os.environ.get("XDG_RUNTIME_DIR", "/tmp"))
        / "talon/cache/completions"
    )
    zsh_folder_path = completion_base / "talon_zsh_folders"
    zsh_file_path = completion_base / "talon_zsh_files"
else:
    completion_base = TALON_HOME / "cache/completions/"
    # FIXME: use getconf DARWIN_USER_TMP_DIR for mac
    zsh_folder_path = completion_base / "talon_zsh_folders"
    zsh_file_path = completion_base / "talon_zsh_files"

current_zsh_pid = None


def _zsh_cwd_watch_folders(path, flags):
    """Update the folder list based off of a change of working directory"""
    # print(f"_zsh_cwd_watch_folders() Detected an update for {path} with flags {flags}")
    try:
        with open(path, "r") as f:
            folder_list = [os.path.basename(x) for x in f.read().splitlines()]
            if len(folder_list) == 0:
                ctx.lists["user.zsh_folder_completion"] = {}
            else:
                ctx.lists[
                    "user.zsh_folder_completion"
                ] = actions.user.create_spoken_forms_from_list(folder_list)
                # print(f"Updating zsh_folder_completion with {len(folder_list)} entries")
    except Exception as e:
        # If there's no folders in a directory this is expected
        # print(f"zsh.py _zsh_cwd_watch_folders() failed to read {path}: {e}")
        pass


def _zsh_cwd_watch_files(cwd, flags):
    """Update the file list based off of a change of working directory"""
    # print(f"_zsh_cwd_watch_files() Detected an update for {cwd} with flags {flags}")

    try:
        with open(cwd, "r") as f:
            file_list = [os.path.basename(x) for x in f.read().splitlines()]
            if len(file_list) == 0:
                ctx.lists["user.zsh_file_completion"] = {}
            else:
                # print(
                #     f"Updating zsh_file_completion with {len(file_list)} file entries"
                # )
                ctx.lists[
                    "user.zsh_file_completion"
                ] = actions.user.create_spoken_forms_from_list(file_list)
    except Exception as e:
        # If there's no files in a directory this is expected
        # print(f"zsh.py _zsh_cwd_watch_files() failed to read {path}: {e}")
        pass


def _is_zsh_window(window):
    return (
        window.title.startswith("VIM ")
        and "TERM:" in window.title
        and " zsh" in window.title
    )


def _get_zsh_pid(title):
    """Extract the zsh pid from the window title"""
    try:
        pid = int(title.split("term://")[1].split(":")[0].split("/")[-1])
        return pid
    except Exception as e:
        print(f"zsh.py _get_zsh_pid() failed to extract pid from {title}: {e}")


extra_callbacks = []


def _setup_watches(window):
    global zsh_folder_path
    if window == ui.active_window() and _is_zsh_window(window):
        pid = _get_zsh_pid(window.title)
        print(f"zsh.py _setup_watches() detected zsh pid {pid}")
        global current_zsh_pid
        if pid != current_zsh_pid:
            # print(f"zsh.py win_title() detected zsh pid {pid} != {current_zsh_pid}")
            if current_zsh_pid is not None:
                fs.unwatch(
                    f"{zsh_folder_path}.{current_zsh_pid}", _zsh_cwd_watch_folders
                )
                fs.unwatch(f"{zsh_file_path}.{current_zsh_pid}", _zsh_cwd_watch_files)
                for entry in extra_callbacks:
                    print(f"unwatching {entry['watch_file']}")
                    fs.unwatch(
                        f'{entry["watch_file"]}..{current_zsh_pid}', entry["callback"]
                    )

            current_zsh_pid = pid
            # print(f"zsh.py win_title() watching /proc/{current_zsh_pid}/cwd")
            # fs.watch(f"/proc/{pid}/cwd", _zsh_cwd_watch_folders)
            folder_path = f"{zsh_folder_path}.{pid}"
            file_path = f"{zsh_file_path}.{pid}"
            # Pre-run functions just to load any existing data, this is mostly relevant
            # for first executing the shell
            _zsh_cwd_watch_files(file_path, None)
            _zsh_cwd_watch_folders(folder_path, None)
            if os.path.exists(folder_path):
                fs.watch(folder_path, _zsh_cwd_watch_folders)
            if os.path.exists(file_path):
                fs.watch(file_path, _zsh_cwd_watch_files)

            print(f"Setting watch for {len(extra_callbacks)} extra callbacks")
            for entry in extra_callbacks:
                watch_path = f'{entry["watch_file"]}.{pid}'
                # print(f"calling callback for {watch_path}")
                entry["callback"](watch_path, None)
                print(f"Setting watch on {watch_path}")
                fs.watch(watch_path, entry["callback"])
    else:
        if current_zsh_pid is not None:
            fs.unwatch("{zsh_folder_path}.{current_zsh_pid}", _zsh_cwd_watch_folders)
            fs.unwatch("{zsh_file_path}.{current_zsh_pid}", _zsh_cwd_watch_files)
            for entry in extra_callbacks:
                fs.unwatch(
                    f'{entry["watch_file"]}..{current_zsh_pid}', entry["callback"]
                )
            current_zsh_pid = None


def win_focus(window):
    _setup_watches(window)


def win_title(window):
    _setup_watches(window)


ui.register("win_focus", win_title)
ui.register("win_title", win_title)


@mod.action_class
class Actions:
    def zsh_dump_file_completions():
        """Dump add a pretty version of the file completions to the log"""
        logging.info("ZSH File Completions:")
        logging.info(pprint.pformat(ctx.lists["user.zsh_file_completion"]))

    def zsh_dump_folder_completions():
        """Dump add a pretty version of the folder completions to the log"""
        logging.info("ZSH Folder Completions:")
        logging.info(pprint.pformat(ctx.lists["user.zsh_folder_completion"]))

    def zsh_dump_completions():
        """Dump add a pretty version of the completions to the log"""
        actions.user.zsh_dump_folder_completions()
        actions.user.zsh_dump_file_completions()

    def zsh_get_pid():
        """Return the current zsh pid"""
        return current_zsh_pid

    def zsh_register_watch_file_callback(watch_file: str, callback: str):
        """Register a callback for a watch file"""
        global extra_callbacks
        for entry in extra_callbacks:
            if entry["watch_file"] == watch_file:
                # FIXME: Does this work to update the list?
                entry["callback"] = callback
                return
        extra_callbacks.append({"watch_file": watch_file, "callback": callback})
        print("new callback registered")

    def zsh_completion_base_dir():
        """Return the base directory for zsh completions"""
        return completion_base
