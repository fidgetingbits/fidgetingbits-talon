from typing import Union

from talon import Context, Module, actions

ctx = Context()
mod = Module()
mod.tag("code_types", desc="Tag for enabling types for programming languages")

mod.list("code_type", desc="List of types for active language")
mod.list("code_containing_types", desc="List of containing types for active language")


@ctx.capture(
    "user.code_type",
    rule="[{user.code_type_modifier}] {user.code_type} [or {user.code_type}]",
)
def code_type(m) -> str:
    """Returns a macro name"""
    s = ""
    types = m
    if "code_type_modifier" in m:
        s += m.code_type_modifier
        types = m[1:]
    if len(types) > 1:
        # Pull out every other element which will be "or"
        types = types[::2]
    separator = actions.user.code_alternative_type_separator()
    return separator.join(types)


@ctx.capture(
    "user.code_containing_type",
    rule="[{user.code_type_modifier}] {user.code_containing_types}",
)
def code_containing_type(m) -> str:
    """Returns a macro name"""
    return "".join(m)


@mod.capture(rule="{user.code_type}")
def code_type(m) -> str:
    """Returns a type name"""
    return m.code_type


@mod.capture(rule="{user.code_containing_type}")
def code_containing_type(m) -> str:
    """Returns a containing type name"""
    return m.code_containing_type


@mod.action_class
class Actions:
    def code_insert_type_annotation(type: str):
        """Inserts a type annotation"""

    def code_alternative_type_separator():
        """Separator for multi-types variables declarations"""
