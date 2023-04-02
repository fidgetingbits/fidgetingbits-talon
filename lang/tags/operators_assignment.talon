tag: user.code_operators_assignment
-
tag(): user.code_operators_math
tag(): user.code_operators_bitwise

# assignment
(op | put) (equals | assign): user.code_operator_assignment()

# combined computation and assignment
(op | put) (minus | subtract) equals: user.code_operator_subtraction_assignment()
(op | put) (plus | add) equals: user.code_operator_addition_assignment()
(op | put) (times | multiply) equals: user.code_operator_multiplication_assignment()
(op | put) divide equals: user.code_operator_division_assignment()
(op | put) mod equals: user.code_operator_modulo_assignment()
[(op | put)] increment: user.code_operator_increment()
[(op | put)] decrement: user.code_operator_decrement()

#bitwise operators
[(op | put)] bit [wise] and equals: user.code_operator_bitwise_and_assignment()
[(op | put)] bit [wise] or equals: user.code_operator_bitwise_or_assignment()
(op | put| logical | bitwise) (ex | exclusive) or equals:
    user.code_operator_bitwise_exclusive_or_assignment()
[(op | put| logical | bitwise)] (left shift | shift left) equals:
    user.code_operator_bitwise_left_shift_assignment()
[(op | put| logical | bitwise)] (right shift | shift right) equals:
    user.code_operator_bitwise_right_shift_assignment()
