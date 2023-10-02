# see doc/vim.md

import logging
import pprint
import time

from talon import Context, Module, actions, app, settings, ui

try:
    import pynvim

    has_pynvim = True
except Exception:
    has_pynvim = False

logger = logging.getLogger("talon.vim")

mod = Module()
ctx = Context()

ctx.matches = r"""
app: vim
"""

# talon vim plugins. see apps/vim/plugins/
# to enable plugins you'll want to set these inside the corresponding mode
# talon file.
# XXX - that should just be automatically done based off the file names inside
# of the plugin folder since it's annoying to manage
# TODO: It would be good to mark some of these with nvim if their specific to neovim
plugin_tag_list = [
    "vim_ale",
    "vim_change_inside_surroundings",
    "vim_codeql",
    "vim_comment_nvim",
    "vim_copilot",
    "vim_cscope",
    "vim_easy_align",
    "vim_easymotion",
    "vim_eunuch",
    "vim_fern",
    "vim_fern_mapping_fzf",
    "vim_floaterm",
    "vim_fugitive",
    "vim_fugitive_summary",
    "vim_fzf",
    "vim_grammarous",
    "vim_lightspeed",
    "vim_leap",
    "vim_lsp",
    "vim_markdown",
    "vim_markdown_preview",
    "vim_markdown_toc",
    "vim_mason",
    "vim_mkdx",
    "vim_null_ls",
    "vim_follows_md_links",
    "vim_lazy",
    "vim_nerdtree",
    "vim_obsession",
    "vim_plug",
    "vim_rooter",
    "vim_signature",
    "vim_suda",
    "vim_surround",
    "vim_taboo",
    "vim_tabular",
    "vim_taskwiki",
    "vim_telescope",
    "vim_test",
    "vim_treesitter",
    "vim_treesitter_textobjects",
    "vim_unicode",
    "vim_ultisnips",
    "vim_wiki",
    "vim_you_are_here",
    "vim_youcompleteme",
    "vim_zenmode",
    "vim_zoom",
    "vim_trouble",
    "vim_luasnip",
    "vim_nvim_cmp",
    "vim_flip_ext",
    "nvim_lua",  # If you want to enable nvim-specific lua language commands
]
for entry in plugin_tag_list:
    mod.tag(entry, f"tag to load {entry} vim plugin commands")

# TODO: add code for creating all of the contexts and associated mode assertions by doing what
# we do in language_modes.py
mode_tag_list = [
    "vim_terminal_mode",
    "vim_command_mode",
    "vim_visual_mode",
    "vim_normal_mode",
    "vim_insert_mode",
    "vim_select_mode",
]
for entry in mode_tag_list:
    mod.tag(entry, f"tag to load {entry} specific commands")


# Based on you using a custom titlestring see doc/vim.md
@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        result = title.split(")")
        if len(result) > 1:
            # Assumes the last word after the last ) entry has the filename
            result = result[-1]
            # print(f"vim.filename(): {result.strip()}")
            return result.strip()
        else:
            return ""


ctx.lists["self.vim_arrow"] = {
    "left": "h",
    "right": "l",
    "up": "k",
    "down": "j",
}

# XXX - need to break into normal, visual, etc
# XXX - Technically some of these are not counted atm... so could be split
# Standard self.vim_counted_actions insertable entries
standard_counted_actions = {
    "suffix": "a",
    "append": "a",
    "suffix line": "A",
    "insert mode": "i",
    "insert column zero": "gI",
    "open below": "o",
    # "open above": "O",
    # opposite is useful for visual mode cursor swapping
    "opposite": "o",
    "substitute": "s",
    "substitute line": "S",
    "undo": "u",
    "regret": "u",
    "undo line": "U",
    "regret line": "U",
    # "erase": "x",
    "forget": '"_x',
    "erase reversed": "X",
    "paste": "p",
    "paste above": "P",
    "repeat": ".",
    "forget line": '"_dd',  # TODO - can we avoid because of clear line?
    # "yank line": "Y", # XXX - this has mode specific implementations now
    # "copy line": "Y",
    "scroll left": "zh",
    "scroll right": "zl",
    "scroll half screen left": "zH",
    "scroll half screen right": "zL",
    "scroll start": "zs",
    "scroll end": "ze",
    "upper line": "gUU",
    "lower line": "guu",
    # XXX - these work from visual mode and normal mode
    "prefix": "I",
    "play again": "@@",
    "toggle case": "~",
    "repeat last swap": "&",
    "dedent": "<<",
    "indent": ">>",
    "drop": "x",
    "open above": "O",
}


# Standard self.vim_counted_actions key() entries
standard_counted_actions_control_keys = {
    "redo": "ctrl-r",
    "scroll": "ctrl-f",
    "punk": "ctrl-b",
    "half down": "ctrl-d",
    "half up": "ctrl-u",
    "increment": "ctrl-a",
    "decrement": "ctrl-x",
}

# Custom self.vim_counted_actions insertable entries
# You can put custom aliases here to make it easier to manage. The idea is to
# alias commands from standard_counted_actions above, without replacing them
# there to prevent merge conflicts.
custom_counted_action = {}

# Custom self.vim_counted_actions insertable entries
# You can put custom shortcuts requiring key() here to make it easier to manage
custom_counted_actions_control_keys = {}

ctx.lists["self.vim_counted_actions"] = {
    **standard_counted_actions,
    **custom_counted_action,
}

ctx.lists["self.vim_counted_actions_keys"] = {
    **standard_counted_actions_control_keys,
    **custom_counted_actions_control_keys,
}

ctx.lists["self.vim_jump_range"] = {
    "jump to line of": "'",
    "jump to character of": "`",
}

ctx.lists["self.vim_jumps"] = {
    "start of last selection": "<",
    "end of last selection": ">",
    "latest jump": "'",
    "last exit": '"',
    "last insert": "^",
    "last change": ".",
}

ctx.lists["self.vim_counted_actions_args"] = {
    "macro play": "@",  # takes char arg
}

