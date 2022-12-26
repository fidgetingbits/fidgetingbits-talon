from talon import Context, actions

ctx = Context()
ctx.matches = r"""
user: user.codeql
"""

ctx.lists["user.code_libraries"] = {
    "see pee pee": "cpp",
    "see plus plus": "cpp",
    "dataflow": "import semmle.code.cpp.dataflow.DataFlow",
    "overflow": "import semmle.code.cpp.security.Overflow",
}

# Note that these follow this standard naming convention for certain
# objects, for instance FunctionCall
ctx.lists["user.code_functions"] = {
    "exists": "exists",
    "target has name": "fc.getTarget().hasName()",
    "get target": "fc.getTarget()",
}


@ctx.action_class("user")
class UserActions:
    ##
    # code_data_bool
    ##
    def code_insert_true():
        actions.insert("true")

    def code_insert_false():
        actions.insert("false")

    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + f"({selection})"
        else:
            text = text + "()"

        actions.user.paste(text)
        actions.edit.left

    ##
    # code_data_null
    ##
    def code_insert_null():
        actions.insert("none")

    def code_insert_is_null():
        actions.insert("== none")

    def code_insert_is_not_null():
        actions.insert("!= none")

    ##
    # code_functions_gui
    ##

    ##
    # code_libraries
    ##
    def code_import():
        actions.insert("import ")

    ##
    # code_libraries_gui
    ##
    def code_insert_library(text: str, selection: str):
        actions.insert(f"import {selection} ")

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
        actions.insert(" != ")

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
