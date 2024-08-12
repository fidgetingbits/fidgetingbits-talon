import logging
import pathlib
import pprint
import subprocess

from talon import Context, Module, actions, settings, ui

ctx = Context()
mod = Module()

ctx.matches = r"""
tag: user.zsh
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
mod.list("zsh_symlink_completion", desc="ZSH symlink completions")


# FIXME: make this is setting
FILE_LIMIT = 100

# Folders that we know for certain are too big and that will break the find command, even when using -maxdepth 1
# FIXME: add private lists
blacklist = [
    "/nix/store",
]


def _find_items_in_current_path(type: str) -> dict[str, str]:
    # grab any items of requested type
    # NOTE: Don't use -printf below because it doesn't work on Darwin
    cwd = actions.user.get_cwd()
    if str(cwd) in blacklist:
        print(f"Skipping find in blacklisted folder: {actions.user.get_cwd()}")
        return {}

    ps = subprocess.Popen(
        [
            f"bash -c \"find $PWD -maxdepth 1 -type {type} -not -path '*/\\.*' -not -path '\\.' -exec basename {{}} \\; -exec echo \\; \""
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        shell=True,
    )
    cmd_error = ps.stderr.read()
    if len(cmd_error) > 0:
        print(f"Error running find command: {cmd_error}")
        return {}
    results = subprocess.check_output(
        [f"head -n {FILE_LIMIT}"], stdin=ps.stdout, shell=True
    ).decode("utf-8")
    ps.wait()
    if not results:
        print("no found items")
        return {}

    # grab any symlinks
    ps = subprocess.Popen(
        ["find $PWD -maxdepth 1 -type l -not -path '*/\\.*' -not -path '\\.' -print"],
        stdout=subprocess.PIPE,
        cwd=cwd,
        shell=True,
    )
    symlink_list = subprocess.check_output(
        [f"head -n {FILE_LIMIT}"], stdin=ps.stdout, shell=True
    ).decode("utf-8")
    ps.wait()

    items = []
    for line in results.splitlines():
        if line == "." or line == "..":
            continue
        items.append(line.strip())
    for line in symlink_list.splitlines():
        link_path = pathlib.Path(line).resolve()
        if link_path.exists():
            if type == "d" and link_path.is_dir():
                items.append(pathlib.Path(line).name)
            elif type == "f" and link_path.is_file():
                items.append(pathlib.Path(line).name)
            elif type == "l" and link_path.is_symlink():
                items.append(pathlib.Path(line).name)

    return actions.user.create_spoken_forms_from_list(items)


@ctx.dynamic_list("user.zsh_folder_completion")
def user_zsh_folder_completion(m) -> dict[str, str]:
    """A dynamic list of folders in the current folder"""
    return _find_items_in_current_path("d")


@ctx.dynamic_list("user.zsh_file_completion")
def user_zsh_file_completion(m) -> dict[str, str]:
    """A dynamic list of files in the current folder"""
    return _find_items_in_current_path("f")


@ctx.dynamic_list("user.zsh_symlink_completion")
def user_zsh_symlink_completion(m) -> dict[str, str]:
    """A dynamic list of symlinks in the current folder"""
    return _find_items_in_current_path("l")


@mod.capture(rule="{user.zsh_folder_completion}")
def zsh_folder_completion(m) -> str:
    """Returns a speakable folder name"""
    return m


@mod.capture(rule="{user.zsh_folder_completion}")
def zsh_folder_completions(m) -> str:
    """Returns one or more folder names"""
    return " ".join(m.zsh_folder_completion_list)


@mod.capture(rule="{user.zsh_file_completion}")
def zsh_file_completion(m) -> str:
    """Returns a speakable file name"""
    return m


@mod.capture(rule="{user.zsh_file_completion} [and {user.zsh_file_completion}]")
def zsh_file_completions(m) -> str:
    """Returns one or more file names"""
    return " ".join(m.zsh_file_completion_list)


@mod.capture(rule="{user.zsh_symlink_completion}")
def zsh_symlink_completion(m) -> str:
    """Returns a speakable symlink name"""
    return m


@mod.capture(rule="{user.zsh_symlink_completion} [and {user.zsh_symlink_completion}]")
def zsh_symlink_completions(m) -> str:
    """Returns one or more symlink names"""
    return " ".join(m.zsh_symlink_completion_list)


# FIXME: Decide if I want symlinks included in this
@mod.capture(rule="({user.zsh_folder_completion} | {user.zsh_file_completion})")
def zsh_path_completion(m) -> str:
    """Returns a speakable file name"""
    return m


@mod.capture(rule="<user.zsh_path_completion> [and <user.zsh_path_completion>]")
def zsh_path_completions(m) -> str:
    """Returns a speakable file name"""
    return " ".join(m.zsh_path_completion_list)


def _is_zsh_window(window):
    return (
        window.title.startswith("VIM ")
        and "TERM:" in window.title
        and " zsh" in window.title
    )


def _zsh_get_pid(title):
    """Extract the zsh pid from the window title"""
    try:
        pid = int(title.split("term://")[1].split(":")[0].split("/")[-1])
        return pid
    except Exception as e:
        # FIXME:
        # print(f"zsh.py _zsh_get_pid() failed to extract pid from {title}: {e}")
        pass


def _zsh_get_cwd(title, noisy=False) -> pathlib.Path:
    """Extract the zsh cwd from the window title"""
    if not title.startswith("VIM"):
        return
    try:
        # Title: VIM MODE:t RPC:/run/user/1000/nvim.2299162.0 FILETYPE: TERM:zsh:~/dev/nix/nix-config
        # (term://~//2299179:/usr/bin/zsh) zsh
        # isolate :zsh...
        cwd = title.split("TERM")[1].split(":")[2]
        # remove the trailing part after the path
        cwd = cwd.split("(term")[0]
        # resolve any ~
        cwd = pathlib.Path(cwd.strip()).expanduser()
        if cwd.exists():
            return cwd
        else:
            if noisy:
                print(f"zsh.py _get_zsh_cwd() extracted cwd does not exist: {cwd}")
    except Exception as e:
        if noisy:
            print(f"zsh.py _get_zsh_cwd() failed to extract cwd from {title}: {e}")


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

    def zsh_get_pid():
        """Return the current zsh pid"""
        return _zsh_get_pid(ui.active_window().title)

    def zsh_get_cwd(noisy: bool = False):
        """Return the current zsh cwd"""
        return _zsh_get_cwd(ui.active_window().title, noisy)


@ctx.action_class("user")
class UserActions:
    def get_pinned_tag_id() -> tuple[int, str]:
        return (actions.user.zsh_get_pid(), "pid")

    def get_cwd() -> str:
        return actions.user.zsh_get_cwd()
