# Somewhat inspired by flameshot
# TODO
# - Add the pixel grid indicated movement/size
# - Allow selecting a point on the rectangle you only move it
# - Indicate the selection size as metadata on the overlay
# - Allow setting a temporary screenshot naming scheme
# - Implement a separate screenshot coordinate history
# - Add the ability to cycle through old selections
# - Add command to center the current selection
# - Configure the screenshot flash color
# - New name
# - Add support for dragging the mouse over the selection

from talon import (
    Module,
    Context,
    app,
    actions,
    canvas,
    screen,
    settings,
    ui,
    ctrl,
    cron,
)
from talon.skia import Shader, Color, Paint, Rect
from talon.types.point import Point2d
from talon_plugins import eye_mouse, eye_zoom_mouse
from typing import Union

import math, time, string

import typing

mod = Module()
mod.tag(
    "selection_overlay_showing",
    desc="Tag indicates whether the selection overlay is showing",
)
mod.tag("selection_overlay_enabled", desc="Tag enables the selection overlay commands.")
mod.list("points_of_compass", desc="point of compass for selection overlay")
mod.mode("selection_overlay", desc="indicate the selection overlay is active")

setting_grow_size = mod.setting(
    "overlay_select_default_grow_size",
    type=int,
    default=5,
    desc="The number of pixels to grow/shrink by default",
)

setting_undo_history_size = mod.setting(
    "overlay_select_undo_history_size",
    type=int,
    default=100,
    desc="The number of box selections to record",
)

setting_snap_to_mouse = mod.setting(
    "overlay_select_start_snapped_to_mouse",
    type=int,
    default=1,
    desc="Whether the default selection on start snaps to mouse",
)

setting_default_x = mod.setting(
    "overlay_select_default_x",
    type=int,
    default=500,
    desc="The default X coordinate",
)

setting_default_y = mod.setting(
    "overlay_select_default_y",
    type=int,
    default=500,
    desc="The default Y coordinate",
)

setting_default_width = mod.setting(
    "overlay_select_default_width",
    type=int,
    default=200,
    desc="The default box width",
)

setting_default_height = mod.setting(
    "overlay_select_default_height",
    type=int,
    default=200,
    desc="The default box height",
)

setting_box_color = mod.setting(
    "overlay_select_box_color",
    type=str,
    default="#FF00FF",
    desc="The default box color",
)



ctx = Context()

ctx.matches = r"""
tag: user.selection_overlay_enabled
"""

direction_name_steps = [
    "east",
    "south east",
    "south",
    "south west",
    "west",
    "north west",
    "north",
    "north east",
]

arrow_name_steps = ["right", "down", "left", "up"]

direction_vectors = [Point2d(0, 0) for _ in range(len(direction_name_steps))]
arrow_vectors = [Point2d(0, 0) for _ in range(len(arrow_name_steps))]

arrow_vectors[0] = direction_vectors[0] = Point2d(1, 0)  # east
arrow_vectors[1] = direction_vectors[2] = Point2d(0, 1)  # south
arrow_vectors[2] = direction_vectors[4] = Point2d(-1, 0)  # west
arrow_vectors[3] = direction_vectors[6] = Point2d(0, -1)  # north

# This edits all single and double entries
for i in [1, 3, 5, 7]:
    direction_vectors[i] = (
        direction_vectors[(i - 1) % len(direction_vectors)]
        + direction_vectors[(i + 1) % len(direction_vectors)]
    ) / 2

ctx.lists["self.points_of_compass"] = direction_name_steps


