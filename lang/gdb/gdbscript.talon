code.language: gdb
and not tag: user.gdb

tag: user.gdb
and not code.language: gdb

code.language: gdb
and tag: user.gdb
-
# For commands to run well actually in the debugger, see gdb.talon
tag(): user.code_imperative

# XXX - this might be overkill since the split of operators, and right now none
# of these are implemented except comments I think
tag(): user.code_comment_line
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_math

# general
put set: "set"
func stir equal: "$_streq()"
set system root: "set sysroot "
put run: "run"

# breakpoints
put commands: "commands"
put end: "end"
put break: "break"

# printing
print: "p "
print string: "x/s "
print (bits | binary): "p/t "
print (var | variable) <user.text>:
    insert("p ")
    insert(user.formatted_text(text, "snake"))
(print hex | funk print): "p/x "
print hex (var | variable) <user.text>:
    insert("p/x ")
    insert(user.formatted_text(text, "snake"))
print hex {user.registers}: insert("p/x ${user.registers}\n")

# displays
display source: "display "

# arguments
set args: "set args "

# signals
handle signal <user.signal>: "handle {signal} "
signal <user.signal>: "signal {signal} "

# source code
set substitute path: "set substitute-path "
unset substitute path: "unset substitute-path "

# files
set remote file: "set remote exec-file "

# symbol files
add symbol file: "add-symbol-file "
set system root: "set sysroot "

# printing
print size of: user.insert_between("p/x sizeof(", ")")

print (struct | structure) size: user.insert_between("p/x sizeof(struct ", ")")

print type: insert("ptype ")

# variables
set var [<user.word>]:
    insert("set $")
    # XXX - this should be formatter for the language...
    insert(word or "")
    # XXX - we should support a second word for the assignment

# titles
# Useful to set tags if you didn't user script file
set title: user.insert_between('shell echo -n -e "\\033]0;', '\\007"')

set title G D B: insert('shell echo -n -e "\\033]0;gdb\\007"\n')

set title pone: insert('shell echo -n -e "\\033]0;pwndbg\\007"\n')

set title jeff: insert('shell echo -n -e "\\033]0;gef\\007"\n')

# typecasting
# maybe we should make these generic across gdb and C
# XXX - we should make these expressible to gdb
# Ex. (int *)
cast to <user.c_cast>: "{c_cast}"
basic cast to <user.c_basic_cast>: "{c_basic_cast}"
standard cast to <user.c_stdint_cast>: "{c_stdint_cast}"
[put] type <user.c_types>: "{c_types}"
<user.c_pointers>: "{c_pointers}"
<user.c_signed>: "{c_signed}"
basic <user.c_basic_types>: "{c_basic_types}"
standard <user.c_stdint_types>: "{c_stdint_types}"

# macros
define macro: "macro define "

# logging
set logging on: "set logging on"
set logging off: "set logging off"
set logging file: "set logging file "
