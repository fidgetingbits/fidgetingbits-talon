tag: user.full_mouse_grid_showing
and tag: user.full_mouse_grid_enabled
and mode: user.full_mouse_grid
and not mode: sleep
-

soup off:
    user.full_grid_close()

<user.letter> <user.letter> <number>:
    user.full_grid_select(letter_1 + letter_2, number, "")
    user.full_grid_finish()

<user.letter> <user.letter> <number> {user.mg_point_of_compass}:
    user.full_grid_select(letter_1 + letter_2, number, mg_point_of_compass)
    user.full_grid_finish()

<user.letter> <user.letter> {user.mg_point_of_compass}:
    user.full_grid_select(letter_1 + letter_2, -1, mg_point_of_compass)
    user.full_grid_finish()

<user.letter> <user.letter>:
    user.full_grid_select(letter_1 + letter_2, -1, "")
    user.full_grid_finish()

<number> <user.letter> <user.letter>:
    user.full_grid_select(letter_1 + letter_2, number, "")
    user.full_grid_finish()

^<number>$:
    user.full_grid_input_partial(number)

^<user.letter>$:
    user.full_grid_input_partial(letter)

alphabet checkers:
    user.full_grid_checkers_toggle()

alphabet rulers:
    user.full_grid_rulers_toggle()

darker:
    user.full_grid_adjust_label_transparency(50)

lighter:
    user.full_grid_adjust_label_transparency(-50)

toggle hover:
    user.full_grid_set_hover()

toggle drag:
    user.full_grid_set_drag()

toggle click:
    user.full_grid_set_left_click()


