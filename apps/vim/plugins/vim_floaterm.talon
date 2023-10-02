# https://github.com/voldikss/vim-floaterm
tag: user.vim_floaterm
-

float term: user.vim_command_mode_exterm(':exe ":FloatermNew"\n')
(float toggle | toggle float): user.vim_command_mode_exterm(':exe ":FloatermToggle"\n')
float kill: user.vim_command_mode_exterm(':exe ":FloatermKill"\n')
# python repl
float python: user.vim_command_mode_exterm(':exe ":FloatermNew python"\n')
# talon repl
float talon: user.vim_command_mode_exterm(':exe ":FloatermNew ~/.talon/bin/repl"\n')
