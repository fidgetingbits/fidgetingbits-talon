tag: user.vim_lazy
win.title: /FILETYPE:\[lazy\]/
win.title: /FILETYPE:\[on\]/
-
# NOTE: I think the filetype 'on' above is probably a bug. It only triggers when lazy is
# called on initial startup

install: user.vim_normal_mode("I")
update: user.vim_normal_mode("U")
sync: user.vim_normal_mode("S")
clean: user.vim_normal_mode("X")
check: user.vim_normal_mode("C")
log: user.vim_normal_mode("L")
restore: user.vim_normal_mode("R")
profile: user.vim_normal_mode("P")
debug: user.vim_normal_mode("D")
help: user.vim_normal_mode("?")
close: user.vim_normal_mode("q")
