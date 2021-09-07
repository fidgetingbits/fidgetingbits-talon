# https://github.com/tpope/vim-fugitive
# This file is specifically for when navigating the git-summary feature of the
# vim-fugitive plugin

# It currently relies on you using ${FugitiveStatusLine()} in your titlestring
# ex: let &titlestring ='VIM MODE:%{mode()} RPC:%{v:servername} %{FugitiveStatusline()} (%f) %t'
tag: user.vim_fugitive_summary
and win.title: /\[Git.*git.*index/
#tag: user.vim_fugitive_summary
#and win.title: /.git\/index/
-

# Staging/unstaging maps

[file] stage: user.vim_normal_mode_key("s")
[file] unstage: user.vim_normal_mode_key("u")
unstage (all|everything): user.vim_normal_mode_key("U")
discard change: user.vim_normal_mode_key("X")
file diff: user.vim_normal_mode_key("=")
file exclude: user.vim_normal_mode_keys("g I")

# Diff maps

# Navigation maps
# XXX - these should may be override common file actions
open file: user.vim_normal_mode_key("o")
open vertical file: user.vim_normal_mode_keys("g O")
open tab file: user.vim_normal_mode_key("O")
preview file: user.vim_normal_mode_key("p")

# Commit maps

commit [changes]: 
    user.vim_normal_mode_keys("c c")
    user.vim_set_insert_mode()
amend [last commit]: user.vim_normal_mode_keys("c a")

# Checkout/branch maps

# Stash maps

# Rebase maps

# Miscellaneous maps

[git] status close: user.vim_normal_mode_keys("g q")
help: user.vim_normal_mode_keys("g ?")

# Global maps
