from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.auto_lang
and code.language: lua
"""

mod.setting(
    "lua_version",
    type=float,
    default=5.1,
    desc="The default lua version to use. Dictates certain operators",
)

# XXX - this should be updatable with other modules like nse, neovim, base
# off some tags
ctx.lists["user.code_functions"] = {
    "to number": "tonumber",
    "eye pairs": "ipairs",
    "print": "print",
    "print F": "printf",
    "type": "type",
    "assert": "assert",
    "get meta table": "getmetatable",
    "set meta table": "setmetatable",

    # io
    "eye oh write": "io.write",
    "eye oh read": "io.read",
    "eye oh open": "io.open",

    # string
    "format": "string.format",
    "string G find": "string.gfind",
    "string find": "string.strfind",
    "string len": "string.strlen",
    "string upper": "string.strupper",
    "string lower": "string.strlower",
    "string sub": "string.strsub",
    "string G sub": "string.gsub",
    "string match": "string.match",
    "string G match": "string.gmatch",

    # table
    "table unpack": "table.unpack",
    "table insert": "table.insert",
    "tabel get N": "table.getn",
    "tabel sort": "table.sort",

    # math
    "math max": "math.max",

    # json
    "jason parse": "json.parse",

    # http
    "web get": "http.get",

    # os
    "O S date": "os.date",
    "O S time": "os.time",
    "O S clock": "os.clock",
    "O S rename": "os.rename",
    "O S remove": "os.remove",
    "O S getenv": "os.getenv",
    "O S execute": "os.execute",
}

# XXX - it would be nice to correlate what we import these library is as to the
# function calls. Ex: if someone does `local j = require("json")` then when we
# call in too json libraries, we would prefix it with `j.parse()`
ctx.lists["user.code_libraries"] = {
    "bit": "bit",
    "I O": "io",
    "string": "string",
    "U T F eight": "utf8",
    "table": "table",
    "math": "math",
    "O S": "os",
    "debug": "debug",
    "L F S": "lfs",
    "socket": "socket",
    "H T T P": "http",
    "web": "http",
    "jason": "json",

    # Nmap Scripting Engine
    # XXX - They should go in its own extension for .nse files
    "short port": "shortport",
}


@mod.capture(rule="{self.lua_functions}")
def lua_functions(m) -> str:
    "Returns a string"
    return m.lua_functions


@ctx.action_class("user")
class UserActions:
    # tag-related actions listed first, indicated by comment. corresponds to
    # the tag(): user.code_imperative style declaration in the language .talon
    # file

    ##
    # code_imperative
    ##
    def code_state_if():
        actions.insert("if  then\n\nend")
        actions.key("up:2")

    def code_state_else_if():
        actions.insert("elseif  then\n")
        actions.key("up:1 right:3")

    def code_state_else():
        actions.insert("else\n")

    def code_state_do():
        actions.insert("repeat\n\nuntil ")
        actions.key("up:1")

    def code_state_for():
        actions.insert("for  do\n\nend")
        actions.key("up:2 right:1")

    def code_state_go_to():
        actions.insert("goto ")

    def code_state_while():
        actions.insert("while  do\n\nend")
        actions.key("up:2 right:3")

    def code_state_return():
        actions.insert("return ")

    def code_break():
        actions.insert("break ")

    # Assumes a ::continue:: label
    def code_state_continue():
        actions.insert("goto continue")

    def code_try_catch():
        actions.insert("pcall()")
        actions.key("left")

    ##
    # code_comment_line
    ##
    def code_comment_line_prefix():
        actions.insert("--")

    ##
    # code_comment_block
    ##
    def code_comment_block():
        actions.insert("--[[\n\n--]]")
        actions.edit.up()

    def code_comment_block_prefix():
        actions.insert("--[[")

    def code_comment_block_suffix():
        actions.insert("--]]")

    ##
    # code_data_bool
    ##
    def code_insert_true():
        actions.insert("true")

    def code_insert_false():
        actions.insert("false")

    ##
    # code_data_null
    ##
    def code_insert_null():
        actions.insert("nil")

    def code_insert_is_null():
        actions.insert("== nil")

    def code_insert_is_not_null():
        actions.insert("~= nil")

    ##
    # code_functions
    ##
    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "local function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.insert("\n\nend")
        actions.key("up:2")
        actions.user.code_insert_function(result, None)


    def code_public_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.insert("\n\nend")
        actions.key("up:2")
        actions.user.code_insert_function(result, None)

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left()

    ##
    # code_functions_gui
    ##

    ##
    # code_libraries
    ##
    def code_import():
        actions.user.insert_cursor("local [|] = require('')")

    ##
    # code_libraries_gui
    ##
    def code_insert_library(text: str, selection: str):
        actions.insert(f"local {selection} = require('{selection}')")

    ##
    # code_operators_array
    ##
    def code_operator_subscript():
        actions.insert('[]')
        actions.key('left')

    ##
    # code_operators_assignment
    ##
    def code_operator_assignment():
        actions.insert(" = ")

    ##
    # code_operators_math
    ##
    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_multiplication():
        actions.insert(" * ")

    # action(user.code_operator_exponent): " ** "
    def code_operator_division():
        actions.insert(" / ")

    def code_operator_modulo():
        actions.insert(" % ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" ~= ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    def code_operator_and():
        actions.insert(" and ")

    def code_operator_or():
        actions.insert(" or ")

    ###
    # code_operators_bitwise
    ###

    # NOTE: < 5.3 assumes Lua BitOp usage
    #       > 5.2 assumes native bitwise operators
    # TODO: Possibly add settings to define which library to use, as 5.2
    # includes bit32. Neovim uses luajit, which uses Lua BitOp
    def code_operator_bitwise_and():
        if settings.get("user.lua_version") > 5.2:
            actions.insert(" & ")
        else:
            actions.insert(" bit.band() ")

    def code_operator_bitwise_or():
        if settings.get("user.lua_version") > 5.2:
            actions.insert(" | ")
        else:
            actions.insert(" bit.bor() ")

    def code_operator_bitwise_exclusive_or():
        if settings.get("user.lua_version") > 5.2:
            actions.insert(" ~ ")
        else:
            actions.insert(" bit.xor() ")

    def code_operator_bitwise_left_shift():
        if settings.get("user.lua_version") > 5.2:
            actions.insert(" << ")
        else:
            actions.insert(" bit.lshift() ")

    def code_operator_bitwise_right_shift():
        if settings.get("user.lua_version") > 5.2:
            actions.insert(" >> ")
        else:
            actions.insert(" bit.rshift() ")

    # non-tag related actions
