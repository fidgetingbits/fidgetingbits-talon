import logging
import os
import re
from random import randint
from typing import List, Union

from talon import Context, Module, actions, app, clip, imgui, registry, ui
from talon.grammar import Phrase

ctx = Context()
key = actions.key
edit = actions.edit

words_to_keep_lowercase = (
    "a an and as at but by en for if in nor of on or per the to v via vs".split()
)

# The last phrase spoken, without & with formatting. Used for reformatting.
last_phrase = ""
last_phrase_formatted = ""

# Internally, a formatter is a pair (sep, fn).
#
# - sep: a boolean, true iff the formatter should leave spaces between words.
#   We use SEP & NOSEP for this for clarity.
#
# - fn: a function (i, word, is_end) --> formatted_word, called on each `word`.
#   `i` is the word's index in the list, and `is_end` is True iff it's the
#   last word in the list.
SEP = True
NOSEP = False


def format_phrase(m: Union[str, Phrase], formatters: str):
    global last_phrase, last_phrase_formatted
    last_phrase = m
    words = []
    if isinstance(m, str):
        words = m.split(" ")
    else:
        # # I believe this is no longer necessary. -rntz, 2022-02-10
        # # TODO: I've commented this out, remove if nobody has issues -rntz, 2022-06-21
        # if m.words[-1] == "over":
        #     m.words = m.words[:-1]
        words = actions.dictate.replace_words(actions.dictate.parse_words(m))

    result = last_phrase_formatted = format_phrase_without_adding_to_history(
        words, formatters
    )
    actions.user.add_phrase_to_history(result)
    # Arguably, we shouldn't be dealing with history here, but somewhere later
    # down the line. But we have a bunch of code that relies on doing it this
    # way and I don't feel like rewriting it just now. -rntz, 2020-11-04
    return result


def format_phrase_letters(m: str, formatters: str):
    """Mostly a copy of format_phrase, but for letters"""
    global last_phrase, last_phrase_formatted
    last_phrase = m
    words = m.split(" ")

    result = last_phrase_formatted = format_phrase_without_adding_to_history(
        words, formatters
    )
    actions.user.add_phrase_to_history(result)
    return result


def format_phrase_without_adding_to_history(word_list, formatters: str):
    # A formatter is a pair (keep_spaces, function). We drop spaces if any
    # formatter does; we apply their functions in reverse order.
    formatters = [all_formatters[name] for name in formatters.split(",")]
    separator = " " if all(x[0] for x in formatters) else ""
    functions = [x[1] for x in reversed(formatters)]
    words = []
    for i, word in enumerate(word_list):
        for f in functions:
            word = f(i, word, i == len(word_list) - 1)
        words.append(word)
    return separator.join(words)


# Formatter helpers
def surround(by):
    return lambda i, word, last: (by if i == 0 else "") + word + (by if last else "")


def prefixed_words_with_joiner(prefix, joiner):
    """Pass through words unchanged, but add a separator between them."""

    def formatter_function(i, word, _):
        return prefix + word if i == 0 else joiner + word

    return (NOSEP, formatter_function)


def words_with_joiner(joiner):
    """Pass through words unchanged, but add a separator between them."""
    return (NOSEP, lambda i, word, _: ("" if i == 0 else joiner) + word)


def first_vs_rest(first_func, rest_func=lambda w: w):
    """Supply one or two transformer functions for the first and rest of
    words respectively.

    Leave second argument out if you want all but the first word to be passed
    through unchanged.
    Set first argument to None if you want the first word to be passed
    through unchanged.
    """
    first_func = first_func or (lambda w: w)
    return lambda i, word, _: first_func(word) if i == 0 else rest_func(word)


def title_case():
    last_word = None

    def title_case_word(i, word, is_end):
        nonlocal last_word

        if word.islower() and (  # contains only lowercase letters
            word not in words_to_keep_lowercase
            or i == 0
            or is_end
            or not last_word[
                -1
            ].isalnum()  # title case subsequent words if they follow punctuation
        ):
            if "-" in word:
                components = word.split("-")
                title_case_component = title_case()
                components = [
                    title_case_component(j, component, j == len(components) - 1)
                    for j, component in enumerate(components)
                ]
                word = "-".join(components)
            elif word_start := re.match(r"\W*", word).end():
                # word begins with non-alphanumeric characters
                word = word[:word_start] + word[word_start:].capitalize()
            else:
                word = word.capitalize()

        last_word = word

        return word

    return title_case_word


def every_word(word_func):
    """Apply one function to every word."""
    return lambda i, word, _: word_func(word)


def spongebob(i, word, _):
    capitalize = bool(randint(0, 1))
    formatted_string = ""

    for char in word:
        if not char.isalpha():
            formatted_string += char
        elif capitalize:
            formatted_string += char.upper()
        else:
            formatted_string += char.lower()
        capitalize = not capitalize

    return formatted_string


