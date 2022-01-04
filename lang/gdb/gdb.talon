mode: user.gdb
mode: user.auto_lang 
and code.language: gdb
-
tag(): user.code_imperative

# XXX - this might be overkill since the split of operators, and right now none
# of these are implemented except comments I think
tag(): user.code_comment_line
tag(): user.code_functions
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_math
