mode: user.selection_overlay
and not mode: sleep
-

snap mouse:
    user.selection_overlay_snap_mouse()

slide {user.points_of_compass} [<number>]:
    user.selection_overlay_move(points_of_compass, number or 1)

grow [<number>]:
    user.selection_overlay_grow(number or 1)

shrink [<number>]:
    user.selection_overlay_shrink(number or 1)

overlay off:
    user.selection_overlay_close()