def brief(word):
    formatted_string = ""
    if word in registry.lists["user.abbreviation"][0].keys():
        return registry.lists["user.abbreviation"][0][word]
    return word


# All formatters (code and prose)
formatters_dict = {
    "ALL_CAPS": (SEP, every_word(lambda w: w.upper())),
    "ALL_LOWERCASE": (SEP, every_word(lambda w: w.lower())),
    "ALL_BRIEF": (SEP, every_word(brief)),
    "CAPITALIZE_FIRST_WORD": (
        SEP,
        first_vs_rest(lambda w: title_case()(0, w, True)),
    ),
    "CAPITALIZE_ALL_WORDS": (SEP, title_case()),
    "C_POINTER_SEPARATED": words_with_joiner("->"),
    "COMMA_SEPARATED": words_with_joiner(", "),
    "DASH_SEPARATED": words_with_joiner("-"),
    "DOT_SEPARATED": words_with_joiner("."),
    "DOUBLE_COLON_SEPARATED": words_with_joiner("::"),
    "DOUBLE_QUOTED_STRING": (SEP, surround('"')),
    "DOUBLE_UNDERSCORE": (NOSEP, first_vs_rest(lambda w: f"__{w}__")),
    "EQUAL_SEPARATED": words_with_joiner("="),
    "FIRST_THREE": (NOSEP, lambda i, word, _: word[0:3]),
    "FIRST_FOUR": (NOSEP, lambda i, word, _: word[0:4]),
    "FIRST_FIVE": (NOSEP, lambda i, word, _: word[0:5]),
    "FOLDER_SEPARATED": (NOSEP, every_word(lambda w: w + os.sep)),
    "ROOT_FOLDER_SEPARATED": (
        NOSEP,
        first_vs_rest(lambda w: os.sep + w + os.sep, lambda w: w + os.sep),
    ),
    "WINDOWS_FOLDER_SEPARATED": (NOSEP, every_word(lambda w: w + "\\")),
    "WINDOWS_ROOT_FOLDER_SEPARATED": (
        NOSEP,
        first_vs_rest(lambda w: "\\" + w + "\\", lambda w: w + "\\"),
    ),
    "LONG_ARG": prefixed_words_with_joiner("--", "-"),
    "SHORT_ARG": prefixed_words_with_joiner("-", "-"),
    "SCORE_SEPARATED": prefixed_words_with_joiner("__", "_"),
    "NO_SPACES": (NOSEP, every_word(lambda w: w)),
    "NOOP": (SEP, lambda i, word, _: word),
    "PIPE_SEPARATED": words_with_joiner("|"),
    "PRIVATE_CAMEL_CASE": (NOSEP, first_vs_rest(lambda w: w, lambda w: w.capitalize())),
    "PROTECTED_CAMEL_CASE": (
        NOSEP,
        first_vs_rest(lambda w: w, lambda w: w.capitalize()),
    ),
    "PUBLIC_CAMEL_CASE": (NOSEP, every_word(lambda w: w.capitalize())),
    "SINGLE_QUOTED_STRING": (SEP, surround("'")),
    "SLASH_SEPARATED": words_with_joiner("/"),
    "SNAKE_CASE": (
        NOSEP,
        first_vs_rest(lambda w: w.lower(), lambda w: "_" + w.lower()),
    ),
    "SPACE_SURROUNDED_STRING": (SEP, surround(" ")),
    "SPONGEBOB": (SEP, spongebob),
}

# Mapping from spoken phrases to formatter names
code_formatter_names = {
    "arguing": "COMMA_SEPARATED",
    "all cap": "ALL_CAPS",
    "all down": "ALL_LOWERCASE",
    "camel": "PRIVATE_CAMEL_CASE",
    "dotted": "DOT_SEPARATED",
    "dunder": "DOUBLE_UNDERSCORE",
    "hammer": "PUBLIC_CAMEL_CASE",
    "proud": "PUBLIC_CAMEL_CASE",
    "dashing": "DASH_SEPARATED",
    "packing": "DOUBLE_COLON_SEPARATED",
    "padded": "SPACE_SURROUNDED_STRING",
    "slasher": "SLASH_SEPARATED",
    "snake": "SNAKE_CASE",
    "pathing": "FOLDER_SEPARATED",
    "root pathing": "ROOT_FOLDER_SEPARATED",
    "piping": "PIPE_SEPARATED",
    "windows pathing": "WINDOWS_FOLDER_SEPARATED",
    "windows root pathing": "WINDOWS_ROOT_FOLDER_SEPARATED",
    "long arg": "LONG_ARG",
    "scoring": "SCORE_SEPARATED",
    "pointing": "C_POINTER_SEPARATED",
    "equaling": "EQUAL_SEPARATED",
    "smashing": "NO_SPACES",
    "turbo": "DOUBLE_COLON_SEPARATED",
}
prose_formatter_names = {
    "briefing": "ALL_BRIEF",
    "say": "NOOP",
    "speak": "NOOP",
    "sentence": "CAPITALIZE_FIRST_WORD",
    "title": "CAPITALIZE_ALL_WORDS",
    "spongebob": "SPONGEBOB",
    "quoted": "DOUBLE_QUOTED_STRING",
    "ticks": "SINGLE_QUOTED_STRING",
    "upper": "ALL_CAPS",
    "lower": "ALL_LOWERCASE",
}


