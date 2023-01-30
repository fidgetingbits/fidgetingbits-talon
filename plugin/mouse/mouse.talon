not tag: user.shotbox_showing
-

# Mouse control
mouse control: tracking.control_toggle()
mouse zoom: tracking.control_zoom_toggle()
# XXX: I don't think this function works anymore
camera overlay: tracking.control_debug_toggle()
mouse calibration: tracking.calibrate()

# Basic Clicking
# left click
[mouse] click:
    user.mouse_click(0, 1)
    # End any open drags
    # Left click automatically ends left drags so this is for right drags specifically
    user.mouse_drag_end()
# right click
[mouse] (ricky|right click):
    user.mouse_click(1, 1)
# middle click
[mouse] mid click:
    user.mouse_click(2, 1)
# double click
[mouse] double click:
    user.mouse_click(0, 2)
# triple click
[mouse] triple click:
    user.mouse_click(0, 3)


#see keys.py for modifiers.
#defaults
#command
#control
#option = alt
#shift
#super = windows key
<user.modifiers> click:
    key("{modifiers}:down")
    user.mouse_click(0, 1)
    key("{modifiers}:up")
<user.modifiers> (ricky|right click):
    key("{modifiers}:down")
    user.mouse_click(1, 1)
    key("{modifiers}:up")
:
# Dragging
left drag | drag:
    user.mouse_drag(0)
    user.grid_close()
right drag | righty drag:
    user.mouse_drag(1)
    user.grid_close()
end drag | drag end: user.mouse_drag_end()

# Mouse movement
wheel down: user.mouse_scroll_down()
wheel down here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down()
wheel tiny [down]: user.mouse_scroll_down(0.2)
wheel tiny [down] here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down(0.2)
wheel downer: user.mouse_scroll_down_continuous()
wheel downer here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down_continuous()
wheel up: user.mouse_scroll_up()
wheel up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up()
wheel tiny up: user.mouse_scroll_up(0.2)
wheel tiny up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up(0.2)
wheel upper: user.mouse_scroll_up_continuous()
wheel upper here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up_continuous()
wheel gaze: user.mouse_gaze_scroll()
wheel gaze here:
    user.mouse_move_center_active_window()
    user.mouse_gaze_scroll()
wheel stop: user.mouse_scroll_stop()
wheel stop here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_stop()
wheel left: user.mouse_scroll_left()
wheel left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left()
wheel tiny left: user.mouse_scroll_left(0.5)
wheel tiny left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left(0.5)
wheel right: user.mouse_scroll_right()
wheel right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right()
wheel tiny right: user.mouse_scroll_right(0.5)
wheel tiny right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right(0.5)

# Convenience
copy mouse position: user.copy_mouse_position()
