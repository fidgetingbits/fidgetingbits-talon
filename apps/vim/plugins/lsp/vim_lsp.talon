# XXX - this should eventually be generic for handling multiple different lsp
# implementations
tag: user.vim_lsp
-

(code server | lisp) info: user.vim_command_mode(':exe ":LspInfo"\n')
(code server | lisp) start: user.vim_command_mode(':exe ":LspStart"\n')
(code server | lisp) stop: user.vim_command_mode(":LspStop ")
lisp dock sym:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.document_symbol()"\n')
lisp log level trace:
    user.vim_command_mode(":exe \":lua vim.lsp.set_log_level('trace')\"\n")
lisp log level debug:
    user.vim_command_mode(":exe \":lua vim.lsp.set_log_level('debug')\"\n")
lisp log level info:
    user.vim_command_mode(":exe \":lua vim.lsp.set_log_level('info')\"\n")
lisp log level warn:
    user.vim_command_mode(":exe \":lua vim.lsp.set_log_level('warn')\"\n")
lisp log level error:
    user.vim_command_mode(":exe \":lua vim.lsp.set_log_level('error')\"\n")
lisp log file show:
    user.vim_command_mode_exterm(":exe 'tabnew ' .. luaeval(\"vim.lsp.get_log_path()\")\n")

#user.vim_command_mode(':exe ":lua vim.lsp.buf.clear_references()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.code_action()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.completion()"\n')

#(jump|lisp) (declaration|deck): user.vim_command_mode(':exe ":lua vim.lsp.buf.declaration()"\n')
(jump | lisp) implementation:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.implementation()"\n')
(jump | lisp) (definition | deaf):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.definition()"\n')
(jump | lisp) (highlight | light):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.document_highlight()"\n')

#user.vim_command_mode(':exe ":lua vim.lsp.buf.formatting()"\n')
(jump | lisp) hover: user.vim_command_mode(':exe ":lua vim.lsp.buf.hover()"\n')
peek (this | deaf): user.vim_command_mode(':exe ":lua vim.lsp.buf.hover()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.implementation()"\n')
(jump | lisp) in coming:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.incoming_calls()"\n')
(jump | lisp) out going:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.outgoing_calls()"\n')
(jump | peak) (references | ref | callers):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.references()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.signature_help()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.type_definition()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.workspace_symbol()"\n')

# Code refactoring
code rename:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.rename()"\n')
# Code linting and formatting
file fix:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.format()"\n')
