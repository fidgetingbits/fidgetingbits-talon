import logging
import os
import pathlib
import pprint
from dataclasses import dataclass

from talon import Context, Module, actions, app, fs, settings, ui
from talon_init import TALON_HOME

ctx = Context()
mod = Module()

ctx.matches = r"""
app: zsh
"""

mod.tag("zsh", desc="Tag for enabling zsh shell support")
mod.setting(
    "zsh_auto_completion",
    type=bool,
    default=False,
    desc="Whether or not to enable autocompletion for zsh",
)

plugin_tag_list = [
    "zsh_cd_gitroot",
    "zsh_folder_completion",
    "zsh_zhooks",
]

for entry in plugin_tag_list:
    mod.tag(entry, f"tag to load {entry} zsh plugin commands")

mod.list("zsh_folder_completion", desc="ZSH folder completions")
mod.list("zsh_file_completion", desc="ZSH file completions")


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
    completion_base_folder = (
        pathlib.Path(os.environ.get("XDG_RUNTIME_DIR", "/tmp"))
        / "talon/cache/completions"
    )
    zsh_folder_path = completion_base_folder / "talon_zsh_folders"
    zsh_file_path = completion_base_folder / "talon_zsh_files"
else:
    completion_base_folder = TALON_HOME / "cache/completions/"
    # FIXME: use getconf DARWIN_USER_TMP_DIR for mac
    zsh_folder_path = completion_base_folder / "talon_zsh_folders"
    zsh_file_path = completion_base_folder / "talon_zsh_files"

current_zsh_pid = None

# FIXME: arguably this whole watching subsystem could be replaced with dynamic lists and it would be a lot cleaner
# but I don't like the idea of running actions.user.create_spoken_forms_from_list() on big lists every single time
# I say a command..


@dataclass
class WatchCallback:
    watch_file: str
    setting: str
    list_name: str
    callback: str


def _dispatch_watch_callbacks(path, flags):
    """Find the callback associated with the path and run it"""

    # The files we watch are some known name with a pid tacked on the end, so normalize it and
    # see which callback to run
    p = pathlib.Path(path)
    file = p.name.split(".")[0]
    for entry in watch_callbacks:
        if entry.watch_file == file:
            entry.callback(entry, path)
            # We don't break in case eventually there's multiple callbacks for the same file


def paths_watch_callback(cb: WatchCallback, path: str):
    """Update a list based off changes in working directory

    Each entry in the watched file is a full path, so we just want the basename. Otherwise this is the same
    as the basic watch callback

    FIXME: Probably could fix this to not use the full path in the zsh hook and then we don't need a separate function?
    """
    # print(f"_zsh_cwd_watch() Detected an update for {path}")
    try:
        with open(path, "r") as f:
            folder_list = [os.path.basename(x) for x in f.read().splitlines()]
            if len(folder_list) == 0:
                ctx.lists[cb.list_name] = {}
            else:
                ctx.lists[cb.list_name] = actions.user.create_spoken_forms_from_list(
                    folder_list
                )
                # print(f"Updating {cb.list_name} with {len(folder_list)} entries")
    except Exception:
        # If there's no folders in a directory this is expected
        # print(f"zsh.py _zsh_cwd_watch_folders() failed to read {path}: {e}")
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


watch_callbacks = []
old_callback_count = 0


def _basic_watch_callback(cb: WatchCallback, path: str):
    """Update the list based off of a change of working directory"""
    # print("_basic_watch_callback()")
    if not settings.get(cb.setting):
        return
    try:
        with open(path, "r") as f:
            commands = f.read().splitlines()
            if len(commands) == 0:
                ctx.lists[cb.list_name] = {}
            else:
                ctx.lists[cb.list_name] = actions.user.create_spoken_forms_from_list(
                    commands
                )
            # print(
            #     f"Updated {cb.list_name} with {len(commands)} entries: {ctx.lists[cb.list_name]}"
            # )
    except Exception:
        pass


def _register_callback(
    watch_file: str, setting_name: str, list_name: str, callback: str
):
    """Register a callback for a watch file

    @param watch_file: The file to watch
    @param list_name: The talon list to update
    @param callback: The callback to run on file update. Is passed the list name
    """
    global watch_callbacks
    new = WatchCallback(watch_file, setting_name, list_name, callback)
    if list_name not in ctx.lists:
        ctx.lists[list_name] = {}
    # print(f"registered {list_name}: {ctx.lists[list_name]}")

    for entry in watch_callbacks:
        if entry.watch_file == new.watch_file:
            entry.callback = callback
            return
    watch_callbacks.append(new)
    # print(f"new {new.watch_file} callback registered")


