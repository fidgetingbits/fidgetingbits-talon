import os
import socket
import logging
import selectors
import pprint
import pathlib
from talon import Context, Module, ui, fs, actions
from talon_init import TALON_HOME

from . import events

ctx = Context()
mod = Module()

ctx.matches = r"""
tag: user.zsh
"""

mod.tag("zsh", desc="Tag for enabling zsh shell support")

plugin_tag_list = [
    "zsh_cd_gitroot",
    "zsh_folder_completion",
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


zsh_folder_path = TALON_HOME / "/cache/completions/talon_zsh_folders"
zsh_file_path = TALON_HOME / "/cache/completions/talon_zsh_files"
current_zsh_pid = None


def _zsh_cwd_watch_folders(path, flags):
    """Update the folder list based off of a change of working directory"""
    print(f"Detected an update for {path} with flags {flags}")
    with open(path, "r") as f:
        folder_list = f.read().splitlines()
        # print(f"zsh.py: folder_list = {folder_list}")
        if len(folder_list) == 0:
            ctx.lists["user.zsh_folder_completion"] = {}
        else:
            ctx.lists[
                "user.zsh_folder_completion"
            ] = actions.user.create_spoken_forms_from_list(folder_list)


def _zsh_cwd_watch_files(path, flags):
    """Update the folder list based off of a change of working directory"""
    print(f"Detected an update for {path} with flags {flags}")
    with open(path, "r") as f:
        file_list = f.read().splitlines()
        # print(f"zsh.py: file_list = {file_list}")
        # It would be nice to be able to tell whether or not the list changed but
        # because we're using the create spoken form in the list that we create we can
        # actually compare it directly here, so we might need to create a copy of the
        # original file list and compare that instead.
        if len(file_list) == 0:
            ctx.lists["user.zsh_file_completion"] = {}
        else:
            ctx.lists[
                "user.zsh_file_completion"
            ] = actions.user.create_spoken_forms_from_list(file_list)


def _is_zsh_window(window):
    return (
        window.title.startswith("VIM ")
        and "TERM:" in window.title
        and " zsh " in window.title
    )


def _get_zsh_pid(title):
    """Extract the zsh pid from the window title"""
    try:
        pid = int(title.split("term://")[1].split(":")[0].split("/")[-1])
        return pid
    except Exception as e:
        print(f"zsh.py _get_zsh_pid() failed to extract pid from {title}: {e}")


def win_focus(window):
    if _is_zsh_window(window):
        pid = _get_zsh_pid(window.title)
        print(f"zsh.py win_focus() detected zsh pid {pid}")


def win_title(window):
    global zsh_folder_path
    if window == ui.active_window() and _is_zsh_window(window):
        pid = _get_zsh_pid(window.title)
        global current_zsh_pid
        if pid != current_zsh_pid:
            # print(f"zsh.py win_title() detected zsh pid {pid} != {current_zsh_pid}")
            if current_zsh_pid is not None:
                fs.unwatch(
                    f"{zsh_folder_path}.{current_zsh_pid}", _zsh_cwd_watch_folders
                )
                fs.unwatch(f"{zsh_file_path}.{current_zsh_pid}", _zsh_cwd_watch_files)
            current_zsh_pid = pid
            # print(f"zsh.py win_title() watching /proc/{current_zsh_pid}/cwd")
            # fs.watch(f"/proc/{pid}/cwd", _zsh_cwd_watch_folders)
            folder_path = f"{zsh_folder_path}.{pid}"
            file_path = f"{zsh_file_path}.{pid}"
            if os.path.exists(folder_path):
                fs.watch(folder_path, _zsh_cwd_watch_folders)
            if os.path.exists(file_path):
                fs.watch(file_path, _zsh_cwd_watch_files)
    else:
        if current_zsh_pid is not None:
            fs.unwatch("{zsh_folder_path}.{current_zsh_pid}", _zsh_cwd_watch_folders)
            fs.unwatch("{zsh_file_path}.{current_zsh_pid}", _zsh_cwd_watch_files)
            current_zsh_pid = None


ui.register("win_focus", win_title)
ui.register("win_title", win_title)


@mod.action_class
class Actions:
    def debug_zsh_completions():
        """Dump add a pretty version of the completions to the log"""
        logging.info(pprint.pformat(ctx.lists["user.zsh_folder_completion"]))
        logging.info(pprint.pformat(ctx.lists["user.zsh_file_completion"]))
