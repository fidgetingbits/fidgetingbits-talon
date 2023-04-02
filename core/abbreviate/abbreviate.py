# this file is a set of words that have common abbreviations, but in some cases
# entries will also include acronyms or more technical vernacular, such as
# 'brief pie -> py'

from talon import Context, Module

mod = Module()
mod.list("abbreviation", desc="Common abbreviation")

ctx = Context()

abbreviations = {
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
    "address": "addr",
    "addresses": "addrs",
    "administrator": "admin",
    "administrators": "admins",
    "advance": "adv",
    "advanced": "adv",
    "alberta": "ab",
    "allocate": "alloc",
    "alternative": "alt",
    "apple": "appl",
    "application": "app",
    "applications": "apps",
    "argument": "arg",
    "arguments": "args",
    "as far as i can tell": "afaict",
    "as far as i know": "afaik",
    "assembly": "asm",
    "asynchronous": "async",
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
    "be right back": "brb",
    "binary": "bin",
    "block": "blk",
    "boolean": "bool",
    "bottom": "bot",
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
    "check": "chk",
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
    "constant": "const",
    "contribute": "contrib",
    "constructor": "ctor",
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
    "database": "db",
    "date format": "yyyy-mm-dd",
    "debian": "deb",
    "debug": "dbg",
    "decimal": "dec",
    "declaration": "decl",
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
    "develop": "dev",
    "development": "dev",
    "device": "dev",
    "diagnostic": "diag",
    "dictation": "dict",
    "dictionary": "dict",
    "direction": "dir",
    "directories": "dirs",
    "directory": "dir",
    "display": "disp",
    "distance": "dist",
    "distribution": "dist",
    "document": "doc",
    "documents": "docs",
    "doing": "ing",  # some way to add 'ing' to verbs
    "double ended queue": "deque",
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
    "eye dent": "id",
    "eye low": "ilo",
    "eye octal": "ioctl",
    "eye three": "i3",
    "feature": "feat",
    "file system": "fs",
    "fingerprint": "fp",
    "for what": "fwiw",
    "format": "fmt",
    "fortigate": "fgt",
    "framework": "fw",
    "frequency": "freq",
    "function": "func",
    "functions": "funcs",
    "funny": "lol",
    "fuzzy": "fzy",
    "ge bag": "gdb",
    "ge lib see": "glibc",
    "generate": "gen",
    "generic": "gen",
    "hardware": "hw",
    "header": "hdr",
    "hello": "helo",
    "history": "hist",
    "hypertext": "http",
    "identity": "id",
    "ignore": "ign",
    "image": "img",
    "implement": "impl",
    "import address table": "iat",
    "import table": "iat",
    "in real life": "irl",
    "increment": "inc",
    "index": "idx",
    "information": "info",
    "infrastructure": "infra",
    "initialize": "init",
    "initializer": "init",
    "inode": "ino",
    "insert": "ins",
    "instance": "inst",
    "instruction": "insn",
    "integer": "int",
    "interpreter": "interp",
    "interrupt": "int",
    "iterate": "iter",
    "jason five": "json5",
    "jason": "json",
    "java archive": "jar",
    "javascript": "js",
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
    "laugh out loud": "lol",
    "length": "len",
    "lib P T malloc": "libptmalloc",
    "lib see": "libc",
    "library": "lib",
    "lisp": "lsp",
    "looks good to me": "lgtm",
    "lycanthrope": "lycan",
    "mail": "smtp",
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
    "microphone": "mic",
    "middle": "mid",
    "milligram": "mg",
    "millisecond": "ms",
    "minimum viable product": "mvp",
    "minimum": "min",
    "miscellaneous": "misc",
    "modify": "mod",
    "module": "mod",
    "modules": "mods",
    "monitor": "mon",
    "mount": "mnt",
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
    "object": "obj",
    "objects": "objs",
    "offset": "off",
    "offsets": "offs",
    "okay": "ok",
    "ontario": "on",
    "operating system": "os",
    "operation": "op",
    "operations": "ops",
    "option": "opt",
    "options": "opts",
    "original": "orig",
    "out of bounds": "oob",
    "package build": "pkgbuild",
    "package": "pkg",
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
    "receipt": "rcpt",
    "receive": "recv",
    "record": "rec",
    "recording": "rec",
    "rectangle": "rect",
    "ref count": "refcnt",
    "reference": "ref",
    "references": "refs",
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
    "requests": "reqs",
    "resources": "rsrcs",
    "response": "resp",
    "result": "res",
    "return": "ret",
    "revision": "rev",
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
    "see": "C",
    "segment": "seg",
    "select": "sel",
    "semaphore": "sem",
    "send": "snd",
    "sequel": "sql",
    "sequence": "seq",
    "service pack": "sp",
    "session id": "sid",
    "shell": "sh",
    "shellcode": "sc",
    "signal": "sig",
    "size": "sz",
    "snipped": "[...]",
    "some": "sum",
    "source": "src",
    "sources": "srcs",
    "special": "spec",
    "specific": "spec",
    "specification": "spec",
    "specify": "spec",
    "standard error": "stderr",
    "standard in": "stdin",
    "standard out": "stdout",
    "standard": "std",
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
    "symbolic link": "symlink",
    "symbols": "syms",
    "synchronize": "sync",
    "synchronous": "sync",
    "sys cuttle": "sysctl",
    "system call": "syscall",
    "system cuddle": "systemctl",
    "system": "sys",
    "table of contents": "toc",
    "table": "tbl",
    "taiwan": "tw",
    "talk": "toc",
    "technology": "tech",
    "temp": "tmp",
    "temperature": "temp",
    "temporary": "tmp",
    "terminal": "term",
    "text": "txt",
    "time format": "hh:mm:ss",
    "time of check time of use": "toctou",
    "time to live": "ttl",
    "token": "tok",
    "transaction": "txn",
    "typescript": "ts",
    "ultimate": "ulti",
    "unique id": "uuid",
    "unknown": "unk",
    "user id": "uid",
    "user": "usr",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "values": "vals",
    "variable": "var",
    "variables": "vars",
    "vector": "vec",
    "verify": "vrfy",
    "version": "ver",
    "versus": "vs",
    "video": "vid",
    "videos": "vids",
    "virtual machine": "vm",
    "virtual": "virt",
    "virtual address": "vaddr",
    "visual studio": "msvc",
    "visual": "vis",
    "volume": "vol",
    "vulnerable": "vuln",
    "wave": "wav",
    "web": "www",
    "what the fuck": "wtf",
    "wind": "wnd",
    "window": "win",
    "windows kernel": "ntoskrnl",
    "work in progress": "wip",
}

ctx.lists["user.abbreviation"] = abbreviations


@mod.capture(rule="brief {user.abbreviation}")
def abbreviation(m) -> str:
    "One abbreviation"
    return m.abbreviation