#  XXX - We need to break this up so that commands related to thing that
#  requires a motion can't be triggered otherwise, are only if they're in there
#  associated mode. For instance fold shouldn't be something that can be
#  triggered from normal or insert unless it's followed by some motion, whereas
#  in visual mode it's fine.
# normal mode commands that require motion, and that are counted
# includes motions and no motions :|
commands_with_motion = {
    # no motions
    "join line": "J",  # join alone too often conflicts with junkvim
    "merge": "gJ",  # won't produce spaces between joined words
    # "filter": "=",  # XXX - not sure about how to use this
    "paste": "p",  # XXX this really have motion
    "undo": "u",  # XXX this really have motion
    "regret": "u",  # XXX this really have motion
    "swap case": "~",
    # motions
    "change": '"_c',  # NOTE: we purposely use the black hole register
    "clear": "d",  # this is to be consistent with talon generic_editor.talon
    "forget": '"_d',  # this is to be consistent with talon generic_editor.talon
    "indent": ">",
    "unindent": "<",
    "yank": "y",  # NOTE: conflicts with talon 'yank' alphabet for 'y' key
    "copy": "y",
    "fetch": "y",
    "fold": "zf",
    "format": "gq",
    "to upper": "gU",
    "to lower": "gu",
    # comment.nvim
    # "comment": "gc",
    # "comment outer": "gca",
    # "comment inner": "gci",
}

# TODO: That should get moved to the visual mode file now

# only relevant when in visual mode. these will have some overlap with
# commands  and commands_with_motion above. this is mostly because
# some characters differ, and also in visual mode they don't have motions
visual_commands = {
    # normal overlap
    "change": '"_c',  # NOTE: we purposely use the black hole register
    "join lines": "J",
    "clear": "d",  # this is to be consistent with talon generic_editor.talon
    "forget": '"_d',  # this is to be consistent with talon generic_editor.talon
    "yank": "y",  # NOTE: conflicts with talon 'yank' alphabet for 'y' key
    "format": "gq",
    "fold": "zf",
    # some visual differences
    "to upper": "U",
    "to lower": "u",
    "swap case": "~",
    "opposite": "o",
    # counted
    "indent": ">",
    "unindent": "<",
}


ctx.lists["self.vim_motion_commands"] = list(
    set().union(commands_with_motion.keys(), visual_commands.keys())
)

# note that some of these are disabled to reduce the rule explosion to make
# things faster, where you can enable some if your detection is bad for the
# ones that are already enabled
# XXX - find a better name for the "big <thing>" names?
motions = {
    "back": "b",
    "big back": "B",
    "backie": "B",
    "tippy": "e",  # tip conflicts with other stuff
    "big tippy": "E",
    "word": "w",
    "big word": "W",
    "biggie": "W",
    # "tail": "ge",
    # "big tail": "gE",
    "right": "l",
    "left": "h",
    # "down": "j",
    "south": "j",
    # "up": "k",
    "north": "k",
    "next": "n",
    "previous": "N",
    "column zero": "0",
    "column": "|",
    "start of line": "^",
    "bend": "^",
    "lend": "$",
    "curse search": "*",
    "curse search reversed": "#",
    # TODO - make easier to remember/say
    "again": ";",
    "again reversed": ",",
    "tense": ")",
    "last tense": "(",
    "graph": "}",
    "last graph": "{",
    #    "section": "]]",
    #    "last section": "[[",
    "end section": "][",
    "last end section": "[]",
    # XXX - not sure about naming - don't seem to work yet
    "block end": "]}",
    "block start": "[{",
    "last block": "[}",
    "matching": "%",
    "down line": "+",
    "up line": "-",
    "first character": "_",
    "curse top": "H",
    "curse middle": "M",
    "curse last": "L",
    # "loft": "gg",
    # "file top": "gg",
    "gutter": "G",
    # "file ent": "G",
    "change": "]c",
    "last change": "[c",
}

# XXX - These come from treesitter-textobjects, so should really be injected
# from that .py
treesitter_motions = {
    "funk start": "[m",
    "funk next": "]m",
    "class start": "[[",
    "class next": "]]",
    "comment start": "[/",
    "comment next": "]/",
    "loop start": "[l",
    # "loop": "[l",
    "loop next": "]l",
    "condition start": "[C",
    # "condition": "[C",
    "condition next": "]C",
}


motions_custom = {}

ctx.lists["self.vim_motions"] = {
    **motions,
    **motions_custom,
    **treesitter_motions,
}


# TODO - Not sure if curse always applies
ctx.lists["self.vim_motions_keys"] = {
    "last curse": "ctrl-o",
    "next curse": "ctrl-i",
    # "retrace movements": "ctrl-o",
    # "retrace movements forward": "ctrl-i",
}

# all of these motions take a character argument
vim_character_motions = {
    "mark": "'",
    "find": "f",
    "fever": "F",
    "till": "t",
    # XXX - tier caused way too many problem
    "timber": "T",
}

custom_vim_motions_with_character_commands = {
    # XXX - these don't work due to comboing had to be moved into commands in a
    # talon file
    #    "last": "$F",  # find starting end of line
    #    "first": "^f",  # find starting beginning of line
}

ctx.lists["self.vim_motions_with_character"] = {
    **vim_character_motions,
    **custom_vim_motions_with_character_commands,
}


# all of these motions take a phrase argument
ctx.lists["self.vim_motions_with_phrase"] = {
    "search": "/",
    "search reversed": "?",
}

ctx.lists["self.vim_text_object_range"] = {
    "inner": "i",
    "inside": "i",
    "around": "a",
    "out side": "a",
    "outer": "a",
    "this": "a",
}

# Common names used for text object selection, vim-surround, etc
common_key_names = {
    "tick": "'",
    "quote": '"',
}


# XXX - Should match more wording in vim_surround_targets
# These can be pluralized because of how you speak vim grammars
# ex: yank inside braces
# however in practice talon matches them any ways
text_object_select = {
    "word": "w",
    "big word": "W",
    "block": "b",
    "big block": "B",
    "quote": '"',
    "tick": "'",
    "parens": "(",
    "round": "(",
    "angles": "<",
    "code block": "{",
    "braces": "{",
    "squares ": "[",
    "graves": "`",
    "sentence": "s",
    "graph": "p",
    "tag block": "t",
    "funk": "f",  # This is for around or iner
    "block": "b",
    "condition": "m",
    "loop": "l",
    "class": "c",
    "comment": "/",
}

text_object_select_custom = {}

ctx.lists["self.vim_text_object_select"] = {
    **text_object_select,
    **text_object_select_custom,
}

