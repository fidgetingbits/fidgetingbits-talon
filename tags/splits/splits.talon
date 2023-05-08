tag: user.splits
-
split right: user.split_window_right()
split left: user.split_window_left()
split down: user.split_window_down()
split up: user.split_window_up()
split (vertically | vertical): user.split_window_vertically()
split (horizontally | horizontal): user.split_window_horizontally()
split flip: user.split_flip()
split max: user.split_maximize()
split reset: user.split_reset()
split window: user.split_window()
split clear: user.split_clear()
split clear all: user.split_clear_all()

# split navigation
# move to the next split moving right
(split next|sprite): user.split_next()
# moved to the next split moving left
(split last|spliff): user.split_last()
go split <number>: user.split_number(number)
