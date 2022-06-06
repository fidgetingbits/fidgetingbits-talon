win.title: /TERM:pwndbg/
win.title: /TERM:gdb/
-

go last prompt: 
    user.vim_command_mode_exterm("0?(gdb)\\|pwndbg>\n")
    user.vim_motion_mode("0f)2l")

go next prompt: 
    user.vim_command_mode_exterm("0/(gdb)\\|pwndbg>\n")
    user.vim_motion_mode("0f)2l")

# XXX - add something for highlighting and entire command that was just
# executed
