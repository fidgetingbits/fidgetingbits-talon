tag: user.vim_telescope
win.title: /[Prompt]/
-

# XXX - using preserve insert mode went inside of a telescope window, but
# otherwise using regular vim commands is broken. we main to a special case
# detecting certain overrides from inside of vim.py? if when telescope is open
# it registers a callback that prevents the preservation, then on registers on
#  context switch
cancel: key(ctrl-c)
