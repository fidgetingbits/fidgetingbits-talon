from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.gdb
"""

ctx.lists["user.code_common_function"] = {"print": "printf"}


@ctx.action_class("user")
class UserActions:
    ###
    # code_operators_pointers
    ###
    def code_operator_indirection():
        actions.insert("*")

    def code_operator_address_of():
        actions.insert("&")

    def code_operator_structure_dereference():
        actions.insert("->")

    ###
    # code_operators_array
    ###
    def code_operator_subscript():
        actions.insert("[]")
        actions.key("left")

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

    def code_operator_subtraction_assignment():
        actions.insert(" -= ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_addition_assignment():
        actions.insert(" += ")

    def code_operator_increment():
        actions.insert("++")

    def code_operator_decrement():
        actions.insert("--")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_multiplication_assignment():
        actions.insert(" *= ")

    # action(user.code_operator_exponent): " ** "
    def code_operator_division():
        actions.insert(" / ")

    def code_operator_division_assignment():
        actions.insert(" /= ")

    def code_operator_modulo():
        actions.insert(" % ")

    def code_operator_modulo_assignment():
        actions.insert(" %= ")

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
        actions.insert(" && ")

    def code_operator_or():
        actions.insert(" || ")

    ##
    # code_operators_bitwise
    ##
    def code_operator_bitwise_and():
        actions.insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.insert(" &= ")

    def code_operator_bitwise_or():
        actions.insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.insert(" >>= ")

    def code_insert_null():
        actions.insert("NULL")

    def code_insert_is_null():
        actions.insert(" == NULL ")

    def code_insert_is_not_null():
        actions.insert(" != NULL")

    def code_comment_line_prefix():
        actions.auto_insert("# ")
