not tag: user.i3wm
-

portal <number_small>: user.desktop(number_small)
portal (next | right): user.desktop_next()
portal (last | left): user.desktop_last()
portal show: user.desktop_show()
shuffle place <number>: user.window_move_desktop(number, false)
shuffle <number>: user.window_move_desktop(number, true)
shuffle left: user.window_move_desktop_left()
shuffle right: user.window_move_desktop_right()
