# https://github.com/numToStr/Comment.nvim
tag: user.vim_comment_nvim
-

comment toggle: user.vim_normal_mode("gcc")
block comment toggle: user.vim_normal_mode("gbc")
comment above: user.vim_normal_mode_np("gcO")
comment below: user.vim_normal_mode_np("gco")
comment push: user.vim_normal_mode_np("gcA")

# XXX - Still have to add smart tree-sitter based commands
# Although some is already working because I added `gc` directly to
# commands_with_motion in vim.py
