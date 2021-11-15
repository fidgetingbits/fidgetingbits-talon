import sys
from typing import Set

from talon import Context, Module, actions, app

# My experience:
#   fine - conflicts with find
#   jury  - two syllables, and matching with three or tree
#   jail  - suddenly always with til
#   pit  - conflicts with page
#   yank - conflicts with vim command
#   sit - conflicting with split on conformer
default_alphabet = "air bat cap drum each fin gust harp sit jury crunch look made near odd peck quench red sun trap urge vest whale plex yell zip".split(
    " "
)
letters_string = "abcdefghijklmnopqrstuvwxyz"

hex_alphabet = "A B C D E F".split(" ")
hex_letters_string = "abcdef"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("hex_letter", desc="Spoken hex letters (a-f)")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")


@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.hex_letter}")
def hex_letter(m) -> str:
    "One hex letter key"
    return m.hex_letter


@mod.capture(rule="{self.letter}")
def upper_letter(m) -> str:
    "Return one upper case"
    return m.letter.upper()


@mod.capture(rule="{self.letters}")
def letters(m) -> str:
    "Multiple letter keys"
    return m.letters


@mod.capture(rule="{self.hex_letters}")
def hex_letters(m) -> str:
    "Multiple hex letter keys"
    return m.hex_letters


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.special_key> )"
)
def unmodified_key(m) -> str:
    """A single key with no modifiers.

    Excludes arrow keys and function keys
    """
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def all_unmodified_key(m) -> str:
    "A single key including F keys and arrow keys, with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.all_unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.all_unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


@mod.capture(rule="{self.hex_letter}+")
def hex_letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.hex_letter_list)


ctx = Context()
modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "alt": "alt",  #'alter': 'alt',
    "control": "ctrl",  #'troll':   'ctrl',
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
}
if app.platform == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys
alphabet = dict(zip(default_alphabet, letters_string))
ctx.lists["self.letter"] = alphabet

# `punctuation_words` is for words you want available BOTH in dictation and as
# key names in command mode. 
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
# XXX - There should be a way to make some things only available in dictation
# mode...
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "grave": "`",
    # "comma": ",",
    "calm": ",",  # i found comma and commit would conflict too much
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "bang": "!",
    "dollar sign": "$",
    "asterisk": "*",
    "hash sign": "#",
    "percent sign": "%",
    #"at sign": "@",
    "amper": "&",
    "at sign": "@",
    "pound sign": "£",
}
symbol_key_words = {
    "grave": "`",
    "calm": ",",  # i found comma and commit would conflict too much
    "dot": ".",
    "blank": " ",
    "semi": ";",
    "tick": "'",
    "locker": "[",
    "rocker": "]",
    "slash": "/",
    "bish": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "question": "?",
    "wave": "~",
    "bang": "!",
    "dollar": "$",
    "score": "_",
    "coal": ":",
    "lub": "(",
    "rub": ")",
    "lace": "{",
    "racer": "}",
    "langle": "<",
    "rangle": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "cent": "%",
    "caret": "^",
    "swirl": "@",
    "amper": "&",
    "piper": "|",
    "quote": '"',
    "pound": "£",
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
number_keys = dict(zip(default_digits, numbers))
ctx.lists["self.number_key"] = number_keys

hex_spoken = dict(zip(default_alphabet[:6], hex_letters_string))
hex_alphabet = dict(zip(hex_alphabet, hex_letters_string))
ctx.lists["self.hex_letter"] = {**hex_spoken, **hex_alphabet, **number_keys}

ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}


simple_keys = [
    #    "backspace",
    "end",
    "enter",
    "escape",
    "home",
    #    "insert",
    #    "pagedown",
    #    "pageup",
    #    "space",
    "tab",
]

alternate_keys = {
    "junk": "backspace",
    "delhi": "delete",
    "page up": "pageup",
    "page down": "pagedown",
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


@mod.action_class
class Actions:
    def get_alphabet() -> dict:
        """Provides the alphabet dictionary"""
        return alphabet
