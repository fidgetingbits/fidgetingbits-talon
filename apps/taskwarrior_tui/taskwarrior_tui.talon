tag: user.taskwarrior_tui
-

# The filter tasks section supports a minimal readline interface
# See `readline-like functionality` @ https://github.com/kdheepak/taskwarrior-tui
tag(): user.readline

# Keybindings taken from:
# https://github.com/kdheepak/taskwarrior-tui/blob/master/KEYBINDINGS.md
task list: key(esc)
view next: key(])
view list: key([)

## task view
task (search|filter): key(/)
task add: key(a)
task done: key(d)
task edit: key(e)

task log: key(l)
task modify: key(m)
quit: key(q)
task (start|stop): key(s)
task undo: key(u)
task delete: key(x)
task info: key(z)
task annotate: key(A)
task shell command: key(!)
task context: key(c)
task help: key(?)

## calendar view
next year: key(j)
last year: key(k)
next decade: key(J)
last decade: key(K)


# helpers for filters
