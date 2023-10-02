tag: user.vim_flip_ext
-

# TODO: Switch flip type to flip-ext, also add a proper tag.
file flip: user.vim_normal_mode(":lua require('flip-ext').flip()\n")
flip reload: user.vim_normal_mode(":lua require('flip-ext').reload()\n")
