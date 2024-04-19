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
GO = "(go|pivot)"


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
