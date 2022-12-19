win.title: /TERM:pwndbg/
win.title: /TERM:gdb/
-

go last prompt:
    user.vim_any_motion_mode_exterm("0?(gdb)\\|pwndbg>\n")
    user.vim_any_motion_mode("0f l")

go next prompt:
    user.vim_any_motion_mode_exterm("0/(gdb)\\|pwndbg>\n")
    user.vim_any_motion_mode("0f l")

# XXX - add something for highlighting and entire command that was just
# executed
