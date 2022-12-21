# this file defines commands that are shared across all applications that will
# be running inside of a terminal, like ctrl-c to cancel running something.
# examples would be something like htop, gdb, etc
tag: user.terminal_program
-

cancel [that]: key("ctrl-c")
