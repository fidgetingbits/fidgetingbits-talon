tag: user.selection_overlay_enabled
-
overlay on:
    user.selection_overlay_select_screen(1)
    user.selection_overlay_activate()

overlay off:
    user.selection_overlay_close()
