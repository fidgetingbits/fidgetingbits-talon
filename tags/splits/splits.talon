tag: user.splits
-
split right: user.split_window_right()
split left: user.split_window_left()
split (down|south): user.split_window_down()
split (up|north): user.split_window_up()
pillar: user.split_window_vertically()
river: user.split_window_horizontally()
split flip: user.split_flip()
split (max|zoom): user.split_maximize()
split reset: user.split_reset()
split window: user.split_window()
split clear: user.split_clear()
split clear all: user.split_clear_all()
split grow: user.split_grow()
split shrink: user.split_shrink()
split wider: user.split_width_grow()
split thinner: user.split_width_shrink()
split taller: user.split_height_grow()
split shorter: user.split_height_shrink()

# split navigation
# move to the next split moving right
(split next | sprite): user.split_next()
# moved to the next split moving left
(split last | spliff): user.split_last()
go split <number>: user.split_number(number)
