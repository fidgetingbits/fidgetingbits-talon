# This file is a set of words that have common abbreviations, but in some cases
# entries will also include acronyms or more technical vernacular, such as
# 'brief pie -> py'

from talon import Context, Module

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")

ctx = Context()
abbreviations = {
    "abort": "abrt",
    "acknowledge": "ack",
    "address": "addr",
    "addresses": "addrs",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "alternative": "alt",
    "allocate": "alloc",
    "apple": "appl",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "A sink": "async",
    "asynchronous": "async",
    "assembly": "asm",
    "at the moment": "atm",
    "attribute": "attr",
    "attributes": "attrs",
    "authenticate": "auth",
    "authentication": "authn",
    "authorization": "authz",
    "auto group": "augroup",
    "average": "avg",
    "away from keyboard": "afk",
    "backup": "bkp",
    "binary": "bin",
    "block": "blk",
    "boolean": "bool",
    "bottom": "bot",
    "B P F": "ebpf",
    "B P F trace": "bpftrace",
    "break point": "bp",
    "break points": "bps",
    "british columbia": "bc",
    "buffer": "buf",
    "button": "btn",
    "by the way": "btw",
    "calculator": "calc",
    "camera": "cam",
    "canada": "ca",
    "centimeter": "cm",
    "char": "chr",
    "character": "char",
    "child": "chld",
    "chip": "cpu",
    "class": "cls",
    "client": "cli",
    "code Q L": "codeql",
    "column": "col",
    "command": "cmd",
    "commands": "cmds",
    "comment": "cmt",
    "communication": "comm",
    "communications": "comms",
    "compare": "cmp",
    "condition": "cond",
    "conference": "conf",
    "config": "cfg",
    "configuration": "config",
    "configurations": "configs",
    "connection": "conn",
    "context": "ctx",
    "control": "ctrl",
    "control flow graph": "cfg",
    "constant": "const",
    "coordinate": "coord",
    "coordinates": "coords",
    "copy": "cpy",
    "count": "cnt",
    "counter": "ctr",
    "credential": "cred",
    "credentials": "creds",
    "current": "cur",
    "cuddle": "ctl",
    "cute": "qt",
    "database": "db",
    "date format": "yyyy-mm-dd",
    "declare": "decl",
    "declaration": "decl",
    "decode": "dec",
    "decrement": "dec",
    "debug": "dbg",
    "debian": "deb",
    "decimal": "dec",
    "define": "def",
    "definition": "def",
    "delete": "del",
    "description": "desc",
    "dest": "dst",
    "destination": "dest",
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "diagnostic": "diag",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directory": "dir",
    "directories": "dirs",
    "display": "disp",
    "distance": "dist",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "doing": "ing",  # some way to add 'ing' to verbs
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
    "entry": "ent",
    "enumerate": "enum",
    "environment": "env",
    "error": "err",
    "escape": "esc",
    "etcetera": "etc",
    "ethernet": "eth",
    "evaluate": "eval",
    "example": "ex",
    "exception": "exc",
    "executable": "exe",
    "executables": "exes",
    "execute": "exec",
    "experience": "exp",
    "expression": "expr",
    "expressions": "exprs",
    "extend": "ext",
    "extension": "ext",
    "external": "extern",
    "eye three": "i3",
    "eye dent": "id",
    "eye low": "ilo",
    "eye octal": "ioctl",
    "feature": "feat",
    "file system": "fs",
    "fingerprint": "fp",
    "for what": "fwiw",
    "format": "fmt",
    "framework": "fw",
    "frequency": "freq",
    "functions": "funcs",
    "funny": "lol",
    "fuzzy": "fzy",
    "ge lib see": "glibc",
    "ge bag": "gdb",
    "generic": "gen",
    "generate": "gen",
    "hardware": "hw",
    "header": "hdr",
    "hello": "helo",
    "history": "hist",
    "hypertext": "http",
    "identity": "id",
    "ignore": "ign",
    "image": "img",
    "import table": "iat",
    "import address table": "iat",
    "index": "idx",
    "increment": "inc",
    "information": "info",
    "initialize": "init",
    "initializer": "init",
    "inode": "ino",
    "in real life": "irl",
    "instance": "inst",
    "instruction": "insn",
    "interpreter": "interp",
    "integer": "int",
    "interrupt": "int",
    "iterate": "iter",
    "J peg": "jpg",
    "java archive": "jar",
    "javascript": "js",
    "jason": "json",
    "jason five": "json5",
    "journal cuttle": "journalctl",
    "jiff": "gif",
    "just in time": "jit",
    "jump": "jmp",
    "ka san": "KASAN",
    "kay": "kk",
    "kernel": "krnl",
    "keyboard": "kbd",
    "key cuttle": "keyctl",
    "keyword arguments": "kwargs",
    "keyword": "kw",
    "kilogram": "kg",
    "kilometer": "km",
    "K mem": "kmem",
    "language": "lang",
    "length": "len",
    "lib see": "libc",
    "library": "lib",
    "lib P T malloc": "libptmalloc",
    "lisp": "lsp",
    "lycanthrope": "lycan",
    "mail": "smtp",
    "make": "mk",
    "manager": "mgr",
    "management": "mgmt",
    "manitoba": "mb",
    "markdown": "md",
    "maximum": "max",
    "memory": "mem",
    "message": "msg",
    "message message": "msg_msg",
    "meta sploit": "msf",
    "meta sploit framework": "msf",
    "microphone": "mic",
    "middle": "mid",
    "milligram": "mg",
    "millisecond": "ms",
    "minimum": "min",
    "miscellaneous": "misc",
    "modify": "mod",
    "module": "mod",
    "modules": "mods",
    "monitor": "mon",
    "mount": "mnt",
    "multiple": "multi",
    "muscle": "musl",
    "name cash": "nscd",
    "nano second": "ns",
    "neo vim": "nvim",
    "new brunswick": "nb",
    "nova scotia": "ns",
    "number": "num",
    "numbers": "nums",
    "object": "obj",
    "objects": "objs",
    "offset": "off",
    "offsets": "offs",
    "okay": "ok",
    "ontario": "on",
    "operation": "op",
    "operations": "ops",
    "option": "opt",
    "options": "opts",
    "operating system": "os",
    "out of bounds": "oob",
    "original": "orig",
    "package": "pkg",
    "packages": "pkgs",
    "package build": "pkgbuild",
    "packet": "pkt",
    "packets": "pkts",
    "parameter": "param",
    "parameters": "params",
    "password": "passwd",
    "physical": "phys",
    "pick": "pic",
    "pico second": "ps",
    "pie": "py",
    "ping": "png",
    "pixel": "px",
    "performance": "perf",
    "point": "pt",
    "pointer": "ptr",
    "pointers": "ptrs",
    "position": "pos",
    "position independent code": "pic",
    "position independent executable": "pie",
    "preference": "pref",
    "preferences": "prefs",
    "previous": "prev",
    "private": "priv",
    "process": "proc",
    "processor": "cpu",
    "program": "prog",
    "programs": "progs",
    "property": "prop",
    "protocol": "proto",
    "P T malloc": "ptmalloc",
    "public": "pub",
    "pound bag": "pwndbg",
    "pone to own": "pwn2own",
    "pone": "pwn",
    "P R cuttle": "prctl",
    "python": "py",
    "quebec": "qc",
    "query string": "qs",
    "random": "rnd",
    "read right ex": "rwx",
    "receipt": "rcpt",
    "receive": "recv",
    "record": "rec",
    "recording": "rec",
    "rectangle": "rect",
    "reference": "ref",
    "references": "refs",
    "ref count": "refcnt",
    "register": "reg",
    "registers": "regs",
    "registery": "reg",
    "regular expression": "regex",
    "regular expressions": "regex",
    "remove": "rm",
    "repel": "repl",
    "repetitive strain injury": "rsi",
    "repository": "repo",
    "represent": "repr",
    "representation": "repr",
    "request": "req",
    "resource": "rsrc",
    "resources": "rsrcs",
    "response": "resp",
    "return": "ret",
    "revision": "rev",
    "ruby": "rb",
    "rust": "rs",
    "samba": "smb",
    "samba D": "smbd",
    "saskatchewan": "sk",
    "see": "C",
    "send": "snd",
    "sequel": "sql",
    "sequence": "seq",
    "segment": "seg",
    "semaphore": "sem",
    "schedule": "sched",
    "scheduler": "sched",
    "screen": "scr",
    "scuzzy": "scsi",
    "samba": "smb",
    "select": "sel",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "signal": "sig",
    "size": "sz",
    "snipped": "[...]",
    "source": "src",
    "sources": "srcs",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
    "start of day": "sod",
    "start of month": "som",
    "start of quarter": "soq",
    "start of week": "sow",
    "start of year": "soy",
    "statistic": "stat",
    "statistics": "stats",
    "statement": "stmt",
    "string": "str",
    "structure": "struct",
    "structures": "structs",
    "symbol": "sym",
    "symbols": "syms",
    "synchronize": "sync",
    "synchronous": "sync",
    "sys cuttle": "sysctl",
    "system": "sys",
    "system cuddle": "systemctl",
    "system call": "syscall",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "talk": "toc",
    "technology": "tech",
    "temperature": "temp",
    "temporary": "tmp",
    "temp": "tmp",
    "terminal": "term",
    "text": "txt",
    "time of check time of use": "toctou",
    "time format": "hh:mm:ss",
    "time to live": "ttl",
    "token": "tok",
    "ultimate": "ulti",
    "unique id": "uuid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "values": "vals",
    "variable": "var",
    "variables": "vars",
    "verify": "vrfy",
    "version": "ver",
    "versus": "vs",
    "virtual": "virt",
    "virtual machine": "vm",
    "visual": "vis",
    "visual studio": "msvc",
    "V M linux": "vmlinux",
    "volume": "vol",
    "vulnerable": "vuln",
    "wave": "wav",
    "web": "www",
    "what the fuck": "wtf",
    "wind": "wnd",
    "window": "win",
    "windows kernel": "ntoskrnl",
}

ctx.lists["user.abbreviation"] = abbreviations


@mod.capture(rule="brief {user.abbreviation}")
def abbreviation(m) -> str:
    "One abbreviation"
    return m.abbreviation
