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

ctx.lists["user.code_functions"] = {
    "string len": "strlen",
    "get line": "getline",
    "set line": "setline",
    "length": "len",
    "eye pairs": "ipairs",
}

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
        actions.auto_insert("if  then\n\nend")
        actions.key("up:2")

    def code_state_else_if():
        actions.auto_insert("elseif  then\n")
        actions.key("up:1 right:3")

    def code_state_else():
        actions.auto_insert("else\n")

    def code_state_do():
        actions.auto_insert("repeat\n\nuntil ")
        actions.key("up:1")

    def code_state_for():
        actions.auto_insert("for  do\n\nend")
        actions.key("up:2 right:1")

    def code_state_go_to():
        actions.auto_insert("goto ")

    def code_state_while():
        actions.auto_insert("while  do\n\nend")
        actions.key("up:2 right:3")

    def code_state_return():
        actions.auto_insert("return ")

    def code_state_break():
        actions.auto_insert("break ")

    # Assumes a ::continue:: label
    def code_state_continue():
        actions.auto_insert("goto continue")

    def code_try_catch():
        actions.auto_insert("pcall()")
        actions.key("left")

    ##
    # code_comment_line
    ##
    def code_comment_line_prefix():
        actions.auto_insert("--")

    ##
    # code_comment_block
    ##
    def code_comment_block():
        actions.insert("--[[\n\n--]]")
        actions.edit.up()

    def code_comment_block_prefix():
        actions.auto_insert("--[[")

    def code_comment_block_suffix():
        actions.auto_insert("--]]")

    ##
    # code_data_bool
    ##
    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    ##
    # code_data_null
    ##
    def code_insert_null():
        actions.auto_insert("nil")

    def code_insert_is_null():
        actions.auto_insert("== nil")

    def code_insert_is_not_null():
        actions.auto_insert("~= nil")

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

        actions.auto_insert("\n\nend")
        actions.key("up:2")
        actions.user.code_insert_function(result, None)


    def code_public_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.auto_insert("\n\nend")
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

    def code_import_local():
        # XXX - Not sure about this yet
        pass

    ##
    # code_libraries_gui
    ##
    def code_insert_library(text: str, selection: str):
        actions.auto_insert(f"local {selection} = require('{selection}')")

    ##
    # code_operators_array
    ##
    def code_operator_subscript():
        actions.auto_insert('[]')
        actions.key('left')

    ##
    # code_operators_assignment
    ##
    def code_operator_assignment():
        actions.auto_insert(" = ")

    ##
    # code_operators_math
    ##
    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    # action(user.code_operator_exponent): " ** "
    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" ~= ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" and ")

    def code_operator_or():
        actions.auto_insert(" or ")

    # code_operators_bitwise
    # NOTE: < 5.3 assumes Lua BitOp usage
    #       > 5.2 assumes native bitwise operators
    # TODO: Possibly add settings to define which library to use, as 5.2
    # includes bit32. Neovim uses luajit, which uses Lua BitOp
    def code_operator_bitwise_and():
        if settings.get("user.lua_version") > 5.2:
            actions.auto_insert(" & ")
        else:
            actions.auto_insert(" bit.band() ")

    def code_operator_bitwise_or():
        if settings.get("user.lua_version") > 5.2:
            actions.auto_insert(" | ")
        else:
            actions.auto_insert(" bit.bor() ")

    def code_operator_bitwise_exclusive_or():
        if settings.get("user.lua_version") > 5.2:
            actions.auto_insert(" ~ ")
        else:
            actions.auto_insert(" bit.xor() ")

    def code_operator_bitwise_left_shift():
        if settings.get("user.lua_version") > 5.2:
            actions.auto_insert(" << ")
        else:
            actions.auto_insert(" bit.lshift() ")

    def code_operator_bitwise_right_shift():
        if settings.get("user.lua_version") > 5.2:
            actions.auto_insert(" >> ")
        else:
            actions.auto_insert(" bit.rshift() ")

    # non-tag related actions
