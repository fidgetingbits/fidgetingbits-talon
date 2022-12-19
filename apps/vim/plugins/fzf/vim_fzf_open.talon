# see vim_fzf.talon for the main commands.
#
# The commands in this file are only relevant for when an actual fzf.vim
# floating window is open
# See https://github.com/junegunn/fzf.vim#global-options for bindings
#
# NOTE: by default certain commands will not advertise that they're running
# inside of fzf, so the title matching below doesn't necessarily work without
# manual modification. Ex: anything other than :Files?
tag: user.vim_fzf
win.title: /#FZF/
-

open in vertical split: key(ctrl-v)
open in split: key(ctrl-v)
open in tab: key(ctrl-t)
