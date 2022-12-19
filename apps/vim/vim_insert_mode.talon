tag: user.vim_insert_mode
-

(dup | duplicate) line: user.vim_normal_mode_np("yyp")

yank line: user.vim_normal_mode_np("yy")

push: key('end')

push <user.unmodified_key>:
    key('end')
    key('{unmodified_key}')

push it:
    key('end')
    edit.paste()
