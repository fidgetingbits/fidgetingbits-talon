tag: user.vim_mason
win.title: /FILETYPE:\[mason\]/
-

# There's a weird case where sometimes when I enter of floating window I'm actually in
# insert mode, , even though you can't directly enter insert mode. I guess this is
# because of the way I trigger certain commands using pynvim. So to work around this I
# still force all of these to use normal mode.

all: user.vim_normal_mode("1")
L S P: user.vim_normal_mode("2")
dap: user.vim_normal_mode("3")
linter: user.vim_normal_mode("4")
formatter: user.vim_normal_mode("5")
install: user.vim_normal_mode("i")
uninstall: user.vim_normal_mode("X")
update: user.vim_normal_mode("u")
update all: user.vim_normal_mode("U")
check new: user.vim_normal_mode("c")
check new all: user.vim_normal_mode("C")
[mason] help: user.vim_normal_mode("g?")
[mason] close: user.vim_normal_mode("q")
