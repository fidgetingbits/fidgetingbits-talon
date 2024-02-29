from talon import Context, Module, actions

ctx = Context()
mod = Module()

code_format_string_add_number_prefix = mod.setting(
    "code_format_string_add_number_prefix",
    type=bool,
    default=True,
    desc="Whether or not to prefix hex, binary, octal numbers with their prefix (e.g. 0x) by default",
)
code_format_string_zero_pad_numbers = mod.setting(
    "code_format_string_zero_pad_numbers",
    type=bool,
    default=True,
    desc="Whether or not to zero pad numbers when using widths in format strings by default",
)
mod.tag(
    "code_format_strings",
    desc="Tag for enabling commands for inserting non-interpolated format string specifiers",
)
mod.tag(
    "code_format_string_interpolated_",
    desc="Tag for enabling commands for inserting interpolated format string specifiers",
)
mod.list("code_format_specifiers", desc="List of common formats specifiers: e.g. %lx")
mod.list(
    "code_interpolated_format_specifiers",
    desc="List of common interpolated formats specifiers: e.g. {foo:#02x}",
)

ctx.matches = r"""
tag: user.code_format_strings
"""

ctx.lists["user.code_format_specifiers"] = {
    "hex": "x",
    "long hex": "lx",
    "octal": "o",
    "character": "c",
    "string": "s",
    "integer": "d",
    "float": "f",
    "exponential": "e",
    "unsigned": "u",
}


@mod.action_class
class Actions:
    def code_format_specifier_prefix() -> str:
        """Return a format specifier prefix"""
        return "%"

    def code_format_specifier_suffix() -> str:
        """Return a format specifier suffix"""
        return ""

    def code_format_number_prefix(type: str) -> str:
        """Return a prefix for a number type, e.g. 0x for hex"""

        types = {v: k for k, v in ctx.lists["user.code_format_specifiers"].items()}
        type = types[type]
        if "hex" in type:
            return "0x"
        elif type == "octal":
            return "0o"
        elif type == "binary":
            return "0b"
        else:
            return ""

    def code_format_specifier(specifier: str, width: int) -> str:
        """Insert a format specifier with the optionally specified width"""
        s = ""
        if code_format_string_add_number_prefix.get():
            s += actions.user.code_format_number_prefix(specifier)
        s += actions.user.code_format_specifier_prefix()
        if width != 0:
            if code_format_string_zero_pad_numbers.get():
                s += "0"
            s += str(width)
        s += specifier
        s += actions.user.code_format_specifier_suffix()

        actions.insert(s)

    def code_interpolated_format_specifier_prefix() -> str:
        """Return an interpolated format specifier prefix"""
        return "{:"

    def code_interpolated_format_specifier_suffix() -> str:
        """Return an interpolated format specifier suffix"""
        return "}"

    def code_interpolated_format_specifier(specifier: str, width: int):
        """Insert an interpolated format specifier with the optionally specified width"""
        start = ""
        end = ""

        start += actions.user.code_interpolated_format_specifier_prefix()
        if code_format_string_add_number_prefix.get():
            # FIXME: This should probably be an action as well
            end += "#"
        if width != 0:
            if code_format_string_zero_pad_numbers.get():
                end += "0"
            end += str(width)

        end += specifier
        end += actions.user.code_interpolated_format_specifier_suffix()

        actions.user.insert_between(start, end)
        actions.edit.left()  # Skip the : to add the value
