# These commands had only make sense to be exposed of vim is currently in
# command mode
# See `:help cmdline`

win.title: /VIM MODE:c/
-
tag(): user.vim_command_mode

paste register <user.key>: key(ctrl-r {key})

# Command-line completion: help:cmdline-completion
(match names|expand that): key(ctrl-a)

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

push it:
    key('end')
    edit.paste()
