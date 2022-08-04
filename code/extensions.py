from .user_settings import get_list_from_csv
from talon import Module, Context

mod = Module()
mod.list("file_extension", desc="A file extension, such as .py")

_file_extensions_defaults = {
    "bee tea": ".bt",
    "build": ".build",
    "back": ".bak",
    "backup": ".bkp",
    "bat": ".bat",
    "batch": ".bat",
    "bin": ".bin",
    "bend": ".bin",
    "bit map": ".bmp",
    "bump": ".bmp",
    "B Z two": ".bz2",
    "B zip": ".bz2",
    "C G I": ".cgi",
    "C F G": ".cfg",
    "conf": ".conf",
    "config": ".config",
    "com": ".com",
    "comma": ".csv",
    "C S V": ".csv",
    "data": ".data",
    "database": ".db",
    "deb": ".deb",
    "debug": ".debug",
    "desktop": ".desktop",
    "dock ex": ".docx",
    "dock": ".doc",
    "draw eye oh": ".drawio",
    "E M L": ".eml",
    "exe": ".exe",
    "flack": ".flac",
    "G bag": ".gdb",
    "G D B": ".gdb",
    "git": ".git",
    "G Z": ".gz",
    "G zip": ".gz",
    # NOTE - H conflicted with way too much
    "header": ".h",
    "hex": ".hex",
    "H T M L": "html",
    "hypertext": "html",
    "ida": ".idb",
    "jar": ".jar",
    "java": ".java",
    "J S": ".js",
    "javascript": ".js",
    "jason five": ".json5",
    "jason": ".json",
    "J peg": ".jpg",
    "key": ".key",
    "K O": ".ko",
    "kay oh": ".ko",
    "local": ".local",
    "log": ".log",
    "lua": ".lua",
    "M D": ".md",
    "mark down": ".md",
    "net": ".net",
    "nse": ".nse",
    "org": ".org",
    "out": ".out",
    "patch": ".patch",
    "P D F": ".pdf",
    "peep": ".php",  # because P H P doesn't seem to work
    "pam": ".pem",
    "P H P": "Files.php",
    "P L": ".pl",
    "pearl": ".pl",
    "pickle": ".pkl",
    "pie": ".py",
    "pie four": ".py4",
    "ping": ".png",
    "power shell": ".ps1",
    "queue el": ".ql",
    # "R S": ".rs",
    "rust": ".rs",
    "C S": ".cs",
    "see sharp": ".cs",
    "see": ".c",
    "rules": ".rules",
    "service": ".service",
    "session": ".session",
    "S H": ".sh",
    "shell": ".sh",
    "snippets": ".snippets",
    "S O": ".so",
    "so": ".so",
    "socket": ".socket",
    "S T P": ".stp",
    "talon": ".talon",
    "tar": ".tar",
    "tar G Z": ".tar.gz",
    "tar G zip": ".tar.gz",
    "tar B Z": ".tar.bz2",
    "tar B zip": ".tar.bz2",
    "tar X Z": ".tar.xz",
    "task": ".task",
    "text": ".txt",
    "timer": ".timer",
    "N map": ".nse",
    "N S E": ".nse",
    "neo vim": ".nvim",
    "N vim": ".nvim",
    "web P": ".webp",
    "vim": ".vim",
    "X Z": ".xz",
    "X M L": ".xml",
    "yaml": ".yml",
    "z shell": ".zsh",
    "zip": ".zip",
    # tlds
    "com": ".com",
    "net": ".net",
    "org": ".org",
    "us": ".us",
    "U S": ".us",
    "C A": ".ca",
    "C X": ".cx",
    "T W": ".tw",
}

file_extensions = get_list_from_csv(
    "file_extensions.csv",
    headers=("File extension", "Name"),
    default=_file_extensions_defaults,
)

ctx = Context()
ctx.lists["user.file_extension"] = file_extensions
