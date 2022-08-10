mode: user.selection_overlay
and not mode: sleep
-

snap mouse:
    user.selection_overlay_snap_mouse()

(go|slide|move) ({user.points_of_compass}|{user.arrow_key}) [<number>]:
    user.selection_overlay_move(arrow_key orpoints_of_compass, number or -1)

grow [<number>]:
    user.selection_overlay_grow('', number or -1)

grow ({user.points_of_compass}|{user.arrow_key}) [<number>]:
    user.selection_overlay_grow(arrow_key or points_of_compass, number or -1)

shrink [<number>]:
    user.selection_overlay_shrink('', number or -1)

shrink ({user.points_of_compass}|{user.arrow_key}) [<number>]:
    user.selection_overlay_shrink(arrow_key or points_of_compass, number or -1)

overlay [off]:
    user.selection_overlay_close()

grab:
    user.selection_overlay_screenshot()

set ex <number>:
    user.selection_overlay_set_x(number)

set why <number>:
    user.selection_overlay_set_y(number)

set width <number>:
    user.selection_overlay_set_width(number)

set height <number>:
    user.selection_overlay_set_height(number)

set <number> by <number>:
    user.selection_overlay_set_size(number_1, number_2)

reset:
    user.selection_overlay_reset()

# XXX - We might want to just use the points of compass: ex double north
double (width|length):
    user.selection_overlay_width_double()

double height:
    user.selection_overlay_height_double()

undo:
    user.selection_overlay_undo()

redo:
    user.selection_overlay_redo()
