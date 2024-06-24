tag: user.tabs
-

# Creation
tabby (open | new): app.tab_open()
tabby (open | new) named [<user.text>]: user.tab_open_with_name(text or "")
tabby (reopen | restore): app.tab_reopen()
tabby duplicate: user.tab_clone()

# Destruction
tabby close: user.tab_close_wrapper()
tabby close all: user.tab_close_all()
tabby (close others|solo): user.tab_close_others()

# Navigation
[go] tabby (last | previous | left): app.tab_previous()
[go] tabby (next|right): app.tab_next()
[go] tabby <number>: user.tab_focus_index(number)
[go] tabby minus <number>: user.tab_focus_negative_index(number)
[go] tabby first: user.tab_focus_first()
[go] tabby final: user.tab_focus_final()
[go] tabby flip: user.tab_focus_most_recent()
tabby search [<user.text>]: user.tab_search(text or "")

# Arrangement
tabby pin: user.tab_pin()
tabby unpin: user.tab_unpin()
tabby move right: user.tab_move_right()
tabby move left: user.tab_move_left()
tabby move to split right: user.tab_move_to_split_right()
tabby move to split left: user.tab_move_to_split_left()
tabby move [to split] up: user.tab_move_to_split_up()
tabby move [to split] down: user.tab_move_to_split_down()

# Renaming
tabby rename [<user.text>]: user.tab_rename_formatted(text or "")
tabby [name] reset: user.tab_reset_name()
