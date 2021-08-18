app: vim
-

###
# Convenience for opening my different files
###
edit my vim scripts:
    user.vim_command_mode_exterm(":source ~/.vim/sessions/talon_vim.session\n")

open talon plugins:
    user.vim_command_mode_exterm(":e ~/source/talon/releases/latest/resources/talon_plugins\n")
open talon python:
    user.vim_command_mode_exterm(":e ~/source/talon/releases/latest/resources/python/lib/python3.7/site-packages/talon\n")

###
# Admin
###
# XXX - make this a look up the actual sessions that exist in that folder
scratch session:
    user.vim_command_mode_exterm(":source ~/.vim/sessions/scratch.session")
stellaris session:
    user.vim_command_mode_exterm(":source ~/.vim/sessions/stellaris.session")

###
#
###
fine merge conflict:
    user.vim_command_mode_exterm(":/\\c<<<\n")

dick to class member:
    user.vim_normal_mode("ds[ds\"i.")

###
# Things that mix vim and other command
###
# XXX - rename
super focus:
    # i3wm full screen toggle
    key(super-f)
    # wait for redraw
    sleep(200ms)
    # equalize vim splits
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(=)

###
# Email writing
###

nest this:
    user.vim_set_normal_mode()
    key(0)
    key(m ')
    insert("gqap")
    key(')
    key(')
    key(0)
    user.vim_set_visual_block_mode()
    key(} up)
    key(0 I > space escape)

tidy nest:
    user.vim_set_normal_mode()
    key(0 l)
    user.vim_set_visual_block_mode()
    key(} up l)
    key(I space escape)

# turn a non line wrapped email response into a more wealth formatted
# traditional style nesting
re nest this:
    key(0)
    user.vim_set_visual_block_mode()
    key(} up)
    key(0 I > escape)

###
# VimScript function shortcuts
###

convert string to stack:
    user.vim_command_mode(":call String_to_stack_buffer()")
    edit.left()

toggle (debug|verbose) log:
    user.vim_command_mode(":call ToggleVerbose()\n")
