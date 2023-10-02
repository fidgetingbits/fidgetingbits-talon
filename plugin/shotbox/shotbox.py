# Somewhat inspired by flameshot
# TODO
# - Allow selecting a point on the rectangle so you only move it
# - Indicate the selection size as metadata on the overlay
# - Allow setting a temporary screenshot naming scheme
# - Add command to center the current selection
# - Configure the screenshot flash color
# - Possibly save clipped length and width when moving screen boundaries, so
# when it moves back its going to the original size
# - Sometimes compass doesn't work, sometimes arrows doesn't work
# - Bounds checking still needs also check that the width or height does not
# become negative
# - Setting for if the crosshair grid is enabled by default
# - Add numbers to the crosshair grid
# - Figure out how to speed up closing the canvas, and taking screenshot
# - Allows cycling windows?
# - Allow flushing both caches
# - Make current window selection seamless, it doesn't show the original
# selection at first
# - Make mouse snapping go to this center of the mouse?

import json
import pathlib

from talon import Context, Module, actions, canvas, ctrl, screen, ui
from talon.skia import Paint, Rect
from talon.types.point import Point2d
from talon_init import TALON_HOME

mod = Module()
mod.tag(
    "shotbox_showing",
    desc="Tag indicates whether shotbox is showing",
)
mod.tag("shotbox_enabled", desc="Tag enables shotbox commands.")
mod.list("points_of_compass", desc="Point of compass for shotbox")
mod.list("box_multipliers", desc="Multipliers for growing/shrinking the box")
mod.list("box_dimensions", desc="Box dimensions for multiplication")
mod.mode("shotbox", desc="Indicate shotbox is active")

setting_grow_size = mod.setting(
    "shotbox_default_grow_size",
    type=int,
    default=5,
    desc="The number of pixels to grow/shrink by default",
)

setting_undo_history_size = mod.setting(
    "shotbox_undo_history_size",
    type=int,
    default=100,
    desc="The number of box selections to record",
)

setting_screenshot_history_size = mod.setting(
    "shotbox_screenshot_history_size",
    type=int,
    default=100,
    desc="The number of screenshot selections to record",
)

setting_snap_to_mouse = mod.setting(
    "shotbox_start_snapped_to_mouse",
    type=int,
    default=1,
    desc="Whether the default selection on start snaps to mouse",
)

setting_default_x = mod.setting(
    "shotbox_default_x",
    type=int,
    default=500,
    desc="The default X coordinate",
)

setting_default_y = mod.setting(
    "shotbox_default_y",
    type=int,
    default=500,
    desc="The default Y coordinate",
)

setting_default_width = mod.setting(
    "shotbox_default_width",
    type=int,
    default=200,
    desc="The default box width",
)

setting_default_height = mod.setting(
    "shotbox_default_height",
    type=int,
    default=200,
    desc="The default box height",
)

setting_box_color = mod.setting(
    "shotbox_box_color",
    type=str,
    default="#FF00FF",
    desc="The default box color",
)


ctx = Context()

