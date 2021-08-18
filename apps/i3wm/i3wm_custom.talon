tag: user.i3wm
-

# Custom stuff relying on i3wm commands


# fix an error related to the layout of vim terminals inside i3 also helps with
# split balance issues inside of vim
wiggle:
    key(super-f)
    sleep(500ms)
    key(super-f)


orwell me:
    key(super-0)
    sleep(1000ms)
    edit.copy()
    key(super-u)
    sleep(1000ms)
    edit.paste()
    key(enter)


#reveal:
#    key(super-0)
#    sleep(1000ms)
#    key(ctrl-u)
#    key(super-u)
#    sleep(1000ms)
#    edit.paste()
#    key(enter)


new scratch shell:
    user.system_command_nb("/home/aa/scripts/workflow/scratch_shell.sh")

pulse restart:
    key(super-enter)
    sleep(1000ms)
    insert("pulseaudio -k && pulseaudio --start\n")
    key(super-shift-q)