# # This is the mapping from spoken phrases to formatters.
# formatters_words = {
#     "briefing": formatters_dict["ALL_BRIEF"],
#     "camel": formatters_dict["PRIVATE_CAMEL_CASE"],
#     "arguing": formatters_dict["COMMA_SEPARATED"],
#     "dotted": formatters_dict["DOT_SEPARATED"],
#     "dunder": formatters_dict["DOUBLE_UNDERSCORE"],
#     "scoring": formatters_dict["SCORE_SEPARATED"],
#     "pathing": formatters_dict["FOLDER_SEPARATED"],
#     "root pathing": formatters_dict["ROOT_FOLDER_SEPARATED"],
#     "piping": formatters_dict["PIPE_SEPARATED"],
#     # This is good in addition to pathing, for when we are on linux and writing
#     # windows code, etc.
#     "windows pathing": formatters_dict["WINDOWS_FOLDER_SEPARATED"],
#     "windows root pathing": formatters_dict["WINDOWS_ROOT_FOLDER_SEPARATED"],
#     "hammer": formatters_dict["PUBLIC_CAMEL_CASE"],
#     "proud": formatters_dict["PUBLIC_CAMEL_CASE"],
#     "dashing": formatters_dict["DASH_SEPARATED"],
#     "equaling": formatters_dict["EQUAL_SEPARATED"],
#     "long arg": formatters_dict["LONG_ARG"],
#     "packing": formatters_dict["DOUBLE_COLON_SEPARATED"],
#     "turbo": formatters_dict["DOUBLE_COLON_SEPARATED"],
#     "padded": formatters_dict["SPACE_SURROUNDED_STRING"],
#     "pointing": formatters_dict["C_POINTER_SEPARATED"],
#     "slashing": formatters_dict["SLASH_SEPARATED"],
#     "smashing": formatters_dict["NO_SPACES"],
#     "snake": formatters_dict["SNAKE_CASE"],
#     "sponge bob": formatters_dict["SPONGEBOB"],
#     "quoted": formatters_dict["DOUBLE_QUOTED_STRING"],
#     "ticks": formatters_dict["SINGLE_QUOTED_STRING"],
#     "title": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     "upper": formatters_dict["ALL_CAPS"],
#     "lower": formatters_dict["ALL_LOWERCASE"],
# }

# This is the mapping for series of letters to formatters ex: abc to A B C
formatters_keys = {
    "spacing": formatters_dict["ALL_CAPS"],
}

# Mapping from spoken phrases to formatters
formatter_words = {
    phrase: formatters_dict[name]
    for phrase, name in (code_formatter_names | prose_formatter_names).items()
}

# Allow referencing formatters by either their names or spoken forms
all_prose_formatters = [
    item for sublist in prose_formatter_names.items() for item in sublist
]
all_formatters = formatters_dict | formatter_words | formatters_keys

mod = Module()
mod.list("formatters", desc="list of all formatters (code and prose)")
mod.list("code_formatter", desc="list of formatters typically applied to code")
mod.list("formatters_keys", desc="list of formatters handling individual letters")
mod.list(
    "prose_formatter", desc="list of prose formatters (words to start dictating prose)"
)


@mod.capture(rule="{self.formatters}+")
def formatters(m) -> str:
    "Returns a comma-separated string of formatters e.g. 'SNAKE,DUBSTRING'"
    return ",".join(m.formatters_list)


@mod.capture(rule="{self.formatters_keys}+")
def formatters_letters(m) -> str:
    "Returns a comma-separated string of formatters e.g. 'SNAKE,DUBSTRING'"
    return ",".join(m.formatters_keys_list)


@mod.capture(rule="{self.code_formatter}+")
def code_formatters(m) -> str:
    "Returns a comma-separated string of code formatters e.g. 'SNAKE,DUBSTRING'"
    return ",".join(m.code_formatter_list)


