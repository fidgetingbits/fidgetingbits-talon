from talon import Module

mod = Module()

tagList = [
    "disassembler",  # generic disassember commands
    "gdb",  # linux debugger
    "libptmalloc",  # gdb plugin for ptmalloc
    "libdlmalloc",  # gdb plugin for dlmalloc
    "libheap",  # gdb plugin for ptmalloc
    "libslub",  # gdb plugin for linux kernel slub allocator
    "gdb_vmlinux",  # tag for gdb commands that help with linux kernel debugging
    "git",  # commandline tag for git commands
    "ida",  # ida decompiler commands
    "tabs",
    "generic_windows_shell",
    "generic_unix_shell",
    "readline",
    "taskwarrior",  # commandline tag for taskwarrior commands
    "tmux",
    "windbg",
    "yay",  # arch linux package manager
    "meson",  # meson build system
    "ninja",
    "apt",  # debian/ubuntu package manager
    "buku",  # terminal bookmark manager
    "ghidra_server",  # ghidra decompiler server commands
    "nmcli",  # Linux network manager command line interface
    "nftables",  # Linux firewall command line interface
    "taskwarrior",
    "timewarrior",
    "make_commands",
    "just_commands",
    "kubectl",
    "tmux",
    "docker",
    "vagrant",
    "git",
    "pulse_audio",
    "virsh",
    "iptables",
    "podman",
    # allows programs running inside of a terminal (ex: gdb) to share
    # common terminal commands like ctrl+c, but without actually
    # supporting all of this shell commands themselves (ls, cd, etc)
    "terminal_program",
    # a tag for defining very specific terminal command line editor
    # commands, see command_line_editing_readline.talon
    "readline",
    "shell_edit_emacs",
    "htop",
    "taskwarrior_tui",
    "vimium",
    "obs_studio_global",
    "vboxmanage",  # virtualbox cli
    "glab",  # gitlab cli
    "coredumpctl",  # systemd core dump manager
    "rust_apps",  # rust terminal commands (rustup, cargo, etc)
    "gpg",  # gpg terminal commands
    "nix_cli",  # nix terminal commands
    "poetry",  # python package management commands
    "aws_cli",  # amazon aws cli commands
    "s3fs",  # amazon aws s3 bucket mounting
    "direnv",  # direnv commands
    "ykman",  # yubikey manager commands
    "btrfs",  # btrfs filesystem commands
    "qcow2",  # qemu qcow2 image commands
    "borg",  # borg backup commands
    "atuin",  # atuin terminal commands
]

for entry in tagList:
    mod.tag(entry, f"tag to load {entry} and/or related plugins ")
