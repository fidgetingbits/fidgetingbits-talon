# XXX - this should have os awarenss
import pathlib
from talon import Context, Module, actions


mod = Module()
mod.list("paths_public", desc="Common paths")
mod.list("paths_private", desc="Common private paths")
mod.list("folder_paths_public", desc="Common paths")
mod.list("folder_paths_private", desc="Common private paths")
ctx = Context()

TALON_REPO="fidget"
arch_linux_paths = { "packman hooks": "/etc/pacman.d/hooks/",}
# paths that will work with pivot command
linux_folder_paths = {
    "user services": "~/.config/systemd/user/",
    "services": "/etc/systemd/system/",
    "vim sessions": "~/.vim/sessions/",
    "vim plugins": "~/.vim/plugged/",
    "temp": "/tmp/",
    "config": "/etc/",
    "it see": "/etc/",
    "user": "/usr/",
    "user bin": "/usr/bin/",
    "user lib": "/usr/lib/",
    "user src": "/usr/src/",
    "user local": "/usr/local/",
    "user local bin": "/usr/local/bin/",
    "user local lib": "/usr/local/lib/",
    "user local config": "/usr/local/etc/",
    "log": "/var/log/",
    "shell config": "~/.ohmyzsh/",
    "shell functions": "~/.ohmyzsh/custom/functions/",
    "dot files": "~/dotfiles/",
    "custom snippets": "~/.vim/custom-snippets/",
    "vim snippets": "~/.vim/plugged/vim-snippets/UltiSnips/",
    "talon": f"~/.talon/user/{TALON_REPO}/",
    "back": "../",
}

linux_file_paths = {
    "password": "/etc/passwd",
    "shadow": "/etc/shadow",
    "hosts": "/etc/hosts",
    "resolve": "/etc/resolv.conf",
    "null": "/dev/null",
    "zero": "/dev/zero",
    "vim": "~/.vim/",
    "grub config": "/etc/default/grub",
    "crypt tab": "/etc/crypttab",
    "f stab": "/etc/fstab",
    "make init config": "/etc/mkinitcpio.conf",
    "boot config": "/boot/grub/grub.cfg",
    "journal config": "/etc/systemd/journald.conf", 
    "tunnel config": "~/.ssh/config", 
    "shell config": "~/.zshrc", 
    "poly bar": "~/.config/polybar/config", 
    "eye three": "~/.i3/config", 
    "config": "~/.vimrc", 
}

# this is used for specific commands like pivot
ctx.lists["user.folder_paths_public"] = {
    **linux_folder_paths,
}
ctx.lists["user.folder_paths_private"] = {}

# this is used for any path based commands that don't care of about files or
# folder difference
ctx.lists["user.paths_public"] = {
    **linux_folder_paths,
    **linux_file_paths
}

# Arch Linux

ctx.lists["user.paths_private"] = {}

# XXX - add support for selecting
windows_paths = {
    "desktop": "%USERPROFILE%\\Desktop",
    "profile": "%USERPROFILE%",
    "root": "%SYSTEMROOT%",
    "windows": "%SYSTEMROOT%",
    "system": "%SYSTEMROOT%\\System32",
    "drivers": "%SYSTEMROOT%\\System32\\Drivers",
    "programs": "%PROGRAMFILES%",
}

@mod.capture(rule="{user.folder_paths_public}")
def folder_paths_public(m)-> str:
    "One path representing a public folder"
    return m.folder_paths_public

@mod.capture(rule="{user.folder_paths_private}")
def folder_paths_private(m)-> str:
    "One path representing a public folder"
    return m.folder_paths_private


@mod.capture(rule="{user.paths_public}")
def paths_public(m)-> str:
    "One public path representing a file or folder"
    return m.paths_public


@mod.capture(rule="{user.paths_private}")
def paths_private(m)-> str:
    "One private path representing a file or folder"
    return m.paths_private

@mod.capture(rule="<user.folder_paths_public>|<user.folder_paths_private>")
def folder_paths(m)-> str:
    "One public or private path that represents a folder"
    return m

@mod.capture(rule="<user.paths_public>|<user.paths_private>")
def paths(m)-> str:
    "One public or private path that represents a file or folder"
    return m

@mod.action_class
class Actions:
    def path_traverse(num:int) -> str:
        """creates a string num path traversal sequences"""
        return "../"*num

    # XXX - this should be an overridable type of method so that we can
    # have language specific escaping, for multiple types of scenarios
    def escape_path(path:str):
        """Escape separators in a path string"""
        return path.replace("/", "\\/")
