# https://github.com/LumaKernel/fern-mapping-fzf.vim
# See `:help fern-mapping-fzf`
# NOTE: Only relevant if fern is actually open
tag: user.vim_vern_open
and tag: user.vim_fern_mapping_fzf
-

fuzz files: user.vim_normal_mode_exterm("ff")
fuzz paths: user.vim_normal_mode_exterm("fd")
fuzz: user.vim_normal_mode_exterm("fa")
