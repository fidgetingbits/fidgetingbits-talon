# https://github.com/numToStr/Comment.nvim
tag: user.vim_comment_nvim
-

# TODO: Move this to more explicit motion grammar, but at the moment I seem to have some
# problems with conflicts, so I'm explicitly doing it here.
[un] comment (toggle | this | line): user.vim_normal_mode("gcc")
[un] comment <number_small> (line | lines): user.vim_normal_mode("{number_small}gcc")
block comment (toggle | this): user.vim_normal_mode("gbc")
[un] comment above: user.vim_normal_mode_np("gcO")
[un] comment below: user.vim_normal_mode_np("gco")
(comment push | push comment): user.vim_normal_mode_np("gcA")

# TODO: This may differ in visual mode
# TODO: Technically the included text objects here are outside the scope of what can be done with
# commenting, but for the sake of not duplicating lists for now I will leave it here.
[un] comment (<user.vim_text_objects>): user.vim_normal_mode("gc{vim_text_objects}")

[un] comment <number_small> (<user.vim_text_objects>):
    user.vim_normal_mode("gc{number_small}{vim_text_objects}")

[un] comment till (<user.vim_motions>): user.vim_normal_mode("gc{vim_motions}")
