"""
Stores terms that are used in many different places
"""

from talon import Module

mod = Module()

SELECT = "take"
TELEPORT = "pop"
OPERATOR = "put"
DELETE = "chuck"
FIND = "hunt"
SHOW_LIST = "list"
DRIVE = "drive"
# FIXME: Maybe move this elsewhere.. used for cd in terminal
GO = "pivot"
HISTORY = "(history|atuin)"
VPN = "V P N"
BREAKPOINT = (
    "point"  # don't use break, as it conflicts with cursorless in neovim terminals
)


@mod.capture(rule=SELECT)
def select(m) -> str:
    """Term for select"""
    return str(m)


@mod.capture(rule=TELEPORT)
def teleport(m) -> str:
    """Verb to use for commands that teleport the cursor to another place"""
    return str(m)


@mod.capture(rule=OPERATOR)
def operator(m) -> str:
    """Prefix for operators"""
    return str(m)


@mod.capture(rule=DELETE)
def delete(m) -> str:
    """Verb to use for commands that delete things"""
    return str(m)


@mod.capture(rule=FIND)
def find(m) -> str:
    """Verb to use for commands that find things"""
    return str(m)


@mod.capture(rule=SHOW_LIST)
def show_list(m) -> str:
    """Verb to use for commands that show lists"""
    return str(m)


@mod.capture(rule=GO)
def go(m) -> str:
    """Verb to use for commands that go to some location"""
    return str(m)


@mod.capture(rule=DRIVE)
def drive(m) -> str:
    """Verb to use for commands that deal with disks/drives"""
    return str(m)


@mod.capture(rule=HISTORY)
def history(m) -> str:
    """Verb to use for commands that deal with shell history"""
    return str(m)


@mod.capture(rule=VPN)
def vpn(m) -> str:
    """Verb to use for commands that deal with global vpn connections"""
    return str(m)


@mod.capture(rule=BREAKPOINT)
def breakpoint(m) -> str:
    """Term for break points"""
    return str(m)
