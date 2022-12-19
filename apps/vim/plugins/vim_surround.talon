# see `code/vim.py` for more implementation
tag: user.vim_surround
-

# TODO
#  - add custom surround with markdown command for when i forget to use snip
#    first

# visual mode only
wrap selected with <user.vim_surround_targets>:
    user.vim_visual_mode("S{vim_surround_targets}")

# normal mode

# selects the word under cursor
wrap this with <user.vim_surround_targets>:
    user.vim_normal_mode("ysiw{vim_surround_targets}")

# cursor to the end of the word
wrap [with] <user.vim_surround_targets>:
    user.vim_normal_mode("ysw{vim_surround_targets}")

wrap <user.vim_text_objects> with <user.vim_surround_targets>:
    user.vim_normal_mode("ys{vim_text_objects}{vim_surround_targets}")

wrap <user.vim_motions_all_adjust> [with] <user.vim_surround_targets>:
    user.vim_normal_mode("ys{vim_motions_all_adjust}{vim_surround_targets}")

wrap <user.vim_unranged_surround_text_objects> [with] <user.vim_surround_targets>:
    user.vim_normal_mode("ys{vim_unranged_surround_text_objects}{vim_surround_targets}")

wrap line with <user.vim_surround_targets>:
    user.vim_normal_mode("yss{vim_surround_targets}")

wrap and indent line with <user.vim_surround_targets>:
    user.vim_normal_mode("ySS{vim_surround_targets}")

(clear | drop) those <user.vim_surround_targets>:
    user.vim_normal_mode("ds{vim_surround_targets}")

swap those <user.vim_surround_targets> with <user.vim_surround_targets>:
    user.vim_normal_mode("cs{vim_surround_targets_1}{vim_surround_targets_2}")
