# This is the "mode" that we enter when pressing `q:` or `q/` from normal mode
# Our window title will look something like this:
# IO VIM MODE:n RPC:/tmp/nvimWP0y5W/0  ([Command Line]) [Command Line]
app: vim
tag: user.vim_normal_mode
and win.title: /[Command Line]/
-

# XXX - need to override the commands for closing the buffer to use ctrl+c
# also support commands for just saying normal mode or whatever to escape out
# of it
escape: key(ctrl-c)
