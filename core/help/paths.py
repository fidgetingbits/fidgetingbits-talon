from talon import Context, Module, app

mod = Module()
mod.list("common_files", desc="Common file names")
mod.list("paths_public", desc="Common public paths")
mod.list("paths_private", desc="Common private paths")
mod.list("folder_paths", desc="Common folders")
mod.list("folder_paths_public", desc="Common public folders")
mod.list("folder_paths_private", desc="Common private folders")
mod.list("file_paths_public", desc="Common public files")
mod.list("file_paths_private", desc="Common private files")
mod.list("file_paths", desc="Common files")
ctx = Context()

TALON_REPO = "fidgetingbits-talon"

neovim_folder_paths = {
    "vim sessions": "~/.config/nvim/sessions/",
}
neovim_file_paths = {
    "R plugins": "~/.config/nvim/rplugins.vim",
}
nix_folder_paths = {
    # nix
    "nix profile": "~/.nix-profile/",
    "nix store": "/nix/store/",
    "nix running": "/run/current-system/sw/",
    "nix profile bin": "~/.nix-profile/bin/",
    "nix running bin": "/run/current-system/sw/bin/",
    "nix global bin": "/nix/var/nix/profiles/default/bin",
}

# paths that will work with pivot command
unix_folder_paths = {
    # common
    "var F S": "/var/fs/",
    "opt": "/opt/",
    # ida
    "ida config": "~/.idapro/",
    "ida plugins": "~/.idapro/plugins/",
    "ida themes": "~/.idapro/themes/",
    "ida loaders": "~/.idapro/loaders/",
    # systemd
    "user services": "~/.config/systemd/user/",
    "user timers": "~/.config/systemd/user/",
    "services": "/etc/systemd/system/",
    # admin
    "you dev rules": "/etc/udev/rules.d/",
    "sue doers": "/etc/sudoers.d/",
    # neovim
    "vim sessions": "~/.config/nvim/sessions/",
    "neovim": "~/.config/nvim/",
    "vim": "~/.config/nvim/",
    "neovim lua": "~/.config/nvim/lua/",
    "N vim": "~/.config/nvim/",
    "N vim config": "~/.config/nvim/lua",
    "vim config": "~/.config/nvim/lua",
    "N vim lua": "~/.config/nvim/lua/",
    "neovim plugin": "~/.local/share/nvim/lazy/",
    "vim plugin": "~/.local/share/nvim/lazy/",
    # Unsorted
    "temp": "/tmp/",
    "config": "/etc/",
    "it see": "/etc/",
    "init D": "/etc/init.d/",
    "bin": "/bin/",
    "S bin": "/sbin/",
    "var run": "/var/run/",
    "var log": "/var/log/",
    "user": "/usr/",
    "user bin": "/usr/bin/",
    "user S bin": "/usr/sbin/",
    "user lib": "/usr/lib/",
    "user lib debug": "/usr/lib/debug/",
    "user src": "/usr/src/",
    "user src debug": "/usr/src/debug/",
    "user share": "/usr/share/",
    "user local": "/usr/local/",
    "user local bin": "/usr/local/bin/",
    "user local S bin": "/usr/local/sbin/",
    "user local lib": "/usr/local/lib/",
    "user local config": "/usr/local/etc/",
    "user local share": "/usr/local/share/",
    "lib": "/lib/",
    "dev": "/dev/",
    "log": "/var/log/",
    "kernel trace": "/sys/kernel/tracing/",
    "K mem events": "/sys/kernel/tracing/events/kmem",
    "custom snippets": "~/.config/nvim/snippets/",
    "vim snippets": "~/.local/share/nvim/lazy/friendly-snippets/snippets/",
    "public snippets": "~/.local/share/nvim/lazy/friendly-snippets/snippets/",
    "talon": f"~/.talon/user/{TALON_REPO}/",
    "talon user": "~/.talon/user/",
    "back": "../",
    "tunnel": "~/.ssh/",
    "tunnel config": "~/.ssh/config.d/",
    "S S H": "~/.ssh/",
    "S S H config": "~/.ssh/config.d/",
    "raffi": "~/.config/rofi/",
    "screen layout": "~/.screenlayout/",
    "network manager": "/etc/NetworkManager/",
    "network manager dispatcher": "/etc/NetworkManager/dispatcher.d/",
    "network manager config": "/etc/NetworkManager/conf.d/",
    "systemd network": "/etc/systemd/network/",
    # ubuntu-esque stuff
    "lib linux": "/lib/x86_64-linux-gnu/",
    "lib sixty four": "/lib64/",
    "lib thirty two": "/lib32/",
    "lib three two": "/lib32/",
    "proc": "/proc/",
    "proc pid": "/proc/<pid>/",
    "proc pid limits": "/proc/<pid>/limits",
    "proc pid status": "/proc/<pid>/status",
    "proc pid maps": "/proc/<pid>/maps",
    "proc pid mem": "/proc/<pid>/mem",
    "proc pid self": "/proc/<pid>/self",
    "proc pid X E": "/proc/<pid>/exe",
    "proc pid C W D": "/proc/<pid>/cwd",
    "proc pid F D": "/proc/<pid>/fd/",
    "root": "/root/",
    "boot": "/boot/",
    "packman cache": "/var/cache/pacman/pkg/",
    "yay cache": "~/.cache/yay/",
    "open snitch rules": "/etc/opensnitchd/rules/",
    "local apps": "~/.local/share/applications/",
    "desktop files": "~/.local/share/applications/",
    "Polly bar": "~/.config/polybar/",
    "eye three": "~/.i3/",
    "kitty": "~/.config/kitty/",
    "python sight packages": "/usr/lib/python3.10/site-packages",
    "dot config": "~/.config/",
    "apache": "/etc/apache2/",
    "apache sites": "/etc/apache2/sites-available/",
    "apache sites enabled": "/etc/apache2/sites-enabled/",
    "apache mods": "/etc/apache2/mods-available/",
    "apache mods enabled": "/etc/apache2/mods-enabled/",
    "var web": "/var/www/",
    "code extensions": "~/.vscode/extensions/",
    "talon completions": "$XDG_RUNTIME_DIR/talon/cache/completions/",
}

