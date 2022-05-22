win.title: /TERM:pwndbg/
win.title: /TERM:gdb/
-

go last prompt: 
    user.vim_command_mode_exterm("?\(gdb\)\|pwndbg>\n")
    user.vim_normal_mode("0f)2l")

go next prompt: 
    user.vim_command_mode_exterm("/\(gdb\)\|pwndbg>\n")
    user.vim_normal_mode("0f)2l")
