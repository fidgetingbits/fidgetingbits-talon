tag: user.mouse_guide_enabled
-
(mouse guide | cross hair): user.mouse_guide_toggle()
# for example: mouse 10 up 30 right
mouse <number> {user.mouse_cardinal} <number> {user.mouse_cardinal}:
    user.mouse_cardinal_move_2d(mouse_cardinal_1, number_1, mouse_cardinal_2, number_2)
# for example: mouse 10 up
mouse <number> {user.mouse_cardinal}:
    user.mouse_cardinal_move_1d(mouse_cardinal_1, number_1)
