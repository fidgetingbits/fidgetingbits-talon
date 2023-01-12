# These commands had only make sense to be exposed of vim is currently in
# command mode
# # TODO: It would make a lot more sense if this also disabled the bunch of other
# functionality that we would never want to run from inside command mode ...
# See `:help cmdline`
win.title: /VIM MODE:c/
-
tag(): user.vim_command_mode
# We assume that the user may want to use lua in the commandline, so we include some
tag(): user.nvim_lua

paste register <user.key>: key(ctrl-r {key})

# Command-line completion: help:cmdline-completion
(match names | expand that): key(ctrl-a)

literal: key(ctrl-v)

# XXX - a the ctrl-r ctrl-<key> stuff

# XXX - add the ctrl-d autocompletion stuff

# regex
# XXX - should be made part of a generic regex grammar
state non greedy: "\\{{-}}"
state greedy: ".*"
state escaped or: user.insert_cursor("\\([|]\\|\\)")

push <user.unmodified_key>:
    key('end')
    key('{unmodified_key}')

# TODO: This should use line editing abstraction
push that:
    key('end')
    edit.paste()

# neovim lua stuff
print nvim global: insert_between("print(vim.g.", ")")
pretty print: user.insert_between("print(vim.inspect(", "))"
