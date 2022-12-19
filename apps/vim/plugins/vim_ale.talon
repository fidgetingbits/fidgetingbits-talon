tag: user.vim_ale
-

ale help: user.vim_command_mode(":help ale\n")
ale toggle: user.vim_command_mode(":ALEToggle\n")
ale info: user.vim_command_mode(':exe ":ALEInfo"\n')
ale next: user.vim_command_mode(":ALENext\n")
ale next wrap: user.vim_command_mode(":ALENextWrap\n")
ale (prev | previous): user.vim_command_mode(":ALEPrevious\n")
ale (prev | previous) wrap: user.vim_command_mode(":ALEPreviousWrap\n")
ale fix: user.vim_command_mode(":ALEFix\n")
ale lint: user.vim_command_mode(":ALELint\n")
ale suggest [fixers]: user.vim_command_mode(":ALEFixSuggest\n")
