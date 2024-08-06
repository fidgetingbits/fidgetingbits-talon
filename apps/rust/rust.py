from talon import Module

RUSTUP_COMMAND = "rust [up]"

mod = Module()


@mod.capture(rule=RUSTUP_COMMAND)
def rustup(m) -> str:
    """Verbs to use for rustup commands"""
    return str(m)
