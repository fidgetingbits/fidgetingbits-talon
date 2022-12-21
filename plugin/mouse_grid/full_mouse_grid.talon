tag: user.full_mouse_grid_enabled
-
soup on:
    user.full_grid_select_screen(1)
    user.full_grid_activate()

soup screen <number>:
    user.full_grid_select_screen(number)
    user.full_grid_activate()

soup win:
    user.full_grid_place_window()
    user.full_grid_activate()

soup replay drag: user.full_grid_replay_drag()

soup <user.modifiers> replay drag:
    key("{modifiers}:down")
    user.full_grid_replay_drag()
    key("{modifiers}:up")
