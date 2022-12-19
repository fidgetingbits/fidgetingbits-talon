tag: user.mouse_zoomed
-
(left drag | drag):
    user.mouse_drag(0)
    # close the mouse grid
    user.grid_close()
(right drag | righty drag):
    user.mouse_drag(1)
    # close the mouse grid
    user.grid_close()
(end drag | drag end): user.mouse_drag_end()
