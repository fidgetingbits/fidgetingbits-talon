tag: user.vim_trouble
win.title: /FILETYPE:\[Trouble\]/
-

# TODO: It might be good to remove some of the other default of in bindings here?
# This list is also incomplete, see: https://github.com/folke/trouble.nvim#setup
[trouble] close: user.vim_normal_mode("q")
[trouble] refresh: user.vim_normal_mode("r")
[trouble] next: user.vim_normal_mode("j")
[trouble] previous: user.vim_normal_mode("k")
[trouble] jump: user.vim_normal_mode("enter")
[trouble] jump close: user.vim_normal_mode("o")
[trouble] hover: user.vim_normal_mode("K")