# Specific to the vim-surround plugin
# XXX - should be able to partially mix with earlier list
# XXX - should actually move to surround plugin
# XXX - revisit loose naming
# XXX - things like word, etc should probably be switched? I'm not sure what
# they do...
ctx.lists["self.vim_surround_targets"] = {
    "stars": "*",
    "word": "w",
    "big word": "W",
    "block": "b",
    "big block": "B",
    "quotes": '"',
    "ticks": "'",
    "loose parens": "(",
    "loose round": "(",
    "loose angles": "<",
    "loose braces": "{",
    "loose squares": "[",
    "round": ")",
    "parens": ")",
    "angles": ">",
    "braces": "}",
    "squares": "]",
    "graves": "`",
    "gravy": "```",
    "sentence": "s",
    "paragraph": "p",
    "spaces": "  ",  # double spaces is required because surround gets confused
    "tags": "t",
    "H one tags": "<h1>",
    "H two tags": "<h2>",
    "div tags": "<div>",
    "bold tags": "<b>",
}

# settings that you can just set by sing on or off
# correlates to settings that start with no in turning off
vim_on_and_off_settings = {
    "see indent": "cindent",
}

mod.tag("vim", desc="a tag to load various vim plugins")
mod.tag("vim_terminal", desc="a tag to designate if we are in a vim terminal")
mod.setting(
    "vim_preserve_insert_mode",
    type=int,
    default=1,
    desc="If normal mode actions are called from insert mode, stay in insert",
)

mod.setting(
    "vim_adjust_modes",
    type=int,
    default=1,
    desc="User wants talon to automatically adjust modes for commands",
)

mod.setting(
    "vim_notify_mode_changes",
    type=int,
    default=0,
    desc="Notify user about vim mode changes as they occur",
)

mod.setting(
    "vim_escape_terminal_mode",
    type=int,
    default=0,
    desc="When set won't limit what motions and commands will pop out of terminal mode",
)
mod.setting(
    "vim_cancel_queued_commands",
    type=int,
    default=1,
    desc="Press escape before issuing commands, to cancel previously queued command that might have been in error",
)

mod.setting(
    "vim_cancel_queued_commands_timeout",
    type=float,
    default=0.05,
    desc="How long to wait in seconds before issuing the real command after canceling",
)

mod.setting(
    "vim_mode_change_timeout",
    type=float,
    default=0.2,
    desc="It how long to wait before issuing commands after a mode change",
)

mod.setting(
    "vim_mode_switch_moves_cursor",
    type=int,
    default=0,
    desc="Preserving insert mode will automatically move the cursor. Setting this to 0 can override that.",
)

mod.setting(
    "vim_use_rpc",
    type=int,
    default=0,
    desc="Whether or not to use RPC if it is available. Useful for testing or avoiding bugs",
)
mod.setting(
    "vim_debug",
    type=int,
    default=0,
    desc="Debugging used for development",
)


# Standard VIM motions and action
mod.list("vim_arrow", desc="All vim direction keys")
mod.list("vim_motion_commands", desc="Counted VIM commands with motions")
# mod.list("vim_counted_motions", desc="Counted VIM motion verbs")
mod.list("vim_counted_actions", desc="Counted VIM action verbs")
mod.list("vim_counted_actions_keys", desc="Counted VIM action verbs ctrl keys")
mod.list(
    "vim_counted_actions_args", desc="Counted VIM action verbs with keyi arguments"
)
mod.list("vim_normal_counted_action", desc="Normal counted VIM actions")
mod.list("vim_normal_counted_actions_keys", desc="Counted VIM action verbs ctrl keys")
mod.list("vim_motions", desc="Non-counted VIM motions")
mod.list("vim_motions_keys", desc="Non-counted VIM motions ctrl keys")
mod.list("vim_motions_with_character", desc="VIM motion verbs with char arg")
mod.list("vim_motions_with_phrase", desc="VIM motion verbs with phrase arg")
mod.list("vim_motions_all", desc="All VIM motion verbs")
mod.list("vim_text_object_range", desc="VIM text object ranges")
mod.list("vim_text_object_select", desc="VIM text object selections")
mod.list("vim_jump_range", desc="VIM jump ranges")
mod.list("vim_jumps", desc="VIM jump verbs")
mod.list("vim_jump_targets", desc="VIM jump targets")
mod.list("vim_normal_counted_motion_command", desc="Counted normal VIM commands")
mod.list("vim_counted_motion_command_with_ordinals", desc="Counted normal VIM commands")
mod.list("vim_select_motion", desc="VIM visual mode selection motions")

# Plugin-specific lists
mod.list("vim_surround_targets", desc="VIM surround plugin targets")

# Plugin modes
mod.mode("vim_fugitive", desc="A fugitive mode that exposes git mappings")


@mod.capture(rule="{self.vim_arrow}")
def vim_arrow(m) -> str:
    "An arrow direction to be converted to vim direction"
    return m.vim_arrow


@mod.capture(rule="{self.vim_text_object_select}")
def vim_text_object_select(m) -> str:
    "Returns a string representing a selection text object"
    return m.vim_text_object_select


@mod.capture(rule="{self.vim_text_object_range}")
def vim_text_object_range(m) -> str:
    "Returns a string ranged text object"
    return m.vim_text_object_range


@mod.capture(rule="{self.vim_motions}")
def vim_motions(m) -> str:
    "Returns to string representing motion verb"
    return m.vim_motions


@mod.capture(rule="{self.vim_motions_keys}")
def vim_motions_keys(m) -> str:
    "Returns a key representing a motion"
    return m.vim_motions_keys


@mod.capture(
    rule="{self.vim_motions_with_character} (ship|upper|uppercase) <user.letter>"
)
def vim_motions_with_upper_character(m) -> str:
    "Returns a motion string with an upper case character"
    return m.vim_motions_with_character + "".join(list(m)[2:]).upper()


@mod.capture(
    rule="{self.vim_motions_with_character} (<user.letter>|<digits>|<user.symbol_key>)"
)
def vim_motions_with_character(m) -> str:
    "Returns a motion with a character argument"
    return m.vim_motions_with_character + "".join(str(x) for x in list(m)[1:])


