window (new | open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
(window | snap) hide: app.window_hide()
focus <user.running_applications>: user.switcher_focus(running_applications)
focus flip: user.switch_last_focused()
[help] running list: user.switcher_toggle_running()
running close: user.switcher_hide_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

# FIXME: These are gnome specific tests
run command: key(alt-f2)
run command <user.text>:
    key(alt-f2)
    sleep(100ms)
    insert(text)
launch: key(super)
launch <user.text>:
    key(super)
    sleep(100ms)
    insert(text)

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
