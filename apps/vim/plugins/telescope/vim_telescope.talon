tag: user.vim_telescope
-

# A complete list of pickers is here:
# https://github.com/nvim-telescope/telescope.nvim#pickers

# File Pickers
(telescope|hunt) files: user.vim_command_mode_exterm(':exe ":Telescope find_files"\n')
(telescope|hunt) git files: user.vim_command_mode_exterm(':exe ":Telescope git_files"\n')
(telescope|hunt) [grep] this: user.vim_command_mode_exterm(':exe ":Telescope grep_string"\n')
(telescope|hunt) code: user.vim_command_mode_exterm(':exe ":Telescope live_grep"\n')
(telescope|hunt) open grep: user.vim_command_mode_exterm(':exe ":Telescope live_grep grep_open_files=true"\n')

(telescope|hunt) browse: user.vim_command_mode_exterm(':exe ":Telescope file_browser"\n')

# Vim Pickers
(telescope|hunt) buffers: user.vim_command_mode_exterm(':exe ":Telescope buffers"\n')
(telescope|hunt) old files: user.vim_command_mode_exterm(':exe ":Telescope oldfiles"\n')
(telescope|hunt) commands: user.vim_command_mode_exterm(':exe ":Telescope commands"\n')
(telescope|hunt) global tags: user.vim_command_mode_exterm(':exe ":Telescope tags"\n')
(telescope|hunt) command history: user.vim_command_mode_exterm(':exe ":Telescope command_history"\n')
(telescope|hunt) search history: user.vim_command_mode_exterm(':exe ":Telescope search_history"\n')
(telescope|hunt) help tags: user.vim_command_mode_exterm(':exe ":Telescope help_tags"\n')
(telescope|hunt) man pages: user.vim_command_mode_exterm(':exe ":Telescope man_page"\n')
(telescope|hunt) mark: user.vim_command_mode_exterm(':exe ":Telescope mark"\n')
(telescope|hunt) color: user.vim_command_mode_exterm(':exe ":Telescope colorscheme"\n')
(telescope|hunt) quick fix: user.vim_command_mode_exterm(':exe ":Telescope quickfix"\n')
(telescope|hunt) locations: user.vim_command_mode_exterm(':exe ":Telescope locations"\n')
(telescope|hunt) options: user.vim_command_mode_exterm(':exe ":Telescope options"\n')
(telescope|hunt) registers: user.vim_command_mode_exterm(':exe ":Telescope registers"\n')
(telescope|hunt) auto commands: user.vim_command_mode_exterm(':exe ":Telescope autocommands"\n')
(telescope|hunt) spell: user.vim_command_mode_exterm(':exe ":Telescope spell_suggest"\n')
(telescope|hunt) key maps: user.vim_command_mode_exterm(':exe ":Telescope keymaps"\n')
(telescope|hunt) file types: user.vim_command_mode_exterm(':exe ":Telescope filetypes"\n')
(telescope|hunt) [high] lights: user.vim_command_mode_exterm(':exe ":Telescope highlights"\n')
(telescope|hunt) (buffer|lines): user.vim_command_mode_exterm(':exe ":Telescope current_buffer_fuzzy_find"\n')
(telescope|hunt) tags: user.vim_command_mode_exterm(':exe ":Telescope current_buffer_key_tags"\n')
(telescope|hunt) reload: user.vim_command_mode_exterm(':exe ":Telescope reloader"\n')

# Neovim LSP Pickers
(telescope|hunt) refs: user.vim_command_mode_exterm(':exe ":Telescope lsp_references"\n')
(telescope|hunt) [document] symbols: user.vim_command_mode_exterm(':exe ":Telescope lsp_document_symbols"\n')
(telescope|hunt) global symbols: user.vim_command_mode_exterm(':exe ":Telescope lsp_workspace_symbols"\n')
(telescope|hunt) global dynamic symbols: user.vim_command_mode_exterm(':exe ":Telescope lsp_dynamic_workspace_symbols"\n')
(telescope|hunt) code actions: user.vim_command_mode_exterm(':exe ":Telescope lsp_code_actions"\n')
(telescope|hunt) range code actions: user.vim_command_mode_exterm(':exe ":Telescope lsp_range_code_actions"\n')
(telescope|hunt) document diagnostics: user.vim_command_mode_exterm(':exe ":Telescope lsp_document_diagnostics"\n')
(telescope|hunt) workspace diagnostics: user.vim_command_mode_exterm(':exe ":Telescope lsp_workspace_diagnostics"\n')
(telescope|hunt) implementations: user.vim_command_mode_exterm(':exe ":Telescope lsp_implementations"\n')
(telescope|hunt) definitions: user.vim_command_mode_exterm(':exe ":Telescope lsp_definitions"\n')

# Git Pickers
(telescope|hunt) git commits: user.vim_command_mode_exterm(':exe ":Telescope git_commits"\n')
(telescope|hunt) git buffer commits: user.vim_command_mode_exterm(':exe ":Telescope git_bcommits"\n')
(telescope|hunt) [git] branches: user.vim_command_mode_exterm(':exe ":Telescope git_branches"\n')
(telescope|hunt) git status: user.vim_command_mode_exterm(':exe ":Telescope git_status"\n')
(telescope|hunt) git stash: user.vim_command_mode_exterm(':exe ":Telescope git_stash"\n')

# Treesitter Picker
(telescope|hunt) tree: user.vim_command_mode_exterm(':exe ":Telescope treesitter"\n')