@mod.capture(rule="{self.vim_motions_with_phrase} <user.text>")
def vim_motions_with_phrase(m) -> str:
    "Returns a motion with a phrase argument"
    return "".join(list(m.vim_motions_with_phrase + m.text))


@mod.capture(
    rule="[<user.number_string>] (<self.vim_motions>|<self.vim_motions_with_character>|<self.vim_motions_with_upper_character>|<self.vim_motions_with_phrase>)"
)
def vim_motions_all(m) -> str:
    "Returns a rule matching optionally numbered vim motion"
    return "".join(list(m))


@mod.capture(
    rule="[<user.number_string>] (<self.vim_motions>|<self.vim_motions_with_character>|<self.vim_motions_with_upper_character>|<self.vim_motions_with_phrase>)"
)
def vim_motions_all_adjust(m) -> str:
    "Returns a rule matching a vim motion, and adjusts the vim mode"
    v = VimMode()
    v.set_any_motion_mode()
    # print(m)
    return "".join(list(m))


@mod.capture(rule="{self.vim_counted_actions}")
def vim_counted_actions(m) -> str:
    "Returns string matching accounted action"
    return m.vim_counted_actions


@mod.capture(rule="{self.vim_counted_actions_keys}")
def vim_counted_actions_keys(m) -> str:
    "Returns key matching accounted action"
    return m.vim_counted_actions_keys


# @ctx.capture(rule="[<number_small>] <self.vim_motions_all>")
# def vim_counted_motions(m) -> str:
#    return "".join(str(x) for x in list(m))


@mod.capture(rule="{self.vim_jump_range}")
def vim_jump_range(m) -> str:
    "Returns a string representing a ranged jump"
    return m.vim_jump_range


@mod.capture(rule="{self.vim_jumps}")
def vim_jumps(m) -> str:
    "Returns a string representing a jump target"
    return m.vim_jumps


@mod.capture(rule="{self.vim_surround_targets}")
def vim_surround_targets(m) -> str:
    "Returns a string representing a vim surround plugin target"
    return m.vim_surround_targets


@mod.capture(rule="<self.vim_jump_range> <self.vim_jumps>")
def vim_jump_targets(m) -> str:
    "Returns a string representing a ranged jump target"
    return "".join(list(m))


@mod.capture(
    # XXX - trying to reduce list sizes and never use this
    rule="[<number_small>] [<self.vim_text_object_range>] <self.vim_text_object_select>"
    # rule="<self.vim_text_object_range> <self.vim_text_object_select>"
)
def vim_text_objects(m) -> str:
    "Returns a string representing a ranged texts objects selection"
    return "".join(str(x) for x in list(m))


# Sometimes you want to imply a surround action is going to work on a word, but
# saying around is tedious, of this is defaults to selecting around if no
# actual inner or around range is spoken
@mod.capture(rule="[<number_small>] <self.vim_text_object_select>")
def vim_unranged_surround_text_objects(m) -> str:
    "Returns a string representing an unranged surround plugin target"
    if len(list(m)) == 1:
        return "a" + "".join(list(m))
    else:
        return "".join(str(m.number_small)) + "a" + "".join(list(m)[1:])


@mod.capture(rule="{self.vim_motion_commands}")
def vim_motion_commands(m) -> str:
    "Returns a string representing a motion command"
    v = VimMode()
    if v.is_visual_mode():
        if str(m) in visual_commands:
            return visual_commands[str(m)]
    # Note this throws away commands that matched visual mode only stuff,
    # because if not in visual mode already, there is no selection anyway so
    # the command is moot
    elif str(m) not in commands_with_motion:
        print(f"no match for {str(m)}")
        return ""

    v.set_normal_mode()
    return commands_with_motion[str(m)]


@mod.capture(
    rule="[<number_small>] <self.vim_motion_commands> [(<self.vim_motions_all> | <self.vim_text_objects> | <self.vim_jump_targets>)]"
)
def vim_normal_counted_motion_command(m) -> str:
    "Returns a string representing a motion command with optional arguments"
    return "".join(str(x) for x in list(m))


@mod.capture(
    rule="<self.vim_motion_commands> <user.ordinals> (<self.vim_motions_all>|<self.vim_jump_targets>)"
)
def vim_counted_motion_command_with_ordinals(m) -> str:
    "Returns a string of a motion command with optional counted argument"
    return "".join([str(m.ordinals - 1), "".join(m[2:]), m[0], "".join(m[2:])])


@mod.capture(rule="[<number_small>] <self.vim_motions_keys>")
def vim_normal_counted_motion_keys(m) -> str:
    "Returns a string of a counted motion representing keys"
    # we do this because we pass everything to key() which needs a space
    # separated list
    if len(str(m).split(" ")) > 1:
        return " ".join(list((" ".join(list(str(m.number_small))), m.vim_motions_keys)))
    else:
        return m.vim_motions_keys


# XXX - could combine actions_keys and _action version by test if the entry is
# in which list. might reduce number usage?
@mod.capture(rule="[<number_small>] <self.vim_counted_actions>")
def vim_normal_counted_action(m) -> str:
    "Returns a string of a counted motion"
    # XXX - may need to do action-specific mode checking
    v = VimMode()
    v.cancel_queued_commands()
    if m.vim_counted_actions == "u":
        # undo doesn't work with ctrl-o it seems
        v.set_any_motion_mode_np()
    else:
        v.set_any_motion_mode()

    return "".join(str(x) for x in list(m))


@mod.capture(rule="[<number_small>] <self.vim_counted_actions_keys>")
def vim_normal_counted_actions_keys(m) -> str:
    "Returns a string of a counted action representing keys"
    v = VimMode()
    v.cancel_queued_commands()
    v.set_any_motion_mode()

    # we do this because repass everything to key() which needs a space
    # separated list
    if len(str(m).split(" ")) > 1:
        return " ".join(
            list((" ".join(list(str(m.number_small))), m.vim_counted_actions_keys))
        )
    else:
        return m.vim_counted_actions_keys


@mod.capture(
    rule="[<number_small>] (<self.vim_motions> | <self.vim_text_objects> | <self.vim_jump_targets>)"
)
def vim_select_motion(m) -> str:
    "Returns a string of some selection motion"
    return "".join(str(x) for x in list(m))


