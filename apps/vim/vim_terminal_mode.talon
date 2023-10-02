win.title: /VIM MODE:t/
-

tag(): user.vim_terminal

normal [mode]: key(ctrl-\ ctrl-n)
pop (terminal | term): key(ctrl-\ ctrl-n)
poppy: key(ctrl-\ ctrl-n)

# pop terminal mode and scroll up once, from this point onward you can scroll
# like normal
scroll up: key(ctrl-\ ctrl-n ctrl-b)

# this causes exclusive terminal windows to exit without requiring key press or
# dropping to a new empty buffer
exit terminal:
    key(ctrl-\)
    key(ctrl-n)
    insert("ZQ")

bring line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("y$")
    user.vim_set_insert_mode()
    edit.paste()
    key(space)

bring line fuzzy <user.text>:
    user.vim_normal_mode_exterm(":call search(\"{text}\", 'bcW')\n")
    insert("y$")
    insert(":set nohls\n")
    user.vim_set_insert_mode()
    edit.paste()

bring line <number_small> <user.text>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert(":call search(\"{text}\", 'c', line('.'))\n")
    insert("y$")
    insert(":set nohls\n")
    user.vim_set_insert_mode()
    edit.paste()

bring line <number_small> <user.ordinals>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("{ordinals-1}W")
    insert("y$")
    user.vim_set_insert_mode()
    edit.paste()
    key(space)

yank words <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("yE")
    # See `:help pattern`
    # \_s   - match single white space
    # \{2,} - at least two in a row
    user.vim_command_mode(":set nohls | let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    # XXX - should this be terminal mode?
    user.vim_set_insert_mode()

yank words (last <number_small> | <number_small> last):
    user.vim_normal_mode_exterm("{number_small}k")
    insert("$T ")
    insert("yE")
    user.vim_set_insert_mode()
    edit.paste()
    key(space)

yank words <number_small> <user.ordinals>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("{ordinals-1}W")
    insert("yE")
    user.vim_set_insert_mode()

# copy from the specified key to the end of the line
yank words <number_small> <user.unmodified_key>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("f{unmodified_key}")
    insert("yE")
    user.vim_set_insert_mode()

# XXX - it would be nice to have this you something like treesitter on a single
# line (even though it would be broken syntax) and be able to specify which
# element we want...
# copy a function name on the specified line
yank words <number_small> funk:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("f(")
    insert("yB")
    user.vim_set_insert_mode()

# echo commands are for copying words from a given point, and then pasting them
bring <number_small>:
    #    user.vim_terminal_echo_line_number("{number_small}")
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("yE")
    # See `:help pattern`
    # \_s   - match single white space
    # \{2,} - at least two in a row
    user.vim_command_mode(":set nohls | let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert_mode()
    edit.paste()
    key(space)

bring (last <number_small> | <number_small> last):
    user.vim_normal_mode_exterm("{number_small}k")
    insert("$T ")
    insert("yE")
    user.vim_set_insert_mode()
    edit.paste()
    key(space)

bring <number_small> <user.ordinals>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("{ordinals-1}W")
    insert("yE")

    user.vim_set_insert_mode()
    edit.paste()
    key(space)

# copy from the specified key to the end of the line
bring <number_small> <user.unmodified_key>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("f{unmodified_key}")
    insert("yE")

    user.vim_set_insert_mode()
    edit.paste()
    # disable weird highlight
    key(down:5)

# XXX - it would be nice to have this you something like treesitter on a single
# line (even though it would be broken syntax) and be able to specify which
# element we want...
# copy a function name on the specified line
bring <number_small> funk:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("f(")
    insert("yB")

    user.vim_set_insert_mode()
    edit.paste()
    # disable weird highlight
    key(down:5)

# yankee are commands are for copying the remaining line from a given point
yank line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("y$")
    user.vim_command_mode(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert_mode()

yank line <number_small> <user.ordinals>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("{ordinals-1}W")
    insert("y$")
    user.vim_set_insert_mode()

yank line (last <number_small> | <number_small> last):
    user.vim_normal_mode_exterm("{number_small}k")
    insert("$T ")
    insert("yE")
    user.vim_set_insert_mode()

yank line command:
    user.vim_normal_mode_exterm("0f y$")
    user.vim_command_mode(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert_mode()

    # this is used for pexpect interactive environments
    # https://pexpect.readthedocs.io/en/stable/api/pexpect.html#spawn-class
    # note that you can't use this from within command line itself, because the
    # terminal may not trigger depending on what the interactive command is. who
    # had actually needs to be global
python escape: key(ctrl-])

# this assumes you list some directories with find or whatever, then you want
# to pivot into one of them beasts on what was listed. you say the relative
# number, in it will jump to that point copy the line and then jump you in
pivot line <number_small>:
    insert("cd ")
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("y$")
    user.vim_command_mode(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert_mode()
    edit.paste()
    key(enter)

pivot river <number_small>:
    insert("cd ")
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    key(ctrl-w)
    key(f)

pivot pillar <number_small>:
    insert("cd ")
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    user.vim_command_mode(":vertical wincmd f\n")

edit line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    insert("gf")

river line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    key('ctrl-w')
    key('f')

pillar line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0')
    user.vim_command_mode(":vertical wincmd f\n")

# Combine the pwd with the path at a relative offset and place the result in
# the clipboard
folder yank merge <number_small>:
    user.vim_command_mode_exterm(":let @+ = getcwd() . '/'\n")
    user.vim_normal_mode("{number_small}k0")
    user.vim_command_mode(":let @+ .= substitute(strtrans(getline('.')), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert_mode()

process kill line <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key('0 w y e')
    user.vim_set_insert_mode()
    insert("kill -9 ")
    edit.paste()
    key(right)
