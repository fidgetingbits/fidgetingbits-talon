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

^<user.number_string>$:
    user.full_grid_input_partial(number_string)

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

darker select:
    user.full_grid_adjust_selector_transparency(50)

lighter select:
    user.full_grid_adjust_selector_transparency(-50)

[toggle] high contrast:
    user.full_grid_toggle_high_contrast()

toggle hover:
    user.full_grid_set_hover()

toggle drag open:
    user.full_grid_set_drag_open()

toggle drag [close]:
    user.full_grid_set_drag_close()

toggle <user.modifiers> drag:
    user.full_grid_set_drag_modifiers(modifiers)
    user.full_grid_set_drag_close()


toggle click:
    user.full_grid_set_left_click()