mac_folder_paths = {}
linux_folder_paths = {}
arch_linux_folder_paths = {
    "packman hooks": "/etc/pacman.d/hooks/",
}
windows_folder_paths = {}

unix_file_paths = {
    "O S release": "/etc/os-release",
    "system version": "/etc/os-release",
    "muscle lib": "/lib/ld-musl-x86_64.so.1",
    "apache conf": "/etc/apache2/apache2.conf",
    "G D B init": "~/.gdbinit",
    "known hosts": "~/.ssh/known_hosts",
    "password": "/etc/passwd",
    "groups": "/etc/group",
    "shadow": "/etc/shadow",
    "hosts": "/etc/hosts",
    "resolve": "/etc/resolv.conf",
    "null": "/dev/null",
    "dev null": "/dev/null",
    "zero": "/dev/zero",
    "grub config": "/etc/default/grub",
    "crypt tab": "/etc/crypttab",
    "f stab": "/etc/fstab",
    "make init config": "/etc/mkinitcpio.conf",
    "boot config": "/boot/grub/grub.cfg",
    "journal config": "/etc/systemd/journald.conf",
    "lib virt config": "/etc/libvirt/libvirtd.conf",
    "tunnel config": "~/.ssh/config",
    "shell config": "~/.config/zsh/.zshrc",
    "zish config": "~/.config/zsh/.zshrc",
    "zish R C": "~/.config/zsh/.zshrc",
    "bash config": "~/.bashrc",
    "bash R C": "~/.bashrc",
    "git config": ".git/config",
    "poly bar config": "~/.config/polybar/config",
    "eye three config": "~/.i3/config",
    "c snippets": "~/.vim/plugged/vim-snippets/UltiSnips/c.snippets",
    "mark down snippets": "~/.vim/plugged/vim-snippets/UltiSnips/markdown.snippets",
    "python snippets": "~/.vim/plugged/vim-snippets/UltiSnips/python.snippets",
    "bash snippets": "~/.vim/plugged/vim-snippets/UltiSnips/bash.snippets",
    "kitty config": "~/.config/kitty/kitty.conf",
    "grub defaults": "/etc/default/grub",
    "raffi config": "~/.config/rofi/rofi.rasi",
    "raffi theme": "~/.config/rofi/colors.rasi",
    "lisp log": "~/.cache/nvim/lsp.log",
    "slab info": "/proc/slabinfo",
    "kernel active trace": "/sys/kernel/tracing/trace",
    "kernel current tracer": "/sys/kernel/tracing/current_tracer",
    "kernel available tracersm": "/sys/kernel/tracing/available_tracers",
    "Q emu config": "/etc/libvirt/qemu.conf",
    "proxy chains": "~/.proxychains/proxychains.conf",
    "open snitch log": "/var/log/opensnitchd.log",
    "howdy config": "/usr/lib/security/howdy/config.ini",
    "et see keeper": "/etc/etckeeper/etckeeper.conf",
    "var log messages": "/var/log/messages",
    "K all sims": "/proc/kallsyms",
    "serial usb": "/dev/ttyUSB0",
    "dev T T Y U S B": "/dev/ttyUSB0",
    "dev T T Y A C M": "/dev/ttyACM0",
    "dev T T Y S zero": "/dev/ttyS0",
    "bin bash": "/bin/bash",
    "bin S H": "/bin/sh",
    "bin Z S H": "/bin/zsh",
    "bin ash": "/bin/ash",
    "user bin env": "/usr/bin/env",
    "P trace scope": "/proc/sys/kernel/yama/ptrace_scope",
    "kernel config": "/proc/config.gz",
    "A W S credentials": "~/.aws/credentials",
    "cargo config": "~/.cargo/config",
    "authorized keys": "~/.ssh/authorized_keys",
    "S S H D config": "/etc/ssh/sshd_config",
    "talon log": "~/.talon/talon.log/",
    "S S M T P config": "/etc/ssmtp/ssmtp.conf",
}