@mod.capture(
    # Note that if the user speaks something like "snake dot", it will
    # insert "dot" - otherwise, they wouldn't be able to insert punctuation
    # words directly.
    rule="<self.formatters> <user.text> (<user.text> | <user.formatter_immune>)*"
)
def format_text(m) -> str:
    """Formats text and returns a string"""
    out = ""
    formatters = m[0]
    for chunk in m[1:]:
        if isinstance(chunk, ImmuneString):
            out += chunk.string
        else:
            out += format_phrase(chunk, formatters)
    return out


@mod.capture(rule="<self.formatters_letters> <user.letters>")
def format_letters(m) -> str:
    "Formats the keys and returns a string"
    formatters = m[0]
    letters = m[1]
    out = format_phrase_letters(" ".join(list(letters)), formatters)
    return out


@mod.capture(
    rule="<self.code_formatters> <user.text> (<user.text> | <user.formatter_immune>)*"
)
def format_code(m) -> str:
    """Formats code and returns a string"""
    return format_text(m)


class ImmuneString:
    """Wrapper that makes a string immune from formatting."""

    def __init__(self, string):
        self.string = string


@mod.capture(
    # Add anything else into this that you want to be able to speak during a
    # formatter.
    rule="(<user.symbol_key> | (numb | numeral) <number>)"
)
def formatter_immune(m) -> ImmuneString:
    """Text that can be interspersed into a formatter, e.g. characters. It will be inserted directly, without being formatted."""
    if hasattr(m, "number"):
        value = m.number
    else:
        value = m[0]
        return ImmuneString(str(value))


@mod.action_class
class Actions:
    def formatted_text(phrase: Union[str, Phrase], formatters: str) -> str:
        """Formats a phrase according to formatters. formatters is a comma-separated string of formatters (e.g. 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING')"""
        return format_phrase(phrase, formatters)

    def insert_formatted(phrase: Union[str, Phrase], formatters: str):
        """Inserts a phrase formatted according to formatters. Formatters is a comma separated list of formatters (e.g. 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING')"""
        actions.insert(format_phrase(phrase, formatters))

    def insert_with_history(text: str):
        """Inserts some text, remembering it in the phrase history."""
        actions.user.deprecate_action("2022-12-11", "user.insert_with_history")

        actions.user.add_phrase_to_history(text)
        actions.insert(text)

    def formatters_reformat_last(formatters: str) -> str:
        """Clears and reformats last formatted phrase"""
        global last_phrase, last_phrase_formatted
        if actions.user.get_last_phrase() != last_phrase_formatted:
            # The last thing we inserted isn't the same as the last thing we
            # formatted, so abort.
            logging.warning(
                "formatters_reformat_last(): Last phrase wasn't a formatter!"
            )
            return
        actions.user.clear_last_phrase()
        actions.user.insert_formatted(last_phrase, formatters)

    def formatters_reformat_selection(formatters: str) -> str:
        """Reformats the current selection."""
        selected = edit.selected_text()
        if not selected:
            app.notify("Asked to reformat selection, but nothing selected!")
            return
        if formatters not in all_prose_formatters:
            selected = unformat_text(selected)
        # Delete separately for compatibility with programs that don't overwrite
        # selected text (e.g. Emacs)
        edit.delete()
        text = actions.self.formatted_text(selected, formatters)
        actions.insert(text)
        return text

    def get_formatters_words() -> dict:
        """returns a list of words currently used as formatters, and a demonstration string using those formatters"""
        formatters_help_demo = {}
        for name in sorted(set(formatter_words)):
            demo = format_phrase_without_adding_to_history(
                ["one", "two", "three"], name
            )
            if name in prose_formatter_names:
                name += " *"
            formatters_help_demo[name] = demo
        return formatters_help_demo

    def reformat_text(text: str, formatters: str) -> str:
        """Reformat the text."""
        if formatters not in all_prose_formatters:
            text = unformat_text(text)
        return actions.user.formatted_text(text, formatters)

    def insert_many(strings: List[str]) -> None:
        """Insert a list of strings, sequentially."""
        for string in strings:
            actions.insert(string)
            # actions.user.paste(string)


def unformat_text(text: str) -> str:
    """Remove format from text"""
    unformatted = re.sub(r"[\W_]+", " ", text)
    # Split on camelCase, including numbers
    # FIXME: handle non-ASCII letters!
    unformatted = re.sub(
        r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|(?<=[a-zA-Z])(?=[0-9])|(?<=[0-9])(?=[a-zA-Z])",
        " ",
        unformatted,
    )
    # TODO: Separate out studleycase vars
    return unformatted.lower()


ctx.lists["self.formatters"] = formatter_words.keys()
ctx.lists["self.code_formatter"] = code_formatter_names.keys()
ctx.lists["self.formatters_keys"] = formatters_keys.keys()
ctx.lists["self.prose_formatter"] = prose_formatter_names.keys()
