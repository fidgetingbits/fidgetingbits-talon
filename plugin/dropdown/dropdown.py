from talon import Module

# FIXME: These should become a global list talon list somewhere and everything references it
DROPDOWN_COMMAND = "pick"

mod = Module()


@mod.capture(rule=DROPDOWN_COMMAND)
def dropdown(m) -> str:
    """Verbs to use for dropodown command"""
    return str(m)
