window (new | open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
(window | snap) hide: app.window_hide()
need <user.running_applications>: user.switcher_focus(running_applications)
(need flip|flipper): user.switch_last_focused()

[help] running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

# top, bottom, left, right, center, full
snap {user.window_snap_positions}: user.snap_window_to_position(window_snap_positions)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)

snap (in | out): user.desktop_show()

# alt-tab style cycling
win cycle: user.switcher_focus_last()
