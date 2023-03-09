# https://github.com/tpope/vim-fugitive
# This file is specifically for when navigating the git-summary feature of the
# vim-fugitive plugin
# It currently relies on you using ${FugitiveStatusLine()} in your titlestring
# ex: let &titlestring ='VIM MODE:%{mode()} RPC:%{v:servername} %{FugitiveStatusline()} (%f) %t'
tag: user.vim_fugitive_summary
and win.title: /\[Git.*git.*index/
tag: user.vim_fugitive_summary
and win.title: /fugitive:\/\//
#tag: user.vim_fugitive_summary
#and win.title: /.git\/index/
-

# Staging/unstaging maps

[file] stage: user.vim_normal_mode_key("s")
[file] unstage: user.vim_normal_mode_key("u")
unstage (all | everything): user.vim_normal_mode_key("U")
[file] discard change: user.vim_normal_mode_key("X")
file diff: user.vim_normal_mode_key("=")
file diff top:
    user.vim_normal_mode("zt")
    user.vim_normal_mode_key("=")
file exclude: user.vim_normal_mode_keys("g I")

# Diff maps

# Navigation maps
# XXX - these should may be override common file actions
file open: user.vim_normal_mode_key("o")
file open vertical: user.vim_normal_mode_keys("g O")
file open tabbed: user.vim_normal_mode_key("O")
file preview: user.vim_normal_mode_key("p")

# Commit maps

git commit [changes]:
    user.vim_normal_mode_keys("c c")
    user.vim_set_insert_mode()
(fugitive | git) commit [message] {user.git_conventional_commits}:
    user.vim_normal_mode_keys("c c")
    user.vim_set_insert_mode()
    sleep(0.1)
    insert("{user.git_conventional_commits}: ")
(fugitive | git) commit [message] {user.git_conventional_commits} <user.word>:
    user.vim_normal_mode_keys("c c")
    user.vim_set_insert_mode()
    sleep(0.1)
    insert("{user.git_conventional_commits}({word}): ")
git commit verbose [changes]:
    user.vim_normal_mode_keys("c v c")
    user.vim_set_insert_mode()
(fugitive | git) commit verbose {user.git_conventional_commits}:
    user.vim_normal_mode_keys("c v c")
    user.vim_set_insert_mode()
    sleep(0.1)
    insert("{user.git_conventional_commits}: ")
(fugitive | git) commit verbose {user.git_conventional_commits} <user.word>:
    user.vim_normal_mode_keys("c v c")
    user.vim_set_insert_mode()
    sleep(0.1)
    insert("{user.git_conventional_commits}({word}): ")
amend [last commit]: user.vim_normal_mode_keys("c v a")
commit reword: user.vim_normal_mode("cw")

file restore: user.vim_normal_mode_key("X")

# Checkout/branch maps

# Stash maps

# Rebase maps

git rebase start: user.vim_normal_mode("ri")
git rebase continue: user.vim_normal_mode("rr")
git rebase abort: user.vim_normal_mode("ra")

# Miscellaneous maps

[git] status close: user.vim_normal_mode_keys("g q")
(fugitive | git) help: user.vim_normal_mode_keys("g ?")

# Navigation
jump untracked [<number>]: user.vim_normal_mode("gu")
jump unstaged [<number>]: user.vim_normal_mode("gU")
jump unpushed [<number>]: user.vim_normal_mode("gp")
jump unpulled [<number>]: user.vim_normal_mode("gP")

# Global maps
git status close: user.vim_normal_mode("gq")
