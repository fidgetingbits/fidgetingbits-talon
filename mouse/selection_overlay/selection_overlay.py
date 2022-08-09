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

ctx = Context()

ctx.matches = r"""
tag: user.selection_overlay_enabled
"""

# XXX - Understand how this works better
# XXX - Add basic directions as well
direction_name_steps = [
    "east",
    "east south east",
    "south east",
    "south south east",
    "south",
    "south south west",
    "south west",
    "west south west",
    "west",
    "west north west",
    "north west",
    "north north west",
    "north",
    "north north east",
    "north east",
    "east north east",
]

direction_vectors = [Point2d(0, 0) for _ in range(len(direction_name_steps))]

direction_vectors[0] = Point2d(1, 0)  # east
direction_vectors[4] = Point2d(0, 1)  # south
direction_vectors[8] = Point2d(-1, 0)  # west
direction_vectors[12] = Point2d(0, -1)  # north

# This edits the triple entry ones
for i in [2, 6, 10, 14]:
    direction_vectors[i] = (
        direction_vectors[(i - 2) % len(direction_vectors)]
        + direction_vectors[(i + 2) % len(direction_vectors)]
    )

# This edits all single and double entries
for i in [1, 3, 5, 7, 9, 11, 13, 15]:
    direction_vectors[i] = (
        direction_vectors[(i - 1) % len(direction_vectors)]
        + direction_vectors[(i + 1) % len(direction_vectors)]
    ) / 2

ctx.lists["self.points_of_compass"] = direction_name_steps


class SelectionOverlay:
    def __init__(self, debug=False):
        self.debug = debug
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
        # XXX - These should be configurable in settings
        self.default_x = 100
        self.default_y = 100
        self.default_width = 100
        self.default_height = 100

        # Set to the default or last selection prior to draw
        self.x = 100
        self.y = 100
        self.width = 100
        self.height = 100

    def setup(self, *, rect: Rect = None, screen_num: int = None):
        """Initial overlay setup to get screen dimensions, etc"""

        screens = ui.screens()
        # each if block here might set the rect to None to indicate failure
        if rect is not None:
            try:
                screen = ui.screen_containing(*rect.center)
            except Exception:
                rect = None
        if rect is None and screen_num is not None:
            screen = screens[screen_num % len(screens)]
            rect = screen.rect
        if rect is None:
            screen = screens[0]
            rect = screen.rect
        print(f"Screen rect {rect}")
        self.screen_rect = rect.copy()
        self.screen = screen
        self.img = None
        if self.canvas is not None:
            self.canvas.close()
        self.canvas = canvas.Canvas.from_screen(screen)
        if self.active:
            self.canvas.register("draw", self.draw)
            self.canvas.freeze()

        self.columns = int(self.screen_rect.width // self.field_size)
        self.rows = int(self.screen_rect.height // self.field_size)

    def show(self):
        """Show the selection overlay"""
        if self.active:
            return
        self.x, self.y, self.width, self.height = self.get_selection()
        self.canvas.register("draw", self.draw)
        self.canvas.freeze()
        self.active = True

        # actions.user.full_mouse_grid_help_overlay_show()

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
        # XXX - in force some selection limit
        self.selection_history.append(pos)

    def get_selection(self):
        """Return a rectangle to highlight the last or default selection"""
        if len(self.selection_history) != 0:
            x, y, width, height = self.selection_history[-1]
        else:
            # XXX - We may want to make snapping to the mouse by default
            # optional...
            mouse_x, mouse_y = self.get_mouse_coordinates()
            x, y, width, height = (
                mouse_x,
                mouse_y,
                self.default_width,
                self.default_height,
            )
            self.record_selection((x, y, width, height))

        return x, y, width, height

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
        selection_rect = Rect(self.x, self.y, self.width, self.height)
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

    def adjust(self, size):
        """Adjust the size of the overlay in all directions by the amount specified"""
        # XXX - Add a direction for resizing
        self.x = self.x - size
        self.y = self.y - size
        # *2 because the sizes will already be adjusted by the new x,y
        self.width = self.width + (size * 2)
        self.height = self.height + (size * 2)
        self.commit()

    def move(self, direction, count):
        global direction_name_steps
        global direction_vectors
        index = direction_name_steps.index(direction)
        point = direction_vectors[index]
        self.x = self.x + (point.x * count)
        self.y = self.y + (point.y * count)
        self.commit()

    def commit(self):
        """Commit the cord nat adjustments"""
        self.record_selection((self.x, self.y, self.width, self.height))
        self.canvas.freeze()


def hex_to_string(v: int) -> str:
    """Convert hexadecimal integer to string-based transparency hex value"""
    return "{0:x}".format(v)


overlay = SelectionOverlay(debug=False)


def selection_overlay_mode_enable():
    """Enable the selection overlay talon mode"""
    print("Enabling selection overlay mode")
    actions.mode.enable("user.selection_overlay")
    actions.mode.disable("command")


def selection_overlay_mode_disable():
    """Disable the selection overlay talon mode"""
    print("Disabling selection overlay mode")
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
        print(ctx.tags)
        selection_overlay_mode_enable()

    def selection_overlay_select_screen(screen: int):
        """Brings up mouse grid on the specified screen"""
        overlay.setup(screen_num=screen - 1)
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

    def selection_overlay_grow(size: int):
        """Increase the size of the selection from all angles"""
        overlay.adjust(size)

    def selection_overlay_shrink(size: int):
        """Decrease the size of the selection from all angles"""
        overlay.adjust(-size)

    def selection_overlay_move(direction: str, count: int):
        """Move the selection in some direction"""
        overlay.move(direction, count)
