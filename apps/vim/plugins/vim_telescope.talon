tag: user.vim_telescope
-

# A complete list of pickers is here:
# https://github.com/nvim-telescope/telescope.nvim#pickers

# File Pickers
telescope files: user.vim_command_mode_exterm(":Telescope find_files\n")
telescope git files: user.vim_command_mode_exterm(":Telescope git_files\n")
telescope grep this: user.vim_command_mode_exterm(":Telescope grep_string\n")
telescope grep: user.vim_command_mode_exterm(":Telescope live_grep\n")
telescope open grep: user.vim_command_mode_exterm(":Telescope live_grep grep_open_files=true\n")

telescope browse: user.vim_command_mode_exterm(":Telescope file_browser\n")

# Vim Pickers
telescope buffers: user.vim_command_mode_exterm(":Telescope buffers\n")
telescope old files: user.vim_command_mode_exterm(":Telescope oldfiles\n")
telescope commands: user.vim_command_mode_exterm(":Telescope commands\n")
telescope global tags: user.vim_command_mode_exterm(":Telescope tags\n")
telescope command history: user.vim_command_mode_exterm(":Telescope command_history\n")
telescope search history: user.vim_command_mode_exterm(":Telescope search_history\n")
telescope help tags: user.vim_command_mode_exterm(":Telescope help_tags\n")
telescope man pages: user.vim_command_mode_exterm(":Telescope man_page\n")
telescope mark: user.vim_command_mode_exterm(":Telescope mark\n")
telescope color: user.vim_command_mode_exterm(":Telescope colorscheme\n")
telescope quick fix: user.vim_command_mode_exterm(":Telescope quickfix\n")
telescope locations: user.vim_command_mode_exterm(":Telescope locations\n")
telescope options: user.vim_command_mode_exterm(":Telescope options\n")
telescope registers: user.vim_command_mode_exterm(":Telescope registers\n")
telescope auto commands: user.vim_command_mode_exterm(":Telescope autocommands\n")
telescope spell: user.vim_command_mode_exterm(":Telescope spell_suggest\n")
telescope key maps: user.vim_command_mode_exterm(":Telescope keymaps\n")
telescope file types: user.vim_command_mode_exterm(":Telescope filetypes\n")
telescope [high] lights: user.vim_command_mode_exterm(":Telescope highlights\n")
telescope buffer: user.vim_command_mode_exterm(":Telescope current_buffer_fuzzy_find\n")
telescope tags: user.vim_command_mode_exterm(":Telescope current_buffer_key_tags\n")
telescope reload: user.vim_command_mode_exterm(":Telescope reloader\n")

# Neovim LSP Pickers
telescope refs: user.vim_command_mode_exterm(":Telescope lsp_references\n")
telescope document symbols: user.vim_command_mode_exterm(":Telescope lsp_document_symbols\n")
telescope workspace symbols: user.vim_command_mode_exterm(":Telescope lsp_workspace_symbols\n")
telescope dynamic workspace symbols: user.vim_command_mode_exterm(":Telescope lsp_dynamic_workspace_symbols\n")
telescope code actions: user.vim_command_mode_exterm(":Telescope lsp_code_actions\n")
telescope range code actions: user.vim_command_mode_exterm(":Telescope lsp_range_code_actions\n")
telescope document diagnostics: user.vim_command_mode_exterm(":Telescope lsp_document_diagnostics\n")
telescope workspace diagnostics: user.vim_command_mode_exterm(":Telescope lsp_workspace_diagnostics\n")
telescope implementations: user.vim_command_mode_exterm(":Telescope lsp_implementations\n")
telescope definitions: user.vim_command_mode_exterm(":Telescope lsp_definitions\n")

# Git Pickers
telescope git commits: user.vim_command_mode_exterm(":Telescope git_commits\n")
telescope git buffer commits: user.vim_command_mode_exterm(":Telescope git_bcommits\n")
telescope git branches: user.vim_command_mode_exterm(":Telescope git_branches\n")
telescope git status: user.vim_command_mode_exterm(":Telescope git_status\n")
telescope git stash: user.vim_command_mode_exterm(":Telescope git_stash\n")

# Treesitter Picker
telescope tree: user.vim_command_mode_exterm(":Telescope treesitter\n")