ctx.matches = r"""
tag: user.shotbox_enabled
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
ctx.lists["self.box_multipliers"] = ["double", "triple", "half"]
ctx.lists["self.box_dimensions"] = ["width", "length", "height", "all"]


class ShotBox:
    def __init__(self, debug=False):
        self.debug = debug
        # XXX - Should this be configurable?
        self.screen_num = 1
        self.screen = None
        self.screen_rect = None
        self.img = None
        self.canvas = None
        self.active = False

        # XXX - we don't use the next three fields atm
        self.columns = 0
        self.rows = 0
        self.field_size = 32  # Breaks overlay into 32-pixel blocks

        # Theming
        self.overlay_transparency = 155  # Out of 255. +5 because we adjust by 50
        self.overlay_color = "000000"

        # Caching
        self.selection_history = []
        self.selection_history_idx = 0
        self.screenshot_history = []
        self.screenshot_history_idx = 0
        self.cycle_direction = 1
        self.cache_folder = pathlib.Path(TALON_HOME, "cache/shotbox/")
        self.selection_history_file = self.cache_folder / "selection.json"
        self.screenshot_history_file = self.cache_folder / "screenshots.json"
        self.init_cache()

        # Coordinates
        self.x = self.default_x = setting_default_x.get()
        self.y = self.default_y = setting_default_y.get()
        self.width = self.default_width = setting_default_width.get()
        self.height = self.default_height = setting_default_height.get()

    def init_cache(self):
        """Make sure all cache files and folders exist"""
        self.cache_folder.mkdir(parents=True, exist_ok=True)
        # XXX - The two below could be copied into one function...
        self.selection_history_file.touch()
        with self.selection_history_file.open() as f:
            try:
                history = json.load(f)
                if len(history) > 0:
                    self.selection_history_idx = len(history) - 1
                self.selection_history = history
            except Exception:
                pass
            # print(self.selection_history)

        self.screenshot_history_file.touch()
        with self.screenshot_history_file.open() as f:
            try:
                history = json.load(f)
                if len(history) > 0:
                    self.screenshot_history_idx = len(history) - 1
                self.screenshot_history = history
            except Exception:
                pass
            # print(self.screenshot_history)

    def setup(self, *, rect: Rect = None, screen_num: int = None):
        """Initial overlay setup to get screen dimensions, etc"""

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

        self.screen_num = screen_num
        self.screen_rect = rect.copy()
        self.screen = selected_screen
        self.img = None
        if self.canvas is not None:
            self.canvas.close()
        self.canvas = canvas.Canvas.from_screen(selected_screen)
        if self.active:
            self.canvas.register("draw", self.draw_box)
            self.canvas.freeze()

        self.columns = int(self.screen_rect.width // self.field_size)
        self.rows = int(self.screen_rect.height // self.field_size)

        self.max_x = self.screen_rect.width
        self.max_y = self.screen_rect.height
        self.max_width = self.screen_rect.width
        self.max_height = self.screen_rect.height

    def set_selection_rect(self, rect):
        """Set the actual coordinates for the rect"""
        self.set_selection((rect.x, rect.y, rect.width, rect.height))

    def set_selection(self, pos):
        """Set the actual coordinates for the current selection"""
        x, y, width, height = pos
        self.x = min(x, self.max_x)
        self.y = min(y, self.max_y)
        self.width = min(width, self.max_width - self.x)
        self.height = min(height, self.max_height - self.y)

    def show(self):
        """Show the shotbox overlay"""
        if self.active:
            return
        self.set_selection(self.get_last_selection(direction=0))
        self.canvas.register("draw", self.draw_box)
        self.canvas.freeze()
        self.active = True

    def close(self):
        """Clear the shotbox overlay"""
        if not self.active:
            return
        self.canvas.unregister("draw", self.draw_box)
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
                : self.selection_history_idx
            ]

        if len(self.selection_history) == setting_undo_history_size.get():
            self.selection_history = self.selection_history[1:]
            self.selection_history_idx -= 1

        self.selection_history.append(pos)
        self.selection_history_idx += 1

        # Commit to file
        with self.selection_history_file.open("w+") as f:
            json.dump(self.selection_history, f)

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
            if self.debug:
                print(f"Calculated index: {idx}")
                print(f"History length: {len(self.selection_history)}")
            if idx < 0:
                idx = 0
            elif idx == len(self.selection_history):
                idx = len(self.selection_history) - 1
            if direction == 1:
                x, y, width, height = self.selection_history[idx - 1]
            else:
                x, y, width, height = self.selection_history[idx]
            self.selection_history_idx = idx
        else:
            x, y, width, height = self.default_selection()

        return x, y, width, height

    def selected_rect(self):
        """Return a rectangle of the current selection"""
        return Rect(self.x, self.y, self.width, self.height)

    # XXX - This will only work for duel monitors at the moment?
    def clip_rect(self, rect):
        """Clip a rectangle to fit on the current canvas"""

        if rect.x >= self.screen_rect.x or rect.y < self.screen_rect.y:
            new_x = rect.x
            new_y = rect.y
            if rect.x >= self.screen_rect.x:
                new_x = rect.x - self.screen_rect.x
            if rect.y >= self.screen_rect.y:
                new_y = rect.y - self.screen_rect.y
            return Rect(new_x, new_y, rect.width, rect.height)
        else:
            return rect

    def unclipped_rect(self):
        """Return a rectangle of the current selection without clipping
        to the screen"""
        return Rect(
            self.screen_rect.x + self.x,
            self.screen_rect.y + self.y,
            self.width,
            self.height,
        )

    def unclipped_selection(self):
        """Return current selection ordinates without clipping to the screen"""
        return (
            self.screen_rect.x + self.x,
            self.screen_rect.y + self.y,
            self.width,
            self.height,
        )

    def draw_grid(self, canvas):
        """Draw the grid over the non-selected portion"""

        # This was largely taken from mouse_guide.py
        SMALL_DIST = 5
        SMALL_LENGTH = 5
        SMALL_COLOR = setting_box_color.get()
        MID_DIST = 10
        MID_LENGTH = 10
        MID_COLOR = setting_box_color.get()
        LARGE_DIST = 50
        LARGE_LENGTH = 20
        LARGE_COLOR = setting_box_color.get()
        canvas.paint.antialias = False

        irange = lambda start, stop, step: range(int(start), int(stop), int(step))

        rect = self.selected_rect()
        cx, cy = rect.center
        margin = 200  # How many pixels around the box to paint

        for tick_dist, tick_length, color in (
            (SMALL_DIST, SMALL_LENGTH, SMALL_COLOR),
            (MID_DIST, MID_LENGTH, MID_COLOR),
            (LARGE_DIST, LARGE_LENGTH, LARGE_COLOR),
        ):
            half = tick_length // 2
            canvas.paint.color = color
            # top
            for y in irange(rect.top - margin - 1, rect.top - 1, tick_dist):
                canvas.draw_line(cx - half, y, cx + half, y)
            # bottom
            for y in irange(rect.bot + tick_dist, rect.bot + margin + 1, tick_dist):
                canvas.draw_line(cx - half, y, cx + half, y)
            # left
            for x in irange(rect.left - margin - 1, rect.left - 1, tick_dist):
                canvas.draw_line(x, cy - half, x, cy + half)
            # right
            for x in irange(rect.right + tick_dist, rect.right + margin + 1, tick_dist):
                canvas.draw_line(x, cy - half, x, cy + half)

    def draw_box(self, canvas):
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

        self.draw_grid(canvas)

    def adjust(self, direction, size):
        """Adjust the size of the overlay in direction specified.

        Note that the direction meaning is inverse during shrinkage, because if
        you say shrink up you don't actually want that top to shrink...
        """

        # No explicit direction means adjust in all directions
        if direction == "":
            self.x = self.x - size
            self.y = self.y - size
            # *2 because the sizes will already be adjusted by the new x,y
            self.width = self.width + (size * 2)
            self.height = self.height + (size * 2)
        else:
            if direction.startswith("north") or direction == "up":
                if size < 0:
                    # Shrinking
                    self.height = self.height + size
                else:
                    # Growing
                    self.y = self.y - size
                    self.height = self.height + size
            if direction.startswith("south") or direction == "down":
                if size < 0:
                    # Shrinking
                    self.y = self.y - size
                    self.height = self.height + size
                else:
                    # Growing
                    self.height = self.height + size
            if "east" in direction or direction == "right":
                if size < 0:
                    # Shrinking
                    self.x = self.x - size
                    self.width = self.width + size

                else:
                    self.width = self.width + size
            if "west" in direction or direction == "left":
                if size < 0:
                    # Shrinking

                    self.width = self.width + size
                else:
                    self.x = self.x - size
                    self.width = self.width + size

        self.commit()

    def set_x(self, x):
        """Set the x coordinate of the current selection"""
        self.x = x
        self.commit()

    def set_y(self, y):
        """Set the y coordinate of the current selection"""
        self.y = y
        self.commit()

    def set_width(self, width):
        """Set the width of the current selection"""
        self.width = width
        self.commit()

    def set_height(self, height):
        """Set the height of the current selection"""
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

        if len(self.screenshot_history) == setting_screenshot_history_size.get():
            self.screenshot_history = self.screenshot_history[1:]

        # XXX - This should record this screen number and coordinates
        self.screenshot_history.append((self.x, self.y, self.width, self.height))
        self.screenshot_history_idx += 1
        with self.screenshot_history_file.open("w+") as f:
            json.dump(self.screenshot_history, f)

        # XXX - if I don't just completely disable it, it seems to race with
        # this screenshot taking and sleeps are not super reliable (unless
        # their painfully long)
        self.disable()
        rect = self.unclipped_rect()
        actions.user.screenshot_rect(rect, screen_num=self.screen_num)
        self.screenshot_history_idx = -1

    def screenshot_next(self):
        """Cycle to the next screenshot based off the previously used direction"""
        self.screenshot_cycle(self.cycle_direction)

    # XXX - it would be nice to show which screenshot in the text somewhere
    def screenshot_cycle(self, direction):
        """Cycle to the next screenshot in the specified direction"""
        if len(self.screenshot_history) == 0:
            return
        self.cycle_direction = direction
        idx = self.screenshot_history_idx
        if idx == -1:
            idx = len(self.screenshot_history) - 1
        else:
            if direction > 0:
                idx -= 1
            elif direction < 0:
                idx += 1

        self.screenshot_select(idx)

    def screenshot_select(self, idx):
        self.screenshot_history_idx = idx
        self.set_selection(self.screenshot_history[self.screenshot_history_idx])
        self.commit()

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
        self.set_selection(self.get_last_selection(-1))
        self.canvas.freeze()

    def mouse_drag(self, modifiers=None):
        """Drag the mouse across the current selection"""
        x, y, width, height = self.unclipped_selection()
        start_x = x
        start_y = y
        end_x = x + width
        end_y = y + height
        self.disable()

        ctrl.mouse_move(
            start_x,
            start_y,
        )

        ctrl.mouse_click(0, down=True)
        # Let the underlying application react
        actions.sleep(0.05)
        ctrl.mouse_move(
            end_x,
            end_y,
        )
        ctrl.mouse_click(0, up=True)

    def disable(self):
        """Disable the shotbox overlay"""
        # XXX - I don't like that this access is context
        global ctx
        ctx.tags = []
        self.close()
        shotbox_mode_disable()


def hex_to_string(v: int) -> str:
    """Convert hexadecimal integer to string-based transparency hex value"""
    return f"{v:x}"


shotbox = ShotBox(debug=False)


def shotbox_mode_enable():
    """Enable shotbox"""
    actions.mode.enable("user.shotbox")
    actions.mode.disable("command")


def shotbox_mode_disable():
    """Disable shotbox"""
    actions.mode.disable("user.shotbox")
    actions.mode.enable("command")


@mod.action_class
class ShotBoxActions:
    def shotbox_activate():
        """Show the shotbox overlay on default screen"""
        if not shotbox.canvas:
            shotbox.setup()
        shotbox.show()
        ctx.tags = ["user.shotbox_showing"]
        shotbox_mode_enable()

    def shotbox_activate_win():
        """Show the shotbox overlay on default screen, highlighting active window"""
        actions.user.shotbox_activate()
        win = ui.active_window()
        shotbox.set_selection(shotbox.clip_rect(win.rect))
        shotbox.commit()

    def selection_shotbox_screen(screen_num: int):
        """Brings up overlay on the specified screen"""
        shotbox.setup(screen_num=screen_num)
        shotbox.show()
        ctx.tags = ["user.shotbox_showing"]
        shotbox_mode_enable()

    def shotbox_close():
        """Close the active shotbox overlay"""
        if shotbox.active:
            ctx.tags = []
            shotbox.close()
            shotbox_mode_disable()

    def shotbox_snap_mouse():
        """Snap the current selection to the mouse cursor"""
        shotbox.snap_mouse()

    def shotbox_grow(direction: str, size: int):
        """Increase the size of the selection from all angles"""
        if size == -1:
            size = setting_grow_size.get()
        shotbox.adjust(direction, size)

    def shotbox_shrink(direction: str, size: int):
        """Decrease the size of the selection from all angles"""
        if size == -1:
            size = setting_grow_size.get()
        shotbox.adjust(direction, -size)

    def shotbox_move(direction: str, count: int):
        """Move the selection in some direction"""
        if count == -1:
            count = setting_grow_size.get()
        shotbox.move(direction, count)

    def shotbox_screenshot():
        """Take a screenshot of the current selection"""
        shotbox.screenshot()

    def shotbox_set_x(x: int):
        """Set the x coordinate of the current selection"""
        shotbox.set_x(x)

    def shotbox_set_y(y: int):
        """Set the y coordinate of the current selection"""
        shotbox.set_y(y)

    def shotbox_set_width(width: int):
        """Set the width of the current selection"""
        shotbox.set_width(width)

    def shotbox_set_height(height: int):
        """Set the height of the current selection"""
        shotbox.set_height(height)

    def shotbox_set_size(width: int, height: int):
        """Set the width and height of the current selection"""
        shotbox.set_size(width, height)

    def shotbox_reset():
        """Reset the selection to the default"""
        shotbox.reset()

    def shotbox_grow_multiply(multiplier: str, direction: str):
        """Adjust the box by a multiplayer"""
        multipliers = {"double": 2, "triple": 3, "half": 1.5}
        m = multipliers[multiplier]
        if direction == "width" or direction == "length":
            shotbox.set_width(shotbox.width * m)
        elif direction == "height":
            shotbox.set_height(shotbox.height * m)
        elif direction == "all":
            shotbox.set_width(shotbox.width * m)
            shotbox.set_height(shotbox.height * m)

    def shotbox_shrink_multiply(multiplier: str, direction: str):
        """Adjust the box by a multiplayer"""
        multipliers = {"double": 0.5, "triple": 0.25, "half": 0.5}
        m = multipliers[multiplier]
        if direction == "width" or direction == "length":
            shotbox.set_width(shotbox.width * m)
        elif direction == "height":
            shotbox.set_height(shotbox.height * m)
        elif direction == "all":
            shotbox.set_width(shotbox.width * m)
            shotbox.set_height(shotbox.height * m)

    def shotbox_undo():
        """Undo the last selection modification"""
        shotbox.undo()

    def shotbox_redo():
        """Redo the last selection modification"""
        shotbox.redo()

    def shotbox_mouse_drag():
        """Drag the mouse over the current selection box"""
        shotbox.mouse_drag()

    def shotbox_screenshot_cycle_next():
        """Cycle to the next screenshot based off the previous direction"""
        shotbox.screenshot_next()

    def shotbox_screenshot_cycle_older():
        """Cycle to the next oldest screenshot based off the previous direction"""
        shotbox.screenshot_cycle(-1)

    def shotbox_screenshot_cycle_newer():
        """Cycle to the next newer screenshot based off the previous direction"""
        shotbox.screenshot_cycle(1)

    def shotbox_screenshot_cycle_first():
        """Cycle to the first screenshot in the cache"""
        shotbox.screenshot_select(0)

    def shotbox_screenshot_cycle_last():
        """Cycle to the last screenshot in the cache"""
        shotbox.screenshot_select(len(shotbox.screenshot_history) - 1)
