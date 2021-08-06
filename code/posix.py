from talon import Context, Module

mod = Module()
mod.list("signals", desc="Names for posix signals")

ctx = Context()
ctx.lists["user.signals"] = {
    "hup": "SIGHUP",
    "int": "SIGINT",
    "quit": "SIGQUIT",
    "ill": "SIGILL",
    "trap": "SIGTRAP",
    "cancel": "SIGABRT",  # can't use abort
    "E M T": "SIGEMT",
    "float": "SIGFPE",
    "kill": "SIGKILL",
    "bus": "SIGBUS",
    "seg fault": "SIGSEGV",
    "sys": "SIGSYS",
    "pipe": "SIGPIPE",
    "alarm": "SIGALRM",
    "term": "SIGTERM",
    "urge": "SIGURG",
    "stop": "SIGSTOP",
    "T stop": "SIGTSTP",
    "continue": "SIGCONT",
    "child": "SIGCHLD",
    # "" : "SIGTTIN",
    # "" : "SIGTTOU",
    "I O": "SIGIO",
    # "" : "SIGXCPU",
    # "" : "SIGXFSZ",
    "V T alarm": "SIGVTALRM",
    "profile": "SIGPROF",
    "winch": "SIGWINCH",
    "lost": "SIGLOST",
    "user": "SIGUSR1",
    "user two": "SIGUSR2",
    "power": "SIGPWR",
    "poll": "SIGPOLL",
    "wind": "SIGWIND",
    "phone": "SIGPHONE",
    "wait in": "SIGWAITIN",
    "L W P": "SIGLWP",
    "danger": "SIGDANGER",
    "grant": "SIGGRANT",
    "retract": "SIGRETRAC",
    "message": "SIGMSG",
    "sound": "SIGSOUND",
    "sack": "SIGSAK",
    "priority": "SIGPRIO",
}

@mod.capture(rule="{user.signals}")
def signal(m) -> str:
    "One signal"
    return m.signals
