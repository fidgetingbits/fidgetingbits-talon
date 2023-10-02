mode: user.shotbox
and not mode: sleep
-

snap [to] mouse: user.shotbox_snap_mouse()

(go | slide | move) ({user.points_of_compass} | {user.arrow_key}) [<number>]:
    user.shotbox_move(arrow_key or points_of_compass, number or -1)

grow [<number>]: user.shotbox_grow("", number or -1)

grow ({user.points_of_compass} | {user.arrow_key}) [<number>]:
    user.shotbox_grow(arrow_key or points_of_compass, number or -1)

shrink [<number>]: user.shotbox_shrink("", number or -1)

shrink ({user.points_of_compass} | {user.arrow_key}) [<number>]:
    user.shotbox_shrink(arrow_key or points_of_compass, number or -1)

shotbox [off]: user.shotbox_close()

# XXX - Rename this command
(grab | take [screen] shot): user.shotbox_screenshot()

set ex <number>: user.shotbox_set_x(number)

set why <number>: user.shotbox_set_y(number)

set width <number>: user.shotbox_set_width(number)

set height <number>: user.shotbox_set_height(number)

set <number> by <number>: user.shotbox_set_size(number_1, number_2)

reset: user.shotbox_reset()

# XXX - We might want to just use the points of compass: ex double north
grow {user.box_multipliers} [{user.box_dimensions}]:
    user.shotbox_grow_multiply(box_multipliers, box_dimensions or "all")

shrink {user.box_multipliers} [{user.box_dimensions}]:
    user.shotbox_shrink_multiply(box_multipliers, box_dimensions or "all")

(undo | nope): user.shotbox_undo()

redo: user.shotbox_redo()

drag: user.shotbox_mouse_drag()

<user.modifiers> drag:
    key("{modifiers}:down")
    user.user.shotbox_mouse_drag()
    key("{modifiers}:up")

cycle: user.shotbox_screenshot_cycle_next()

cycle older: user.shotbox_screenshot_cycle_older()

cycle newer: user.shotbox_screenshot_cycle_newer()

cycle first: user.shotbox_screenshot_cycle_first()

cycle last: user.shotbox_screenshot_cycle_last()