def _setup_watches(window):
    # Checking here lets us enable it after the fact
    if not settings.get("user.zsh_auto_completion"):
        return
    global zsh_folder_path
    global completion_base_folder
    if window == ui.active_window() and _is_zsh_window(window):
        pid = _get_zsh_pid(window.title)
        # print(f"zsh.py _setup_watches() detected zsh pid {pid}")
        global current_zsh_pid
        if pid != current_zsh_pid:
            # print(
            #     f"zsh.py _setup_watches() detected zsh pid {pid} != {current_zsh_pid}"
            # )
            if current_zsh_pid is not None:
                for entry in watch_callbacks:
                    watch_file = (
                        completion_base_folder / f"{entry.watch_file}.{current_zsh_pid}"
                    )
                    fs.unwatch(
                        watch_file,
                        entry.callback,
                    )
                    # print(f"unwatching {watch_file}")

            current_zsh_pid = pid

            # print(f"Setting watch for {len(watch_callbacks)} watch callbacks")
            global old_callback_count
            old_callback_count = len(watch_callbacks)
            for entry in watch_callbacks:
                watch_path = completion_base_folder / f"{entry.watch_file}.{pid}"
                # print(f"calling callback for {watch_path}")
                entry.callback(entry, watch_path)
                # print(f"Setting watch on {watch_path}")
                fs.watch(watch_path, _dispatch_watch_callbacks)
        elif len(watch_callbacks) != old_callback_count:
            # Sometimes the callbacks get added after the first pid detection
            for entry in watch_callbacks:
                # print(f"unwatching {entry['watch_file']}")
                fs.unwatch(
                    completion_base_folder / f"{entry.watch_file}.{current_zsh_pid}",
                    _dispatch_watch_callbacks,
                )
            for entry in watch_callbacks:
                watch_path = completion_base_folder / f"{entry.watch_file}.{pid}"
                # print(f"calling callback for {watch_path}")
                entry.callback(entry, watch_path)
                # print(f"Setting watch on {watch_path}")
                fs.watch(watch_path, _dispatch_watch_callbacks)
            # print(
            #     f"zsh.py _setup_watches() detected zsh pid {pid} == {current_zsh_pid}"
            # )
            pass
    else:
        if current_zsh_pid is not None:
            for entry in watch_callbacks:
                fs.unwatch(
                    completion_base_folder / f"{entry.watch_file}.{current_zsh_pid}",
                    _dispatch_watch_callbacks,
                )
            current_zsh_pid = None


def win_focus(window):
    _setup_watches(window)


def win_title(window):
    _setup_watches(window)


def on_ready():
    ui.register("win_focus", win_title)
    ui.register("win_title", win_title)


app.register("ready", on_ready)

_register_callback(
    "talon_zsh_folders",
    "user.zsh_auto_completion",
    "user.zsh_folder_completion",
    paths_watch_callback,
)
_register_callback(
    "talon_zsh_files",
    "user.zsh_auto_completion",
    "user.zsh_file_completion",
    paths_watch_callback,
)


@mod.action_class
class Actions:
    def zsh_dump_file_completions():
        """Dump add a pretty version of the file completions to the log"""
        logging.info(
            f'ZSH File Completions (Enabled {settings.get("user.zsh_auto_completion")}):'
        )
        logging.info(pprint.pformat(ctx.lists["user.zsh_file_completion"]))

    def zsh_dump_folder_completions():
        """Dump add a pretty version of the folder completions to the log"""
        logging.info(
            f'ZSH Folder Completions (Enabled {settings.get("user.zsh_auto_completion")}):'
        )
        logging.info(pprint.pformat(ctx.lists["user.zsh_folder_completion"]))

    def zsh_dump_completions():
        """Dump add a pretty version of the completions to the log"""
        actions.user.zsh_dump_folder_completions()
        actions.user.zsh_dump_file_completions()
        for entry in watch_callbacks:
            logging.info(f"{entry.watch_file} completions:")
            logging.info(pprint.pformat(ctx.lists[entry.list_name]))

    def zsh_get_pid():
        """Return the current zsh pid"""
        return current_zsh_pid

    def zsh_register_watch_file_callback_basic(
        watch_file: str, setting_name: str, list_name: str
    ):
        """Register a default callback for a watch file

        @param watch_file: The file to watch
        @param setting_name: The setting to check if the callback should run
        @param list_name: The talon list to update
        """
        _register_callback(watch_file, setting_name, list_name, _basic_watch_callback)

    def zsh_register_watch_file_callback_custom(
        watch_file: str, setting_name: str, list_name: str, callback: str
    ):
        """Register a custom callback for a watch file

        @param watch_file: The file to watch
        @param setting_name: The setting to check if the callback should run
        @param list_name: The talon list to update
        @param callback: The callback to run on file update, is passed a FileWatchCallback object
        """
        _register_callback(watch_file, setting_name, list_name, callback)

    def zsh_completion_base_dir():
        """Return the base directory for zsh completions"""
        return completion_base_folder

    def update_completion_list(
        completion_list: dict,
        path: str,
    ):
        """Update the completion list based off of a change of working directory"""
        try:
            with open(f"{ actions.user.zsh_completion_base_dir()}/{path}", "r") as f:
                commands = f.read().splitlines()
                completion_list.clear()
                if len(commands) != 0:
                    completion_list.update(
                        actions.user.create_spoken_forms_from_list(commands)
                    )
        except Exception:
            pass
