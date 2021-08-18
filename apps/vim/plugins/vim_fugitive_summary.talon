# This file is specifically for when navigating the git status pane
# https://github.com/tpope/vim-fugitive
# It currently relies on you using ${FugitiveStatusLine()} in your titlestring
# ex: let &titlestring ='VIM MODE:%{mode()} RPC:%{v:servername} %{FugitiveStatusline()} (%f) %t'
# XXX - need to make sure not to conflict with vim bindings
# XXX - missing a significant amount of commands
app: vim
# XXX - at some point titles started showing the git repo, so for now i match
# on something else
tag: user.vim_fugitive_summary
and win.title: /\[Git.*git.*index/
#tag: user.vim_fugitive_summary
#and win.title: /.git\/index/
-

# Staging/unstaging maps

[file] stage: key(s)
[file] unstage: key(u)
unstage (all|everything): key(U)
discard change: key(key)
file diff: key(=)
file exclude: "gI"

# Diff maps

# Navigation maps
# XXX - these should may be override common file actions
open file: key(o)
open vertical file: insert(gO)
open tab file: key(O)
preview file: key(p)

# Commit maps

commit [changes]: 
    insert("cc")
    user.vim_set_insert_mode()
amend [last commit]: "ca"

# Checkout/branch maps

# Stash maps

# Rebase maps

# Miscellaneous maps

[git] status close: "gq"
help: "g?"

# Global maps
