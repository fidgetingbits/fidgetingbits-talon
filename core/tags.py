from talon import Module

mod = Module()

tagList = [
    "disassembler",
    "gdb",
    "libptmalloc",
    "libdlmalloc",
    "libheap",
    "libslub",
    "gdb_vmlinux",
    "git",  # commandline tag for git commands
    "ida",
    "tabs",
    "generic_windows_shell",
    "generic_unix_shell",
    "readline",
    "taskwarrior",  # commandline tag for taskwarrior commands
    "tmux",
    "windbg",
    "yay",
    "meson",
    "ninja",
    "apt",
    "buku",
    "ghidra_server",
    "nmcli",
    "nftables",
    "taskwarrior",
    "timewarrior",
    "make_commands",
    "kubectl",
    "tmux",
    "docker",
    "vagrant",
    "git",
    "pulse_audio",
    "virsh",
    "iptables",
    "docker",
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
    "vboxmanage",
    "glab",
    "coredumpctl",
    "rust_apps",
]

for entry in tagList:
    mod.tag(entry, f"tag to load {entry} and/or related plugins ")
