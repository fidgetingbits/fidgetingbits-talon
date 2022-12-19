# XXX this should only be enabled if were in a .ql file
# see also vim_codeql_panel.talon
tag: user.vim_codeql
-

query set database: user.vim_command_mode(":SetDatabase ")
query set last database:
    user.vim_command_mode(":SetDatabase ")
    key(up enter)
query unset database: user.vim_command_mode(":UnsetDatabase ")
query run: user.vim_command_mode(":RunQuery\n")
query quick eval: user.vim_command_mode(":QuickEval\n")
# this is still load previous results
query history: user.vim_command_mode(":History\n")
query stop history: user.vim_command_mode(":StopServer\n")
query syntax tree: user.vim_command_mode(":PrintAST\n")
query load serif: user.vim_command_mode(":LoadSarif")
# This shows the database bar
query archive tree: user.vim_command_mode(":ArchiveTree\n")