mac_file_paths = {}
linux_file_paths = {}
arch_linux_file_paths = {}
windows_file_paths = {}


# XXX - add support for selecting
windows_paths = {
    "desktop": "%USERPROFILE%\\Desktop\\",
    "profile": "%USERPROFILE%\\",
    "root": "%SYSTEMROOT%\\",
    "windows": "%SYSTEMROOT%\\",
    "system": "%SYSTEMROOT%\\System32\\",
    "drivers": "%SYSTEMROOT%\\System32\\Drivers\\",
    "programs": "%PROGRAMFILES%\\",
}

if app.platform == "mac":
    folder_paths = {**unix_folder_paths, **nix_folder_paths, **mac_folder_paths, **neovim_folder_paths}
    file_paths = {**unix_file_paths, **mac_file_paths, **neovim_file_paths}
elif app.platform == "windows":
    # FIXME: This should probably have something like wsl awareness
    folder_paths = {**windows_paths}
elif app.platform == "linux":
    folder_paths = {**unix_folder_paths, **nix_folder_paths, **linux_folder_paths, **arch_linux_folder_paths, **neovim_folder_paths}
    file_paths = {**unix_file_paths, **linux_file_paths, **arch_linux_file_paths, **neovim_file_paths}
else:
    folder_paths = {**unix_folder_paths, **nix_folder_paths}
    file_paths = {**unix_file_paths}

all_paths = {**folder_paths, **file_paths}


# this is used for specific commands like pivot
ctx.lists["user.folder_paths_public"] = folder_paths
ctx.lists["user.file_paths_public"] = file_paths

# this is used for any path based commands that don't care of about files or
# folder difference
ctx.lists["user.paths_public"] = all_paths

ctx.lists["user.paths_private"] = {}
ctx.lists["user.folder_paths_private"] = {}
ctx.lists["user.file_paths_private"] = {}


ctx.lists["user.common_files"] = {
    "read me": "README.md",
    "trouble": "TROUBLESHOOTING.md",
    "to do": "TODO.md",
    "license": "LICENSE.md",
    "package build": "PKGBUILD",
    "make": "Makefile",
    "make file": "Makefile",
    "just": "justfile",
    "just file": "justfile",
    "git ignore": ".gitignore",
    "env R C": ".envrc",
    "env": ".env",
    "pre commit config": ".pre-commit-config.yaml",
    "flake": "flake.nix",
    "flake lock": "flake.lock",
    "docker": "Dockerfile",
    "docker file": "Dockerfile",
    "docker compose": "docker-compose.yml",
    "package json": "package.json",
    "yarn lock": "yarn.lock",
}


@mod.capture(rule="{user.folder_paths_public}")
def folder_paths_public(m) -> str:
    "One path representing a public folder"
    return m.folder_paths_public


@mod.capture(rule="{user.folder_paths_private}")
def folder_paths_private(m) -> str:
    "One path representing a public folder"
    return m.folder_paths_private


@mod.capture(rule="{user.paths_public}")
def paths_public(m) -> str:
    "One public path representing a file or folder"
    return m.paths_public


@mod.capture(rule="{user.paths_private}")
def paths_private(m) -> str:
    "One private path representing a file or folder"
    return m.paths_private


@mod.capture(rule="<user.folder_paths_public>|<user.folder_paths_private>")
def folder_paths(m) -> str:
    "One public or private path that represents a folder"
    return m


@mod.capture(rule="{user.file_paths_public}|{user.file_paths_private}")
def file_paths(m) -> str:
    "One public or private path that represents a file"
    return m


@mod.capture(rule="{user.file_paths_private}|{user.file_paths_public}")
def file_paths_string(m) -> str:
    "One public or private path that represents a file"
    return str(m)


@mod.capture(rule="{user.paths_public}|{user.paths_private}")
def folder_paths_string(m) -> str:
    "One public or private path that represents a file or folder"
    return str(m)


@mod.capture(rule="<user.paths_public>|<user.paths_private>")
def paths(m) -> str:
    "One public or private path that represents a file or folder"
    return m


@mod.action_class
class Actions:
    def path_traverse(num: int) -> str:
        """creates a string num path traversal sequences"""
        return "../" * num

    # XXX - this should be an overridable type of method so that we can
    # have language specific escaping, for multiple types of scenarios
    def escape_path(path: str):
        """Escape separators in a path string"""
        return path.replace("/", "\\/")
