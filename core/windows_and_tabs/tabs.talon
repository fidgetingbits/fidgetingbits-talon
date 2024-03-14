tag: user.tabs
-
# using tab conflicts with the "tab" key
tabby (open | new): app.tab_open()
tabby (last | left): app.tab_previous()
tabby (next | right): app.tab_next()
tabby close: app.tab_close()
tabby reopen: app.tab_reopen()
tabby show: user.tabs_show()
[go] tabby <number>: user.tab_jump(number)
[go] tabby final: user.tab_final()
[go] tabby first: user.tab_first()
tabby search: user.tab_search()
tabby (duplicate): user.tab_duplicate()
tabby pin: user.tab_pin()
tabby unpin: user.tab_unpin()
(tabby flip | flip): user.tab_last()
tabby rename [<user.text>]: user.tab_rename(text or '')
