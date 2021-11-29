# XXX - this should eventually be generic for handling multiple different lsp
# implementations
tag: user.vim_lsp
-

(code server|lisp) info: user.vim_command_mode(':exe ":LspInfo"\n')
lisp dock sym: user.vim_command_mode(':exe ":lua vim.lsp.buf.document_symbol()"\n')
lisp log level trace: user.vim_command_mode(':exe ":lua vim.lsp.set_log_level(\'trace\')"\n')
lisp log level debug: user.vim_command_mode(':exe ":lua vim.lsp.set_log_level(\'debug\')"\n')
lisp log level info: user.vim_command_mode(':exe ":lua vim.lsp.set_log_level(\'info\')"\n')
lisp log level warn: user.vim_command_mode(':exe ":lua vim.lsp.set_log_level(\'warn\')"\n')
lisp log level error: user.vim_command_mode(':exe ":lua vim.lsp.set_log_level(\'error\')"\n')
lisp log file show: user.vim_command_mode(':exe ":lua vim.lsp.log.get_file_name()"\n')

#user.vim_command_mode(':exe ":lua vim.lsp.buf.clear_references()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.code_action()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.completion()"\n')
tag (declaration|deck): user.vim_command_mode(':exe ":lua vim.lsp.buf.declaration()"\n')
tag (definition|deaf): user.vim_command_mode(':exe ":lua vim.lsp.buf.definition()"\n')
tag (highlight|light): user.vim_command_mode(':exe ":lua vim.lsp.buf.document_highlight()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.formatting()"\n')
tag hover: user.vim_command_mode(':exe ":lua vim.lsp.buf.hover()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.implementation()"\n')
tag in [coming]: user.vim_command_mode(':exe ":lua vim.lsp.buf.incoming_calls()"\n')
tag out [going]: user.vim_command_mode(':exe ":lua vim.lsp.buf.outgoing_calls()"\n')
tag (references|ref): user.vim_command_mode(':exe ":lua vim.lsp.buf.references()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.rename()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.signature_help()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.type_definition()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.workspace_symbol()"\n')