class SelectionOverlay:
    def __init__(self, debug=False):
        self.debug = debug
        # XXX - Should this be configurable?
        self.screen_num = 1
        self.screen = None
        self.screen_rect = None
        self.history = []
        self.img = None
        self.canvas = None
        self.active = False
        self.columns = 0
        self.rows = 0
        self.field_size = 32  # Breaks overlay into 32-pixel blocks
        self.overlay_transparency = 155  # Out of 255. +5 because we adjust by 50
        self.overlay_color = "000000"
        # XXX - This could be cached somewhere to disk
        self.selection_history = []
        self.selection_history_idx = 0
        self.screen_history = []
        self.screen_history_idx = 0

        self.x = self.default_x = setting_default_x.get()
        self.y = self.default_y = setting_default_y.get()
        self.width = self.default_width = setting_default_width.get()
        self.height = self.default_height = setting_default_height.get()

    def setup(self, *, rect: Rect = None, screen_num: int = None):
        """Initial overlay setup to get screen dimensions, etc"""

        screens = ui.screens()
        # each if block here might set the rect to None to indicate failure
        selected_screen = None
        if rect is not None:
            try:
                selected_screen = ui.screen_containing(*rect.center)
            except Exception:
                rect = None
        if rect is None and screen_num is not None:
            selected_screen = actions.user.screens_get_by_number(screen_num)
            rect = selected_screen.rect
        if rect is None:
            selected_screen = screen.main_screen()
            rect = selected_screen.rect

        print(f"Screen rect {rect}")
        self.screen_num = screen_num
        self.screen_rect = rect.copy()
        self.screen = selected_screen
        self.img = None
        if self.canvas is not None:
            self.canvas.close()
        self.canvas = canvas.Canvas.from_screen(selected_screen)
        if self.active:
            self.canvas.register("draw", self.draw)
            self.canvas.freeze()

        self.columns = int(self.screen_rect.width // self.field_size)
        self.rows = int(self.screen_rect.height // self.field_size)

        self.max_x = self.screen_rect.width
        self.max_y = self.screen_rect.height
        self.max_width = self.screen_rect.width
        self.max_height = self.screen_rect.height

    def set_selection(self, pos):
        """Set the actual coordinates for the current selection"""
        x, y, width, height = pos
        self.x = min(x, self.max_x)
        self.y = min(y, self.max_y)
        self.width = min(width, self.max_width-self.x)
        self.height = min(height, self.max_height-self.y)

    def show(self):
        """Show the selection overlay"""
        if self.active:
            return
        self.set_selection(self.get_last_selection())
        self.canvas.register("draw", self.draw)
        self.canvas.freeze()
        self.active = True

    def close(self):
        """Clear the selection overlay"""
        if not self.active:
            return
        self.canvas.unregister("draw", self.draw)
        self.canvas.close()
        self.canvas = None
        self.img = None
        self.active = False

    def get_mouse_coordinates(self):
        """Get mouse coordinates normalized to the current screen"""
        mouse_x, mouse_y = ctrl.mouse_pos()
        if mouse_x > self.screen_rect.width:
            mouse_x = mouse_x - self.screen_rect.width
        if mouse_y > self.screen_rect.height:
            mouse_y = mouse_y - self.screen_rect.height

        return (mouse_x, mouse_y)

    def snap_mouse(self):
        """Snap the current selection to the last most cursor"""
        self.x, self.y = self.get_mouse_coordinates()
        self.commit()

    def record_selection(self, pos):
        """Record the selection in the history"""
        # If we record a new selection after a redo, we trash all previous
        # redoable entries
        if (self.selection_history_idx) != len(self.selection_history):
            self.selection_history = self.selection_history[
                : self.selection_history_idx - 1
            ]

        if len(self.selection_history) == setting_undo_history_size.get():
            self.selection_history = self.selection_history[1:]
            self.selection_history_idx -= 1

        self.selection_history.append(pos)
        self.selection_history_idx += 1
        print(self.selection_history)

    def default_selection(self):
        """Return the ordinates for the default selection"""

        if setting_snap_to_mouse.get() == 1:
            x, y = self.get_mouse_coordinates()
        else:
            x = self.default_x
            y = self.default_y

        return (x, y, self.default_width, self.default_height)

    def get_last_selection(self, direction=1):
        """Return a rectangle to highlight the last or default selection"""
        if len(self.selection_history) != 0:
            idx = self.selection_history_idx - direction
            if idx < 0:
                idx = 0
            elif idx == len(self.selection_history):
                idx = len(self.selection_history) - 1
            if direction ==  1:
                x, y, width, height = self.selection_history[idx - 1]
            else:
                x, y, width, height = self.selection_history[idx]
            self.selection_history_idx = idx
        else:
            x, y, width, height = self.default_selection()

        print((x, y, width, height))
        return x, y, width, height

    def selected_rect(self):
        """Return a rectangle of the current selection"""
        return Rect(self.x, self.y, self.width, self.height)

    def unclipped_rect(self):
        """Return a rectangle of the current selection without clipping
        to the screen"""
        return Rect(
            self.screen_rect.x + self.x,
            self.screen_rect.y + self.y,
            self.width,
            self.height,
        )

    def draw(self, canvas):
        """Draw an updated canvas"""
        paint = canvas.paint

        # for other-screen or individual-window grids
        # XXX - What is this? Clips the main rectangle boundaries?
        canvas.translate(self.screen_rect.x, self.screen_rect.y)
        canvas.clip_rect(
            Rect(
                -self.field_size * 2,
                -self.field_size * 2,
                self.screen_rect.width + self.field_size * 4,
                self.screen_rect.height + self.field_size * 4,
            )
        )
        # At any given time there are 4 darkened rectangles, and this
        # selection rectangle
        selection_rect = self.selected_rect()
        canvas.paint.color = self.overlay_color + hex_to_string(35)
        canvas.paint.style = Paint.Style.FILL

        # We need to be more careful if this selection dimensions are
        # already on zero?
        overlay_top_x = 0
        overlay_top_y = 0
        overlay_top_width = self.screen_rect.width
        overlay_top_height = selection_rect.y
        overlay_top_rect = Rect(
            overlay_top_x, overlay_top_y, overlay_top_width, overlay_top_height
        )
        if self.debug:
            print("Top:")
            print(overlay_top_rect)

        overlay_left_x = 0
        overlay_left_y = selection_rect.y
        overlay_left_width = selection_rect.x
        overlay_left_height = selection_rect.height
        overlay_left_rect = Rect(
            overlay_left_x, overlay_left_y, overlay_left_width, overlay_left_height
        )
        if self.debug:
            print("Left:")
            print(overlay_left_rect)

        overlay_right_x = selection_rect.x + selection_rect.width
        overlay_right_y = selection_rect.y
        overlay_right_width = self.screen_rect.width - overlay_right_x
        overlay_right_height = selection_rect.height
        overlay_right_rect = Rect(
            overlay_right_x, overlay_right_y, overlay_right_width, overlay_right_height
        )
        if self.debug:
            print("Right:")
            print(overlay_right_rect)

        overlay_bottom_x = 0
        overlay_bottom_y = selection_rect.y + selection_rect.height
        overlay_bottom_width = self.screen_rect.width
        overlay_bottom_height = self.screen_rect.height - overlay_bottom_y
        overlay_bottom_rect = Rect(
            overlay_bottom_x,
            overlay_bottom_y,
            overlay_bottom_width,
            overlay_bottom_height,
        )
        if self.debug:
            print("Bottom:")
            print(overlay_bottom_rect)

        canvas.paint.color = self.overlay_color + hex_to_string(
            self.overlay_transparency
        )
        canvas.paint.style = Paint.Style.FILL

        canvas.draw_rect(overlay_top_rect)
        canvas.draw_rect(overlay_bottom_rect)
        canvas.draw_rect(overlay_left_rect)
        canvas.draw_rect(overlay_right_rect)

        canvas.paint.style = Paint.Style.FILL
        canvas.paint.color = setting_box_color.get()
        margin = 0
        # XXX - Add the margins, and use leftmost = self.x + margin
        # See talon_hud
        canvas.draw_line(self.x, self.y, self.x + self.width, self.y)
        canvas.draw_line(self.x, self.y, self.x, self.y + self.height)
        canvas.draw_line(
            self.x + self.width, self.y, self.x + self.width, self.y + self.height
        )
        canvas.draw_line(
            self.x, self.y + self.height, self.x + self.width, self.y + self.height
        )

        # XXX - circle should be configurable
        # top circles
        canvas.draw_circle(self.x, self.y, 5, None)
        canvas.draw_circle(self.x + (self.width / 2), self.y, 5, None)
        canvas.draw_circle(self.x + self.width, self.y, 5, None)
        # side circles
        canvas.draw_circle(self.x, self.y + (self.height / 2), 5, None)
        canvas.draw_circle(self.x + self.width, self.y + (self.height / 2), 5, None)
        # bottom circles
        canvas.draw_circle(self.x, self.y + self.height, 5, None)
        canvas.draw_circle(self.x + (self.width / 2), self.y + self.height, 5, None)
        canvas.draw_circle(self.x + self.width, self.y + self.height, 5, None)

    def adjust(self, direction, size):
        """Adjust the size of the overlay in all directions by the amount specified"""

        # No explicit direction means adjust in all directions
        if direction == "":
            self.x = self.x - size
            self.y = self.y - size
            # *2 because the sizes will already be adjusted by the new x,y
            self.width = self.width + (size * 2)
            self.height = self.height + (size * 2)
        else:
            if direction.startswith("north") or direction == "up":
                self.y = self.y - size
                self.height = self.height + size
            if direction.startswith("south") or direction == "down":
                self.height = self.height + size
            if "east" in direction or direction == "right":
                self.width = self.width + size
            if "west" in direction or direction == "left":
                self.x = self.x - size
                self.width = self.width + size

        self.commit()

    def set_x(self, x):
        """Set the x coordinate of the current selection"""
        # XXX - Sanity checking of boundary
        self.x = x
        self.commit()

    def set_y(self, y):
        """Set the y coordinate of the current selection"""
        # XXX - Sanity checking of boundary
        self.y = y
        self.commit()

    def set_width(self, width):
        """Set the width of the current selection"""
        # XXX - Sanity  checking of boundary
        self.width = width
        self.commit()

    def set_height(self, height):
        """Set the height of the current selection"""
        # XXX - Sanity  checking of boundary
        self.height = height
        self.commit()

    def set_size(self, width, height):
        """Set the width and height of the current selection"""
        self.width = width
        self.height = height
        self.commit()

    def move(self, direction, count):
        global direction_name_steps
        global direction_vectors
        global arrow_name_steps
        global arrow_vectors
        if direction in direction_name_steps:
            index = direction_name_steps.index(direction)
            point = direction_vectors[index]
        else:
            index = arrow_name_steps.index(direction)
            point = arrow_vectors[index]

        self.x = self.x + (point.x * count)
        self.y = self.y + (point.y * count)
        self.commit()

    def reset(self):
        """Reset the selection to the default boundaries"""
        self.set_selection(self.default_selection())
        self.commit()

    def commit(self):
        """Commit the coordinate adjustments"""
        # We do this to do a boundary sanitation pass
        self.set_selection((self.x, self.y, self.width, self.height))
        self.record_selection((self.x, self.y, self.width, self.height))
        self.canvas.freeze()

    def screenshot(self):
        """Take a screenshot of the current selection"""
        # Temporarily disable overlay
        # XXX - This should be doable without closing everything, maybe
        # just set max transparency...
        self.close()
        selection_rect = self.unclipped_rect()
        # XXX - Have to select this screen?

        actions.user.screenshot_rect(selection_rect, screen_num=self.screen_num)
        self.setup()
        self.show()

    def undo(self):
        """Undo the last selection modification"""
        if len(self.selection_history) == 0:
            return
        self.set_selection(self.get_last_selection(1))
        self.canvas.freeze()

    def redo(self):
        """Redo the last selection modification"""
        if self.selection_history_idx == len(self.selection_history):
            return
        print("Trying to redo")
        self.set_selection(self.get_last_selection(-1))
        self.canvas.freeze()


def hex_to_string(v: int) -> str:
    """Convert hexadecimal integer to string-based transparency hex value"""
    return "{0:x}".format(v)


overlay = SelectionOverlay(debug=False)


def selection_overlay_mode_enable():
    """Enable the selection overlay talon mode"""
    actions.mode.enable("user.selection_overlay")
    actions.mode.disable("command")


def selection_overlay_mode_disable():
    """Disable the selection overlay talon mode"""
    actions.mode.disable("user.selection_overlay")
    actions.mode.enable("command")


@mod.action_class
class SelectionOverlayActions:
    def selection_overlay_activate():
        """Show selection overlay on default screen"""
        if not overlay.canvas:
            overlay.setup()
        overlay.show()
        print("Setting tag")
        ctx.tags = ["user.selection_overlay_showing"]
        selection_overlay_mode_enable()

    def selection_overlay_select_screen(screen_num: int):
        """Brings up mouse grid on the specified screen"""
        overlay.setup(screen_num=screen_num)
        overlay.show()
        ctx.tags = ["user.selection_overlay_showing"]
        selection_overlay_mode_enable()

    def selection_overlay_close():
        """Close the active selection overlay"""
        if overlay.active:
            ctx.tags = []
            overlay.close()
            selection_overlay_mode_disable()

    def selection_overlay_snap_mouse():
        """Snap the current selection to the mouse cursor"""
        overlay.snap_mouse()

    def selection_overlay_grow(direction: str, size: int):
        """Increase the size of the selection from all angles"""
        if size == -1:
            size = setting_grow_size.get()
        overlay.adjust(direction, size)

    def selection_overlay_shrink(direction: str, size: int):
        """Decrease the size of the selection from all angles"""
        if size == -1:
            size = setting_grow_size.get()
        overlay.adjust(direction, -size)

    def selection_overlay_move(direction: str, count: int):
        """Move the selection in some direction"""
        if count == -1:
            count = setting_grow_size.get()
        overlay.move(direction, count)

    def selection_overlay_screenshot():
        """Take a screenshot of the current selection"""
        overlay.screenshot()

    def selection_overlay_set_x(x: int):
        """Set the x coordinate of the current selection"""
        overlay.set_x(x)

    def selection_overlay_set_y(y: int):
        """Set the y coordinate of the current selection"""
        overlay.set_y(y)

    def selection_overlay_set_width(width: int):
        """Set the width of the current selection"""
        overlay.set_width(width)

    def selection_overlay_set_height(height: int):
        """Set the height of the current selection"""
        overlay.set_height(height)

    def selection_overlay_set_size(width: int, height: int):
        """Set the width and height of the current selection"""
        overlay.set_size(width, height)

    def selection_overlay_reset():
        """Reset the selection to the default"""
        overlay.reset()

    def selection_overlay_width_double():
        """Double the width of the selection"""
        overlay.set_width(overlay.width * 2)

    def selection_overlay_height_double():
        """Double the height of the selection"""
        overlay.set_height(overlay.height * 2)

    def selection_overlay_undo():
        """Undo the last selection modification"""
        overlay.undo()

    def selection_overlay_redo():
        """Redo the last selection modification"""
        overlay.redo()
