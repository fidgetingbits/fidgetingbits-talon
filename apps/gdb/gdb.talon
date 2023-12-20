tag: user.gdb
-
# See lang/gdbscript.talon for the language specific commands. Generally anything that could be added during
# scripting that's not automatically run should be put there
tag(): user.debugger
tag(): user.terminal_program
tag(): user.readline

tag(): user.code_imperative
tag(): user.code_comment_line
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math
tag(): user.code_operators_pointer

# XXX - this would be better to be managed with settings maybe
# optional generic debugger plugins
# specify which heap plugin you're using
# similar to the architecture
# userland heap
#tag(): user.libptmalloc
#tag(): user.libdlmalloc
#tag(): user.libheap
tag(): user.muslheap

# linux kernel
# XXX These should be based off a list in the title set by the gdb script
# tag(): user.gdb_vmlinux
# tag(): user.libslub

tag(): user.retsync

until <number>: "until {number}"

force clear all break points:
    insert("d br\n")
    insert("y\n")
break [on] clip:
    insert("break ")
    edit.paste()
    key(enter)

clear screen: "shell clear\n"
# information
list [source]: "list\n"
list clip:
    insert("list ")
    edit.paste()
    key(enter)
list (base|P C): "list $pc\n"


print hex {user.registers}:
    insert("p/x ${user.registers}\n")

print string: "x/s "
print (bits|binary): "p/t "

print casted struck:
    user.insert_cursor("p/x *(struct [|] *)")

# symbols
symbol refresh: "sharedlibrary\n"

# execution
source file: "source \t\t"

# displays
# XXX - move thee invoke command into a python script
(list|show|info) display: "info display\n"
display (assembly line|program counter|P C)$: "display /i $pc\n"
enable display <number_small>: "enable display {number_small}\n"
disable display <number_small>: "disable display {number_small}\n"
undisplay: "undisplay\n"

# variables
(list|show|info) local: "info local "
(list|show|info) local typed: "info local -t "
(list|show|info) variable: "info variable "
(list|show|info) variable typed: "info variable -t "
(list|show|info) locals: "info local\n"
(list|show|info) variables: "info variables\n"
(list|show|info) (args|arguments): "info args\n"


# threads
(thread list|info threads): "info threads\n"
thread switch <number_small>: "thread {number_small}\n"
thread (find|search): "thread find "
thread show: "thread\n"
thread help: "help thread\n"
# run command across all threads
thread do: "thread apply all "
thread local storage: "p/x *(tcbhead_t*) $fs_base\n"
thread stack guard: "p/x (*(tcbhead_t*) $fs_base)->stack_guard"
thread pointer guard: "p/x (*(tcbhead_t*) $fs_base)->pointer_guard"

frame info <number_small>: "frame info {number_small}\n"

# inferiors
info inferiors: "info inferiors\n"
inferior <number_small>$: "inferior {number_small}\n"
inferior: "inferior "
resume from main:
    insert("inferior 1\n")
    insert("c\n")
resume [from] (inf|inferior) <number_small>$:
    insert("inferior {number_small}\n")
    insert("c\n")

# arguments
set args: "set args "

info source: "info source\n"
info signal: "info signal\n"
info process: "info proc\n"
handle signal <user.signal>: "handle {signal} "
signal <user.signal>: "signal {signal} "
[remote] process list: "info os processes\n"

show follow (fork|forks) [mode]: "show follow-fork-mode\n"
[set] follow (fork|forks) [mode] child: "set follow-fork-mode child\n"
[set] follow (fork|forks) [mode] parent: "set follow-fork-mode parent\n"

show detach on fork: "show detach-on-fork\n"
set detach on fork: "set detach-on-fork on\n"
unset detach on fork: "set detach-on-fork off\n"

set logging on: "set logging on"
set logging off: "set logging off"
set logging file: "set logging file "
show logging: "show logging\n"

set history size: "set history size "
set history size unlimited: "set history size unlimited\n"
show history size: "show history size\n"

(list libraries|info library): "info sharedlibrary\n"

info file: "info file\n"


set system root: "set sysroot "
show system root: "show sysroot\n"

show substitute path: "show substitute-path\n"

show list size: "show listsize\n"
set list size <number_small>: "set listsize {number_small}\n"

#set remote target: "target extended-remote :9999\n"
[set] target remote default: "target remote :1234\n"
[set] target remote <number>: "target remote :{number}\n"
[set] target remote: "target remote "

print (struct|structure) size clip:
    insert("p/x sizeof(")
    edit.paste()
    key(")")
    key(enter)

unset print elements:
    insert("set print elements 0\n")

unset print repeats:
    insert("set print repeats 0\n")

watch list: "info watch\n"
watch read: "rwatch *"

file show: "info line\n"

# XXX - this should use default for matter
get var <user.word>: "${word}"

# Convenience for repeated commands
hex stump saved: "x/50gx $ADDRESS\n"
save address clip:
    insert("set $ADDRESS=")
    edit.paste()
    key(enter)

define offset of: "macro define offsetof(t, f) &((t *) 0)->f\n"

# XXX - this needs to be ingrated as a language, and we need to break out using
# debugger from the language parts
put python continue: 'python gdb.execute("continue")\n'
put commands: "commands"
put end: "end"
put break: "break"
put set: "set"
func stir equal: "$_streq()"
attach <number>: "attach {number}\n"
break list hidden: "maint info breakpoints\n"

show configuration: "show configuration\n"
info target: "info target\n"
info program: "info program\n"

rerun:
    key(ctrl-r)
rerun <user.text>:
    key(ctrl-r)
    insert(text)
rerun last:
    key(up)
    key(enter)

set debug enable on: "set debuginfod enable on\n"
set debug enable off: "set debuginfod enable off\n"