# @ctx.action_class("main")
# class main_actions:
#    def insert(text):
#        """override insert action to allow us to enter insert mode"""
#        v = VimMode()
#        v.set_insert_mode()
#        scripting.core.MainActions.insert(text)


# These are actions you can call from vim.talon via `user.method_name()` in
# order to modify modes, run commands in specific modes, etc
@mod.action_class
class Actions:
    def vim_set_normal_mode():
        """set normal mode"""
        v = VimMode()
        v.set_normal_mode(auto=False)

    def vim_set_normal_mode_exterm():
        """set normal mode and don't preserve the previous mode"""
        v = VimMode()
        v.set_normal_mode_exterm()

    def vim_set_normal_mode_np():
        """set normal mode and don't preserve the previous mode"""
        v = VimMode()
        v.set_normal_mode_np(auto=False)

    def vim_set_visual_mode():
        """set visual mode"""
        v = VimMode()
        v.set_visual_mode()

    def vim_set_visual_line_mode():
        """set visual line mode"""
        v = VimMode()
        v.set_visual_line_mode()

    def vim_set_visual_block_mode():
        """set visual block mode"""
        v = VimMode()
        v.set_visual_block_mode()

    def vim_set_insert_mode():
        """set insert mode"""
        v = VimMode()
        v.set_insert_mode()

    def vim_set_terminal_mode():
        """set terminal mode"""
        v = VimMode()
        v.set_terminal_mode()

    def vim_set_command_mode():
        """set visual mode"""
        v = VimMode()
        v.set_command_mode()

    def vim_set_command_mode_exterm():
        """set visual mode"""
        v = VimMode()
        v.set_command_mode_exterm()

    def vim_set_replace_mode():
        """set visual mode"""
        v = VimMode()
        v.set_replace_mode()

    def vim_set_visual_replace_mode():
        """set visual mode"""
        v = VimMode()
        v.set_visual_replace_mode()

    def vim_insert_mode(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        v = VimMode()
        v.set_insert_mode()
        actions.insert(cmd)

    def vim_insert_mode_key(cmd: str):
        """run a given list of commands in normal mode, preserve mode"""
        v = VimMode()
        v.set_insert_mode()
        actions.key(cmd)

    def vim_insert_mode_np(cmd: str):
        """run a given list of commands in normal mode, don't preserve"""
        v = VimMode()
        v.set_insert_mode_np()
        actions.insert(cmd)

    def vim_normal_mode(cmd: str):
        """run a given list of commands in normal mode, preserve INSERT"""
        v = VimMode()
        # XXX - This needs to be abstracted for the case where we don't have
        # RPC
        # This is required despite using the nvim.command() method because we
        # can access that mode from terminal mode:
        #  https://github.com/neovim/neovim/issues/4895#issuecomment-303073838
        if v.is_terminal_mode():
            v.set_normal_mode_exterm()
        vapi = VimAPI()
        vapi.api.run_normal_mode_command(cmd)

    def vim_normal_mode_np(cmd: str):
        """run a given list of commands in normal mode, don't preserve
        INSERT"""
        v = VimMode()
        v.set_normal_mode_np()
        actions.insert(cmd)

    def vim_normal_mode_exterm(cmd: str):
        """run a given list of commands in normal mode, don't preserve INSERT,
        escape from terminal mode"""
        v = VimMode()
        v.set_normal_mode_exterm()
        actions.insert(cmd)

    def vim_normal_mode_exterm_preserve(cmd: str):
        """run a given list of commands in normal mode, escape from terminal
        mode, but return to terminal mode after. Special case for settings"""
        v = VimMode()
        v.set_normal_mode_exterm()
        actions.insert(cmd)

    def vim_normal_mode_key(cmd: str):
        """press a given key in normal mode"""
        v = VimMode()
        v.set_normal_mode()
        actions.key(cmd)

    def vim_normal_mode_exterm_key(cmd: str):
        """press a given key in normal mode, and escape terminal"""
        v = VimMode()
        v.set_normal_mode_exterm()
        actions.key(cmd)

    def vim_normal_mode_keys(keys: str):
        """press a given list of keys in normal mode"""
        v = VimMode()
        v.set_normal_mode()
        for key in keys.split(" "):
            # print(key)
            actions.key(key)

    def vim_normal_mode_exterm_keys(keys: str, term_return: str = "False"):
        """press a given list of keys in normal mode"""
        v = VimMode()
        v.set_normal_mode_exterm()
        for key in keys.split(" "):
            # print(key)
            actions.key(key)
        if term_return == "True":
            v.set_insert_mode()

    def vim_visual_mode(cmd: str):
        """run a given list of commands in visual mode"""
        v = VimMode()
        v.set_visual_mode()
        actions.insert(cmd)

    def vim_command_mode(cmd: str):
        """run string of commands in command line mode.

        Preserves INSERT
        """
        vapi = VimAPI()
        vapi.api.run_command_mode_command(cmd)

    def vim_command_mode_exterm(cmd: str):
        """run string of commands in command line mode.

        - Preserves INSERT
        - Exits terminal mode
        """
        vapi = VimAPI()
        vapi.api.run_command_mode_command_exterm(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_any_motion_mode(cmd: str):
        """run a given list of commands in normal mode"""
        v = VimMode()
        v.set_any_motion_mode()
        actions.insert(cmd)

    # Sometimes the .talon file won't know what mode to run something in, just
    # that it needs to be a mode that supports motions like normal and visual.
    def vim_any_motion_mode_exterm(cmd: str):
        """run a given list of commands in some motion mode"""
        v = VimMode()
        v.set_any_motion_mode_exterm()
        actions.insert(cmd)

    def vim_any_motion_mode_key(cmd: str):
        """run a given list of commands in normal mode"""
        v = VimMode()
        v.set_any_motion_mode()
        actions.key(cmd)

    def vim_any_motion_mode_exterm_key(cmd: str):
        """run a given list of commands in normal mode"""
        v = VimMode()
        v.set_any_motion_mode_exterm()
        actions.key(cmd)


class NeoVimRPC:
    """For setting/pulling the modes using RPC"""

    def __init__(self):
        self.init_ok = False
        self.nvim = None

        if settings.get("user.vim_use_rpc") == 0:
            return

        self.rpc_path = self.get_active_rpc()
        if self.rpc_path is not None:
            try:
                # XXX - I'm not sure why but suddenly talon is automatically
                # setting the loggers associated with pynvim to DEBUG, so I
                # need to set them to WARNING every time
                loggers = logging.root.manager.loggerDict.keys()
                for l in loggers:
                    # if l.startswith("pynvim"):
                    # print(f"DEBUG: Resetting log level for {l}")
                    nvim_logger = logging.getLogger(l)
                    nvim_logger.setLevel(logging.ERROR)
                # loggers = [
                #     logging.getLogger(name) for name in logging.root.manager.loggerDict
                # ]

                # NOTE: This is used to avoid "Using selector: EpollSelector" spam
                from pprint import pprint

                # pprint("Detected loggers:")
                # pprint(loggers)
                self.nvim = pynvim.attach("socket", path=self.rpc_path)
            except RuntimeError:
                return
            self.init_ok = True
        else:
            return

    def get_active_rpc(self):
        title = ui.active_window().title
        if "RPC" in title:
            named_pipe = title.split("RPC:")[1].split(" ")[0]
            return named_pipe
        return None

    def get_active_mode(self):
        mode = self.nvim.request("nvim_get_mode")
        return mode


class VimDirectInput:
    """For when RPC is not available or we want to insert partial commands

    This relies on a more finnicky method of detecting no changes, stringing
    commands together, which can be a bit buggy. It's supported for people that
    can't use neovim RPC for some reason, like if you are using something with
    a VIM-like mode, like a consol with bindkeys -v set"""

    def run_command_mode_command(self, cmd):
        """Run a command in commandline mode using direct keyboard input."""
        v = VimMode()
        v.set_command_mode()
        v.insert_command_mode_command(cmd)

    def run_command_mode_command_exterm(self, cmd):
        """Run a command in commandline mode using direct keyboard input."""
        v = VimMode()
        v.set_command_mode()
        v.insert_command_mode_command(cmd)

    def run_normal_mode_command(self, cmd):
        actions.insert(cmd)


class VimRPC:
    """Implementation of functionality when RPC is available."""

    def __init__(self, nvrpc):
        self.nvrpc = nvrpc

    def exit_terminal_mode(self):
        """Leave terminal mode if inside."""
        v = VimMode()
        v.set_normal_mode_exterm()

    def is_insert_mode(self):
        v = VimMode()
        return v.is_insert_mode()

    def is_terminal_mode(self):
        v = VimMode()
        return v.is_terminal_mode()

    def run_command_mode_command(self, cmd):
        """Run a command in commandline mode using RPC.

        This requires some special casing because of support for direct key
        input. This means that certain commands will come in a newline
        character if the command is meant to be executed immediately, otherwise
        the intention is actually to let the user continue to interact after
        the input goes in, in which case we actually redirect back to the
        direct input from here.

        NOTE: This has some pretty significant quirks compared to is running
        commands with direct input. For instance if you have a command declared
        that maps to a function, like "command! :Files fzf#blah" you need a
        very specific invocation for this to work, which is `:exe ":Files"\n` .
        Since we want these comments to work generically across systems that
        have both RPC and not, unfortunately it means we need to rely on the
        more complicated invocation even for when were not using RPC, to avoid
        the duplication... there might be some better way to do this but I
        haven't figured it out yet.
        """
        if cmd[-1] != "\n":
            v = VimDirectInput()
            v.run_command_mode_command(cmd)
        else:
            try:
                # print(f"sending: {cmd}")
                self.nvrpc.nvim.command(cmd, async_=True)
            # I sometimes get this for things like needing a w! for write...
            except pynvim.api.common.NvimError as e:
                print("NvimError START")
                app.notify(subtitle=e)
                self.nvrpc.nvim.err_write(str(e))
                print(e)
                print("NvimError END")
            except Exception as e:
                app.notify(subtitle="Unknown Neovim API error. See talon log")
                print("NvimError START")
                print(e)
                print("NvimError END")

    def run_command_mode_command_exterm(self, cmd):
        """Exit terminal mode and run a command in commandline mode using RPC."""
        if self.is_terminal_mode():
            self.exit_terminal_mode()
        self.run_command_mode_command(cmd)

    def run_normal_mode_command(self, cmd):
        v = VimMode()
        cmd = cmd.replace('"', r"\"")
        v.nvrpc.nvim.command(f':exe "normal" "{cmd}"', async_=True)


class NoEpollSelectorSpam(logging.Filter):
    def filter(self, record):
        return not record.getMessage().endswith("DEBUG Using selector: EpollSelector")


logging.getLogger("asyncio").setLevel(logging.ERROR)
# loggers = logging.root.manager.loggerDict.keys()
# for l in loggers:
#     logger.addFilter(NoEpollSelectorSpam())


# XXX - this should be moved somewhere else
class VimAPI:
    """Abstraction of calls that go through RPC or not."""

    def __init__(self):
        self.api = self._get_api()
        self.nvrpc = None

    # socket
    def _get_api(self):
        """return a RPC or non-RPC API object"""
        # XXX - This is a hack but just trying to get rid of "DEBUG Using selector:
        # EpollSelector"
        # logging.getLogger("asyncio").setLevel(logging.WARNING)
        self.nvrpc = NeoVimRPC()
        if self.nvrpc.init_ok is True:
            return VimRPC(self.nvrpc)
        else:
            return VimDirectInput()

    def __del__(self):
        """Clean up the RPC Connection"""
        if self.nvrpc and self.nvrpc.init_ok is True:
            self.nvrpc.nvim.close()


# XXX - this should be updated to use feedkeys when RPC is available
# XXX - this should be made a singleton they gets registered when the window
# is focused
# XXX - this as a lot of code specific too VimDirectInput rather than VimRPC
# should be broken up were appropriate.
class VimMode:
    """Manage mode transitions with or without RPC"""

    # mode ids represent generic statusline mode() values. see :help mode()
    NORMAL = "normal"
    VISUAL = "visual"
    VISUAL_LINE = "visual_line"
    VISUAL_BLOCK = "visual_block"
    INSERT = "insert"
    TERMINAL = "terminal"
    COMMAND_LINE = "command_line"
    REPLACE = "replace"
    VISUAL_REPLACE = "visual_replace"

    # This is replicated from :help mode()
    vim_modes_new = {"NORMAL": {"mode": "n", "desc": "Normal"}}

    # XXX - incomplete see :help mode
    vim_modes = {
        "n": "Normal",
        "no": "N Operator Pending",
        "v": "Visual",
        "V": "V Line",
        "^V": "V-Block",
        "s": "Select",
        "S": "S·Line",
        "i": "Insert",
        "R": "Replace",
        "Rv": "V·Replace",
        "c": "Command",
        "cv": "Vim Ex",
        "ce": "Ex",
        "r": "Prompt",
        "rm": "More",
        "r?": "Confirm",
        "!": "Shell",
        "t": "Terminal",
    }

    vim_normal_mode_indicators = [
        "n",
        "no",
        "nov",
        "noV",
        "no^V",
        "niI",
        "niR",
        "niV",
        "nt",
    ]

    def __init__(self):
        # list of all vim instances talon is aware of
        self.vim_instances = []
        self.current_rpc = None
        self.nvrpc = NeoVimRPC()
        self.canceled_timeout = settings.get("user.vim_cancel_queued_commands_timeout")
        self.wait_mode_timeout = settings.get("user.vim_mode_change_timeout")
        self.debug_print("VimMode Initializing")

    def __del__(self):
        if self.nvrpc.init_ok is True:
            self.nvrpc.nvim.close()

    def debug_print(self, s):
        # XXX - need to override the logger
        if settings.get("user.vim_debug"):
            logger.debug(s)

    def is_normal_mode(self):
        return self.mode() in self.vim_normal_mode_indicators

    # XXX - move these too arrays like vim_normal_mode_indicators
    def is_visual_mode(self):
        return self.mode() in ["v", "V", "^V"]

    def is_insert_mode(self):
        return self.mode() in ["i", "ic", "ix"]

    def is_terminal_mode(self):
        return self.mode() == "t"

    def is_command_mode(self):
        return self.mode() == "c"

    def is_replace_mode(self):
        return self.mode() in ["R", "Rv", "Rx", "Rc"]

    # XXX - this can maybe get called by the parent class, since will only have
    # when the parent class is VimRPC
    def mode(self):
        if self.nvrpc.init_ok is True:
            mode = self.nvrpc.get_active_mode()["mode"]
            # self.debug_print(f"RPC reported mode: {mode}")
        else:
            title = ui.active_window().title
            mode = None
            if "MODE:" in title:
                mode = title.split("MODE:")[1].split(" ")[0]
                self.debug_print(f"Window title reported mode: {mode}")
                if mode not in self.vim_modes.keys():
                    return None

        return mode

    def current_mode_id(self):
        if self.is_normal_mode():
            return self.NORMAL
        elif self.is_visual_mode():
            return self.VISUAL
        elif self.is_insert_mode():
            return self.INSERT
        elif self.is_terminal_mode():
            return self.TERMINAL
        elif self.is_command_mode():
            return self.COMMAND_LINE

    def insert_text(self, text):
        if app.platform == "linux":
            actions.user.paste(text)
        else:
            actions.insert(text)

    def insert_command_mode_command(self, cmd):
        """prepare the command to be pasted into command mode"""
        # strip the new line to prevent it breaking on mac
        scmd = cmd.rstrip("\n")
        if scmd[0] == ":":
            self.insert_text(scmd[1:])
            # actions.user.paste(scmd[1:])
        else:
            self.insert_text(scmd)
            # actions.user.paste(scmd)
        if cmd[-1] == "\n":
            actions.key("enter")

    def set_normal_mode(self, auto=True):
        self.adjust_mode(self.NORMAL, auto=auto)

    def set_normal_mode_exterm(self):
        self.adjust_mode(self.NORMAL, escape_terminal=True)

    # XXX - revisit auto, maybe have separate method version or something
    def set_normal_mode_np(self, auto=True):
        self.adjust_mode(self.NORMAL, no_preserve=True, auto=auto)

    def set_visual_mode(self):
        self.adjust_mode(self.VISUAL)

    def set_visual_mode_np(self):
        self.adjust_mode(self.VISUAL, no_preserve=True)

    def set_visual_line_mode(self):
        self.adjust_mode(self.VISUAL_LINE)

    def set_visual_block_mode(self):
        self.adjust_mode(self.VISUAL_BLOCK)

    def set_insert_mode(self):
        self.adjust_mode(self.INSERT)

    def set_terminal_mode(self):
        self.adjust_mode(self.TERMINAL)

    def set_command_mode(self):
        self.adjust_mode(self.COMMAND_LINE)

    def set_command_mode_exterm(self):
        self.adjust_mode(self.COMMAND_LINE, escape_terminal=True)

    def set_replace_mode(self):
        self.adjust_mode(self.REPLACE)

    def set_visual_replace_mode(self):
        self.adjust_mode(self.VISUAL_REPLACE)

    def set_any_motion_mode(self):
        self.adjust_mode([self.NORMAL, self.VISUAL])

    # XXX - this should accept additional modes, like visual block
    def set_any_motion_mode_exterm(self):
        self.adjust_mode([self.NORMAL, self.VISUAL], escape_terminal=True)

    def set_any_motion_mode_np(self):
        self.adjust_mode(self.NORMAL, no_preserve=True)

    def adjust_mode(
        self, valid_mode_ids, no_preserve=False, escape_terminal=False, auto=True
    ):
        if auto is True and settings.get("user.vim_adjust_modes") == 0:
            return

        cur = self.current_mode_id()
        if type(valid_mode_ids) != list:
            valid_mode_ids = [valid_mode_ids]
        if cur not in valid_mode_ids:
            self.debug_print(
                f"Want to adjust from from '{cur}' to one of '{valid_mode_ids}'"
            )
            # Just favor the first mode match
            self.set_mode(
                valid_mode_ids[0],
                no_preserve=no_preserve,
                escape_terminal=escape_terminal,
            )
            # Trigger / untrigger mode-related talon grammars
            self.set_mode_tag(valid_mode_ids[0])

    # Often I will say `delete line` and it will trigger `@delete` and `@nine`.
    # This then keys 9. I then say `undo` to fix the bad delete, which does 9
    # undos. Chaos ensues... this seeks to fix that
    def cancel_queued_commands(self):
        if (
            settings.get("user.vim_cancel_queued_commands") == 1
            and self.is_normal_mode()
        ):
            # print("escaping queued cmd")
            actions.key("escape")
            timeout = settings.get("user.vim_cancel_queued_commands_timeout")
            time.sleep(timeout)

    def wait_mode_change(self, wanted):
        check_count = 0
        max_check_count = 20
        if self.nvrpc.init_ok:
            active_mode = self.nvrpc.get_active_mode()["mode"]
            while wanted != active_mode:
                # XXX - There's probably a cleaner way to do this, but there's
                # a lot of normal modes which we don't seem to match on, but
                # technically should
                if wanted == "n" and active_mode in self.vim_normal_mode_indicators:
                    return True

                self.debug_print(
                    f"Wanted mode: {wanted} vs Current mode: {active_mode}"
                )
                # XXX - for wait value should be configurable
                time.sleep(0.020)
                # try to force redraw to prevent weird infinite loops
                self.nvrpc.nvim.command("redraw")
                check_count += 1
                if check_count > max_check_count:
                    # prevent occasional infinite loops stalling talon
                    self.debug_print("early break to avoid infinite loop")
                    return False
                active_mode = self.nvrpc.get_active_mode()["mode"]

            return True
        else:
            time.sleep(self.wait_mode_timeout)
            return True

    @classmethod
    # We don't want unnecessarily only call this from set_mode() is the user
    # might change the mode of vim manually or speaking keys, but we still want
    # the context specific grammars to match.
    # TODO: figure out if this makes sense in addition to win.title matching I
    # already do. I think it does make sense for cases of overriding certain
    # default actions like home/end
    def set_mode_tag(self, mode):
        global mode_tag_list
        global ctx

        # print(ctx.tags)

    # NOTE: querying certain modes is broken (^V mode undetected)
    # Setting mode with RPC is impossible, which makes sense because it would
    # break things like macro recording/replaying. So we use keyboard
    # combinations
    def set_mode(self, wanted_mode, no_preserve=False, escape_terminal=False):
        current_mode = self.mode()
        if current_mode == wanted_mode or (
            self.is_terminal_mode() and wanted_mode == self.INSERT
        ):
            return

        self.debug_print(f"Setting mode to {wanted_mode} from {current_mode}")
        # enter normal mode where necessary
        # XXX - need to handle normal mode in Command Line window, we need to
        # be able to escape from it
        # XXX - also have a lot of special case modes (see :help mode) that we
        # probably want to be able to break out of, instead of just doing more
        # fuzzy matching of the mode (ex: `no`, `rm`, `!`, etc)
        if self.is_terminal_mode():
            if (
                settings.get("user.vim_escape_terminal_mode") is True
                or escape_terminal is True
            ):
                # break out of terminal mode
                actions.key("ctrl-\\")
                actions.key("ctrl-n")

                # XXX - Not sure why I have to sleep after this, but otherwise
                # sit sometimes blocks for way longer then it should
                time.sleep(0.05)

                self.wait_mode_change("n")
            else:
                # Imagine you have a vim terminal and inside you're running a
                # terminal that is using vim mode rather than emacs mode. This
                # means you will want to be able to use some amount of vim
                # commands to edit the shells command line itself without
                # actually being inside the encapsulating vim instance.
                # The use of escape here tries to compensate for those
                # scenerios, where you won't break into the encapsulating vim
                # instance. Needs to be tested. If you don't like this, you can
                # set vim_escape_terminal_mode to 1
                actions.key("escape")
                # NOTE: do not wait on mode change here, as we
                # cannot detect it
        elif self.is_insert_mode():
            # XXX - this might need to be a or for no_preserve and
            # settings.get?
            if (
                wanted_mode == self.NORMAL
                and no_preserve is False
                and settings.get("user.vim_preserve_insert_mode") >= 1
            ):
                if settings.get("user.vim_mode_switch_moves_cursor") == 0:
                    actions.key("ctrl-\\")
                actions.key("ctrl-o")
                # XXX - Same oddity as terminal escape above
                time.sleep(0.05)
                self.wait_mode_change("niI")
            else:
                # Presses right because entering normal mode via escape puts
                # the cursor back one position, otherwise misaligns on words.
                # Exception is `2 delete big-back` from INSERT mode.
                actions.key("right")
                actions.key("escape")
                time.sleep(0.05)
                self.wait_mode_change("n")
        elif self.is_visual_mode() or self.is_command_mode() or self.is_replace_mode():
            actions.key("escape")
            time.sleep(0.05)
            self.wait_mode_change("n")
        elif self.is_normal_mode() and wanted_mode == self.COMMAND_LINE:
            # We explicitly escape even if normal mode, to cancel any queued
            # commands that might affect our command. For instance, accidental
            # number queueing followed by :w, etc
            actions.key("escape")
            time.sleep(0.05)
            time.sleep(self.canceled_timeout)
            self.wait_mode_change("n")

        # switch to explicit mode if necessary. we will be normal mode here
        if wanted_mode == self.INSERT or wanted_mode == self.TERMINAL:
            actions.key("i")
        # or just let the original 'mode' command run from this point
        elif wanted_mode == self.VISUAL:
            # first we cancel queued normal commands that might mess with 'v'
            # ex: normal mode press 5, then press v to switch to visual
            actions.key("escape")
            actions.key("v")
        elif wanted_mode == self.VISUAL_LINE:
            # first we cancel queued normal commands that might mess with 'v'
            # ex: normal mode press 5, then press v to switch to visual
            actions.key("escape")
            actions.key("V")
        elif wanted_mode == self.VISUAL_BLOCK:
            # first we cancel queued normal commands that might mess with 'v'
            # ex: normal mode press 5, then press v to switch to visual
            actions.key("escape")
            actions.key("ctrl-v")
        elif wanted_mode == self.COMMAND_LINE:
            actions.key(":")
            self.wait_mode_change("c")
            self.debug_print("Detected COMMAND mode change")
        elif wanted_mode == self.REPLACE:
            actions.key("R")
        elif wanted_mode == self.VISUAL_REPLACE:
            actions.key("g R")

        # Here we assume we are now in some normalized state:
        # need to make the notify command configurable
        if settings.get("user.vim_notify_mode_changes") >= 1:
            self.notify_mode_change(wanted_mode)

    def notify_mode_change(self, mode):
        """Function to be customized by talon user to determine how they want
        notifications on mode changes"""
