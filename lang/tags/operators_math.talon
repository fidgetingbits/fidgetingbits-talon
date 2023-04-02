tag: user.code_operators_math
-

# math operators
(op | put) (minus | subtract): user.code_operator_subtraction()
(op | put) (plus | add): user.code_operator_addition()
(op | put) (times | multiply): user.code_operator_multiplication()
(op | put) divide: user.code_operator_division()
(op | put) mod: user.code_operator_modulo()
(op | put) ((power | exponent) | to the power [of]): user.code_operator_exponent()

# comparison operators
(op | put | is) equal: user.code_operator_equal()
(op | put | is) not equal: user.code_operator_not_equal()
(op | put | is) (greater | more): user.code_operator_greater_than()
(op | put | is) (less | below) [than]: user.code_operator_less_than()
(op | put | is) greater [than] or equal: user.code_operator_greater_than_or_equal_to()
(op | put | is) less [than] or equal: user.code_operator_less_than_or_equal_to()

# logical operators
(op | put | logical) and: user.code_operator_and()
(op | put | logical) or: user.code_operator_or()

# set operators
(op | put | is) in: user.code_operator_in()
(op | put | is) not in: user.code_operator_not_in()

# TODO: This operator should either be abstracted into a function or removed.
(op | put | pad) colon: " : "
