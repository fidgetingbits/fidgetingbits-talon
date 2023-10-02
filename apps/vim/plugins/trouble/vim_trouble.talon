tag: user.vim_trouble
and not win.title: /FILETYPE:\[Trouble\]/
-

trouble toggle: user.vim_command_mode('exe ":TroubleToggle"\n')
trouble close: user.vim_command_mode('exe ":TroubleClose"\n')
trouble refresh: user.vim_command_mode('exe ":TroubleRefresh"\n')

trouble warn: user.vim_command_mode(':exe ":Trouble document_diagnostics"\n')
trouble global warn: user.vim_command_mode(':exe ":Trouble workspace_diagnostics"\n')
trouble (lock list | location): user.vim_command_mode(':exe ":Trouble loclist"\n')
trouble ref: user.vim_command_mode(':exe ":Trouble lsp_references"\n')
trouble quick: user.vim_command_mode(':exe ":Trouble quickfix"\n')
trouble help: user.vim_command_mode(":lua require('trouble').help()\n")
