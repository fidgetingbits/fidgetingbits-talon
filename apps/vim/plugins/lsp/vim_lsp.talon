# XXX - this should eventually be generic for handling multiple different lsp
# implementations
tag: user.vim_lsp
-

(code server | lisp) (info | show): user.vim_command_mode(':exe ":LspInfo"\n')
(code server | lisp) start: user.vim_command_mode(':exe ":LspStart"\n')
(code server | lisp) stop: user.vim_command_mode(":LspStop ")
lisp dock sym: user.vim_command_mode(':exe ":lua vim.lsp.buf.document_symbol()"\n')

# logging
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

# navigation
#(jump|lisp) (declaration|deck): user.vim_command_mode(':exe ":lua vim.lsp.buf.declaration()"\n')
(jump | lisp) implementation:
    user.vim_command_mode(':exe ":lua vim.lsp.buf.implementation()"\n')
(jump | lisp) (definition | deaf):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.definition()"\n')
(jump | lisp) (highlight | light):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.document_highlight()"\n')
#user.vim_command_mode(':exe ":lua vim.lsp.buf.formatting()"\n')
# TODO: Closing these is a little bit annoying because we don't have any context, we
# need need to make a hook that somehow indicates the pop up is open
(peek | hover) (this | deaf):
    user.vim_command_mode(':exe ":lua vim.lsp.buf.hover()"\n')
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
(code rename | rename this):
    #user.vim_command_mode(':exe ":lua vim.lsp.buf.rename()"\n')
    user.vim_command_mode(":IncRename ")
# Code linting and formatting
file fix: user.vim_command_mode(':exe ":lua vim.lsp.buf.format()"\n')

# diagnostics
# also see plugins/trouble/ for a better interface
toggle errors:
    user.vim_command_mode(':exe ":lua vim.diagnostic.show_line_diagnostics()"\n')

# TODO: It would be nice for this to toggle if it's already open
trouble show: user.vim_command_mode(':exe ":lua vim.diagnostic.open_float()"\n')
trouble next: user.vim_command_mode(':exe ":lua vim.diagnostic.goto_next()"\n')
trouble (prev | last):
    user.vim_command_mode(':exe ":lua vim.diagnostic.goto_prev()"\n')
