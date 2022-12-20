tag: user.tabs
-
# using tab conflicts with the "tab" key
tabby (open | new): app.tab_open()
tabby last: app.tab_previous()
tabby next: app.tab_next()
tabby close: app.tab_close()
tabby reopen: app.tab_reopen()
go tabby <number>: user.tab_jump(number)
go tabby final: user.tab_final()
go tabby first: user.tab_first()
tabby search: user.tab_search()
tabby (duplicate): user.tab_duplicate()
