# see markdown_snippets.py for more complete list
tag: user.vim_ultisnips
and tag: user.markdown
-

# XXX - unsupported by current snippets.py
snip table <number_small> <number_small>:
    user.vim_insert_mode("tb(")
    insert("{number_small_1}{number_small_2})")
    key(tab)
