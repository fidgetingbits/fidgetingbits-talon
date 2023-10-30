from talon import Context, Module

from ..user_settings import get_list_from_csv

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")


abbreviations_list = {
    "A sink": "async",
    "B P F trace": "bpftrace",
    "B P F": "ebpf",
    "J peg": "jpg",
    "K mem": "kmem",
    "P R cuttle": "prctl",
    "P T malloc": "ptmalloc",
    "V M linux": "vmlinux",
    "abbreviate": "abbr",
    "abort": "abrt",
    "acknowledge": "ack",
    "abort": "abrt",
    "acknowledge": "ack",
    "address": "addr",
    "addresses": "addrs",
    "addresses": "addrs",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "allocate": "alloc",
    "allocate": "alloc",
    "alternative": "alt",
    "apple": "appl",
    "apple": "appl",
    "application": "app",
    "applications": "apps",
    "architecture": "arch",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "assembly": "asm",
    "asynchronous": "async",
    "asynchronous": "async",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "authn",
    "authorization": "authz",
    "auto group": "augroup",
    "authentication": "authn",
    "authorization": "authz",
    "auto group": "augroup",
    "average": "avg",
    "away from keyboard": "afk",
    "backup": "bkp",
    "backup": "bkp",
    "be right back": "brb",
    "binary": "bin",
    "block": "blk",
    "block": "blk",
    "boolean": "bool",
    "bottom": "bot",
    "break point": "bp",
    "break points": "bps",
    "bottom": "bot",
    "break point": "bp",
    "break points": "bps",
    "british columbia": "bc",
    "buffer": "buf",
    "button": "btn",
    "by the way": "btw",
    "calculate": "calc",
    "calculator": "calc",
    "camera": "cam",
    "canada": "ca",
    "centimeter": "cm",
    "certificate": "cert",
    "certificates": "certs",
    "char": "chr",
    "character": "char",
    "check": "chk",
    "child": "chld",
    "chip": "cpu",
    "class": "cls",
    "client": "cli",
    "code Q L": "codeql",
    "column": "col",
    "command": "cmd",
    "commands": "cmds",
    "commands": "cmds",
    "comment": "cmt",
    "communication": "comm",
    "communications": "comms",
    "communication": "comm",
    "communications": "comms",
    "compare": "cmp",
    "condition": "cond",
    "condition": "cond",
    "conference": "conf",
    "config": "cfg",
    "configuration": "config",
    "configurations": "configs",
    "connection": "conn",
    "configuration": "config",
    "configurations": "configs",
    "connection": "conn",
    "constant": "const",
    "contribute": "contrib",
    "contribute": "contrib",
    "constructor": "ctor",
    "context": "ctx",
    "control flow graph": "cfg",
    "control": "ctrl",
    "context": "ctx",
    "control flow graph": "cfg",
    "control": "ctrl",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "credential": "cred",
    "credentials": "creds",
    "cross reference": "xref",
    "cross references": "xrefs",
    "cuddle": "ctl",
    "current": "cur",
    "cute": "qt",
    "credential": "cred",
    "credentials": "creds",
    "cross reference": "xref",
    "cross references": "xrefs",
    "cuddle": "ctl",
    "current": "cur",
    "cute": "qt",
    "database": "db",
    "date format": "yyyy-mm-dd",
    "debian": "deb",
    "debug": "dbg",
    "decimal": "dec",
    "date format": "yyyy-mm-dd",
    "debian": "deb",
    "debug": "dbg",
    "decimal": "dec",
    "declaration": "decl",
    "declare": "decl",
    "declare": "decl",
    "decode": "dec",
    "decrement": "dec",
    "define": "def",
    "definition": "def",
    "degree": "deg",
    "delete": "del",
    "depend": "dep",
    "depends": "deps",
    "description": "desc",
    "dest": "dst",
    "destination": "dest",
    "dest": "dst",
    "destination": "dest",
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "diagnostic": "diag",
    "diagnostic": "diag",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directories": "dirs",
    "directories": "dirs",
    "directory": "dir",
    "display": "disp",
    "distance": "dist",
    "display": "disp",
    "distance": "dist",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "doing": "ing",  # some way to add 'ing' to verbs
    "doing": "ing",  # some way to add 'ing' to verbs
    "double ended queue": "deque",
    "double": "dbl",
    "double": "dbl",
    "dupe": "dup",
    "duplicate": "dup",
    "dynamic": "dyn",
    "elastic": "elast",  # elastdocker, elastalert, etc
    "element": "elem",
    "elements": "elems",
    "encode": "enc",
    "end of day": "eod",
    "end of month": "eom",
    "end of quarter": "eoq",
    "end of week": "eow",
    "end of year": "eoy",
    "end of day": "eod",
    "end of month": "eom",
    "end of quarter": "eoq",
    "end of week": "eow",
    "end of year": "eoy",
    "entry": "ent",
    "enumerate": "enum",
    "environment": "env",
    "equal": "eq",
    "equals": "eq",
    "error": "err",
    "escape": "esc",
    "etcetera": "etc",
    "ethernet": "eth",
    "evaluate": "eval",
    "ethernet": "eth",
    "evaluate": "eval",
    "example": "ex",
    "exception": "exc",
    "executable": "exe",
    "executables": "exes",
    "executable": "exe",
    "executables": "exes",
    "execute": "exec",
    "experience": "exp",
    "expression": "expr",
    "expressions": "exprs",
    "expressions": "exprs",
    "extend": "ext",
    "extension": "ext",
    "external": "extern",
    "eye dent": "id",
    "eye low": "ilo",
    "eye octal": "ioctl",
    "eye three": "i3",
    "feature": "feat",
    "file system": "fs",
    "fingerprint": "fp",
    "for what": "fwiw",
    "fingerprint": "fp",
    "for what": "fwiw",
    "format": "fmt",
    "fortigate": "fgt",
    "fortigate": "fgt",
    "framework": "fw",
    "frequency": "freq",
    "frequency": "freq",
    "function": "func",
    "functions": "funcs",
    "functions": "funcs",
    "funny": "lol",
    "fuzzy": "fzy",
    "ge bag": "gdb",
    "ge lib see": "glibc",
    "generate": "gen",
    "generic": "gen",
    "greater than": "gt",
    "hardware": "hw",
    "header": "hdr",
    "hello": "helo",
    "history": "hist",
    "hypertext": "http",
    "identity": "id",
    "ignore": "ign",
    "identity": "id",
    "ignore": "ign",
    "image": "img",
    "implement": "impl",
    "implementation": "impl",
    "import address table": "iat",
    "import table": "iat",
    "in real life": "irl",
    "import table": "iat",
    "in real life": "irl",
    "increment": "inc",
    "index": "idx",
    "index": "idx",
    "information": "info",
    "infrastructure": "infra",
    "infrastructure": "infra",
    "initialize": "init",
    "initializer": "init",
    "inode": "ino",
    "insert": "ins",
    "inode": "ino",
    "insert": "ins",
    "instance": "inst",
    "instruction": "insn",
    "instruction": "insn",
    "integer": "int",
    "interpreter": "interp",
    "interpreter": "interp",
    "interrupt": "int",
    "iterate": "iter",
    "jason five": "json5",
    "jason": "json",
    "java archive": "jar",
    "javascript": "js",
    "jiff": "gif",
    "journal cuttle": "journalctl",
    "jiff": "gif",
    "journal cuttle": "journalctl",
    "jump": "jmp",
    "just in time": "jit",
    "ka san": "KASAN",
    "kay": "kk",
    "kernel": "krnl",
    "key cuttle": "keyctl",
    "keyboard": "kbd",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "language": "lang",
    "language": "lang",
    "laugh out loud": "lol",
    "length": "len",
    "less than": "lt",
    "lib P T malloc": "libptmalloc",
    "lib see": "libc",
    "library": "lib",
    "line": "ln",
    "lisp": "lsp",
    "looks good to me": "lgtm",
    "lycanthrope": "lycan",
    "mail": "smtp",
    "maintenance": "maint",
    "make": "mk",
    "management": "mgmt",
    "manager": "mgr",
    "manitoba": "mb",
    "markdown": "md",
    "maximum": "max",
    "memory": "mem",
    "message message": "msg_msg",
    "message": "msg",
    "meta sploit framework": "msf",
    "meta sploit": "msf",
    "meta sploit": "msf",
    "microphone": "mic",
    "middle": "mid",
    "middle": "mid",
    "milligram": "mg",
    "millisecond": "ms",
    "minimum viable product": "mvp",
    "minimum": "min",
    "minimum": "min",
    "miscellaneous": "misc",
    "modify": "mod",
    "modify": "mod",
    "module": "mod",
    "modules": "mods",
    "monitor": "mon",
    "modules": "mods",
    "monitor": "mon",
    "mount": "mnt",
    "multiple": "multi",
    "muscle": "musl",
    "multiple": "multi",
    "muscle": "musl",
    "mutate": "mut",
    "name cash": "nscd",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "nb",
    "nova scotia": "ns",
    "number": "num",
    "numbers": "nums",
    "numbers": "nums",
    "object": "obj",
    "objects": "objs",
    "offset": "off",
    "offsets": "offs",
    "objects": "objs",
    "offset": "off",
    "offsets": "offs",
    "okay": "ok",
    "ontario": "on",
    "operating system": "os",
    "operation": "op",
    "operations": "ops",
    "operating system": "os",
    "operation": "op",
    "operations": "ops",
    "option": "opt",
    "options": "opts",
    "original": "orig",
    "out of bounds": "oob",
    "package build": "pkgbuild",
    "out of bounds": "oob",
    "package build": "pkgbuild",
    "package": "pkg",
    "packages": "pkgs",
    "packet": "pkt",
    "packets": "pkts",
    "packages": "pkgs",
    "packet": "pkt",
    "packets": "pkts",
    "parameter": "param",
    "parameters": "params",
    "password": "passwd",
    "performance": "perf",
    "performance": "perf",
    "physical": "phys",
    "physical address": "paddr",
    "pick": "pic",
    "pico second": "ps",
    "pie": "py",
    "ping": "png",
    "pie": "py",
    "ping": "png",
    "pixel": "px",
    "point": "pt",
    "pointer": "ptr",
    "pointers": "ptrs",
    "pone to own": "pwn2own",
    "pone": "pwn",
    "position independent code": "pic",
    "position independent executable": "pie",
    "position": "pos",
    "pound bag": "pwndbg",
    "preference": "pref",
    "preferences": "prefs",
    "position": "pos",
    "pound bag": "pwndbg",
    "preference": "pref",
    "preferences": "prefs",
    "previous": "prev",
    "private": "priv",
    "process": "proc",
    "processor": "cpu",
    "program": "prog",
    "programs": "progs",
    "properties": "props",
    "property": "prop",
    "protocol": "proto",
    "public": "pub",
    "python": "py",
    "quebec": "qc",
    "query string": "qs",
    "radian": "rad",
    "random": "rand",
    "read right ex": "rwx",
    "random": "rand",
    "read right ex": "rwx",
    "receipt": "rcpt",
    "receive": "recv",
    "record": "rec",
    "recording": "rec",
    "rectangle": "rect",
    "ref count": "refcnt",
    "receive": "recv",
    "record": "rec",
    "recording": "rec",
    "rectangle": "rect",
    "ref count": "refcnt",
    "reference": "ref",
    "references": "refs",
    "register": "reg",
    "registers": "regs",
    "registers": "regs",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "remove": "rm",
    "remove": "rm",
    "repel": "repl",
    "repetitive strain injury": "rsi",
    "repository": "repo",
    "repetitive strain injury": "rsi",
    "repository": "repo",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "requests": "reqs",
    "resources": "rsrcs",
    "response": "resp",
    "resources": "rsrcs",
    "response": "resp",
    "result": "res",
    "return": "ret",
    "revision": "rev",
    "round": "rnd",
    "round": "rnd",
    "ruby": "rb",
    "rust": "rs",
    "samba D": "smbd",
    "samba": "smb",
    "samba": "smb",
    "saskatchewan": "sk",
    "schedule": "sched",
    "scheduler": "sched",
    "screen": "scr",
    "scuzzy": "scsi",
    "second": "sec",
    "section": "sect",
    "sections": "sects",
    "secure shell": "ssh",
    "secure": "sec",
    "security": "sec",
    "see": "C",
    "segment": "seg",
    "select": "sel",
    "semaphore": "sem",
    "send": "snd",
    "sequel": "sql",
    "sequence": "seq",
    "schedule": "sched",
    "scheduler": "sched",
    "screen": "scr",
    "scuzzy": "scsi",
    "see": "C",
    "segment": "seg",
    "select": "sel",
    "semaphore": "sem",
    "send": "snd",
    "sequel": "sql",
    "sequence": "seq",
    "server": "srv",
    "service": "svc",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "signal": "sig",
    "size": "sz",
    "snipped": "[...]",
    "some": "sum",
    "signal": "sig",
    "size": "sz",
    "snipped": "[...]",
    "some": "sum",
    "source": "src",
    "sources": "srcs",
    "sources": "srcs",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard error": "stderr",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "stood": "std",
    "start of day": "sod",
    "start of month": "som",
    "start of quarter": "soq",
    "start of week": "sow",
    "start of year": "soy",
    "statement": "stmt",
    "statistic": "stat",
    "statistics": "stats",
    "string": "str",
    "structure": "struct",
    "structures": "structs",
    "symbol": "sym",
    "structures": "structs",
    "symbol": "sym",
    "symbolic link": "symlink",
    "symbols": "syms",
    "symbols": "syms",
    "synchronize": "sync",
    "synchronous": "sync",
    "sys cuttle": "sysctl",
    "system call": "syscall",
    "system cuddle": "systemctl",
    "sys cuttle": "sysctl",
    "system call": "syscall",
    "system cuddle": "systemctl",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "talk": "toc",
    "talk": "toc",
    "technology": "tech",
    "temp": "tmp",
    "temp": "tmp",
    "temperature": "temp",
    "temporary": "tmp",
    "terminal": "term",
    "terminal": "term",
    "text": "txt",
    "time format": "hh:mm:ss",
    "time format": "hh:mm:ss",
    "time of check time of use": "toctou",
    "time to live": "ttl",
    "time to live": "ttl",
    "token": "tok",
    "transaction": "txn",
    "tunnel": "tun",
    "typescript": "ts",
    "ultimate": "ulti",
    "unique id": "uuid",
    "unknown": "unk",
    "unknown": "unk",
    "user id": "uid",
    "user": "usr",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "values": "vals",
    "values": "vals",
    "variable": "var",
    "variables": "vars",
    "vector": "vec",
    "variables": "vars",
    "vector": "vec",
    "verify": "vrfy",
    "version": "ver",
    "version": "ver",
    "versus": "vs",
    "video": "vid",
    "videos": "vids",
    "virtual machine": "vm",
    "virtual": "virt",
    "virtual address": "vaddr",
    "virtual machine": "vm",
    "virtual": "virt",
    "virtual address": "vaddr",
    "visual studio": "msvc",
    "visual": "vis",
    "volume": "vol",
    "vulnerable": "vuln",
    "warning": "warn",
    "wave": "wav",
    "web": "www",
    "what the fuck": "wtf",
    "wind": "wnd",
    "wind": "wnd",
    "window": "win",
    "windows kernel": "ntoskrnl",
    "windows kernel": "ntoskrnl",
    "work in progress": "wip",
}


@mod.capture(rule="brief {user.abbreviation}")
def abbreviation(m) -> str:
    "One abbreviation"
    return m.abbreviation


# This variable is also considered exported for the create_spoken_forms module
abbreviations_list = get_list_from_csv(
    "abbreviations.csv",
    headers=("Abbreviation", "Spoken Form"),
    default=abbreviations_list,
)

# Allows the abbreviated/short form to be used as spoken phrase. eg "brief app" -> app
abbreviations_list_with_values = {
    **{v: v for v in abbreviations_list.values()},
    **abbreviations_list,
}

ctx = Context()
ctx.lists["user.abbreviation"] = abbreviations_list_with_values
