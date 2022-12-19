# vim_nerdtree_open.talon for the remainder of commands
# https://github.com/preservim/nerdtree
tag: user.vim_nerdtree
-

nerd tree: user.vim_normal_mode_exterm(":NERDTree\n")
nerd here: user.vim_normal_mode_exterm(":NERDTree %\n")
nerd clip:
    user.vim_command_mode_exterm(":NERDTree ")
    edit.paste()
    key(enter)
