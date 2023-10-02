tag: user.vim_telescope
win.title: /FILETYPE:\[TelescopePrompt\]/
-

# XXX - using preserve insert mode went inside of a telescope window, but
# otherwise using regular vim commands is broken. we main to a special case
# detecting certain overrides from inside of vim.py? if when telescope is open
# it registers a callback that prevents the preservation, then on registers on
#  context switch
cancel: user.vim_insert_mode_key("ctrl-c")
# this is mostly due to bad habits from fzf. the idea is to encourage me to
# start using the explicit mode switching commands
escape:
    app.notify("Stop saying escape in telescope")
    key(ctrl-c)
close: key(ctrl-c)
quick (list | fix) [that]: key(ctrl-q)

# telescope-hop
hop to: key(ctrl-h)
hop select: key(ctrl-space)
