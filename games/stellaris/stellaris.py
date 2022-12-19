# TO DO
# - add cycle for each resource
# - add tab ability to go to next resource
# - add tracking support for states with corresponding tags to enable sub rule
# files
import json
import os
from time import sleep

from talon import Context, Module, actions, ctrl, settings, ui

mod = Module()
# these are used to differentiate between menus with differing hot keys
# they will result in the loading of sub-grammar files
mod.tag("stellaris_government", desc="government screen hot keys")
mod.setting(
    "stellaris_screen_resolution",
    type=str,
    default="2560x1440",
    desc="Default resolution for most coordinates",
)
ctx = Context()
ctx.matches = r"""
app: stellaris
"""

mod.list("stellaris_topbar", desc="list of top bar coordinates locations")
ctx.lists["user.stellaris_topbar"] = []


@mod.capture(rule="{user.stellaris_topbar}")
def stellaris_topbar(m) -> str:
    "Return an stellaris_topbar"
    return m.stellaris_topbar


class Stellaris:

    """Managed database for tracking ts game screen coordinates"""

    def __init__(self):
        """Set up the coordinate database"""
        cwd = os.path.dirname(os.path.realpath(__file__))
        self.coords_file = os.path.join(cwd, "screen_coordinates.json")
        self.resolution = settings.get("user.stellaris_screen_resolution")
        self.resolution = "2560x1440"
        # self.width = self.game_screen.rect.width
        # self.height = self.game_screen.rect.height

        with open(self.coords_file) as f:
            self.db = json.loads(f.read())
        self.coords = self.db[self.resolution]
        # topbar coordinates are isolated to allow to automated cycling
        self.topbar_coords = self.coords["topbar"]
        ctx.lists["user.stellaris_topbar"] = self.topbar_coords.keys()

        # alerts
        self.alert_max = 10  # the maximum we index to the right

        # outliner
        self.outliner = self.coords["outliner"]
        self.outliner_open = False
        self.outliner_state = "idle"

    # XXX - probably can just be a lambda
    def offset_x(self):
        """Find the current windows x offset
        :returns: the current window x offset

        """
        pos = ui.active_window().rect.x
        return 0

    def offset_y(self):
        """Find the current windows y offset
        :returns: the current window y offset

        """
        pos = ui.active_window().rect.y
        return 0

    def get_pos(self, db: dict, entry: str):
        """Query json coordinate adjusted by games screen"""
        pos = db[entry]
        return (pos[0] + self.offset_x(), pos[1] + self.offset_y())

    def hover_topbar(self, name: str):
        """Place the mouse over top of the specified topbar, but no click"""
        x, y = self.topbar_coords[name]
        self.hover(x, y)

    def click_topbar(self, name: str):
        """Place the mouse over top of the specified topbar, then click"""
        x, y = self.topbar_coords[name]
        self.click(x, y)
        self.hover_location("neutral")

    def hover_alert(self, index: int):
        """Placed the mouse over the specified alert index"""
        if index < 1:
            index = 1
        self.alert_x, self.alert_y = self.get_pos(self.coords, "alert_slot_0")
        self.alert_delta, _ = self.get_pos(self.coords, "alert_slot_1")
        self.alert_delta -= self.alert_x
        x = self.alert_x + ((index - 1) * self.alert_delta)
        self.hover(x, self.alert_y)

    def hover_alert_move_direction(self, direction: int):
        """Move the mouse left or right by one alert slot"""

    def hover_location(self, name):
        x, y = self.coords[name]
        self.hover(x, y)

    def hover(self, x, y):
        self.move(x, y, click=False)

    def click_location(self, name):
        x, y = self.coords[name]
        self.click(x, y)

    def click(self, x, y):
        self.move(x, y, click=True)

    def move(self, x, y, click=False):
        actions.user.mouse_disable_control_mouse()
        ctrl.mouse_move(x, y)
        if click:
            ctrl.mouse_click(button=0, hold=16000)

    def toggle_outliner(self):
        """Open or close the outliner window on the right"""
        actions.key("o")
        if self.outliner_state == "closed":
            self.outliner_state = "open"
        else:
            self.outliner_state = "closed"

    def outliner_init(self):
        """Close all of the entries after opening the outliner.

        This assumes that the outliner has been configured to have all of the
        entries opened by default.

        """
        self.toggle_outliner()
        sleep(0.1)
        entries = self.outliner["entries"]
        for entry in entries.keys():
            print(entry)
            sleep(0.075)
            x, y = self.get_pos(entries, entry)
            ctrl.mouse_move(x, y)
            ctrl.mouse_click(button=0, hold=16000)


stellaris = Stellaris()


@mod.action_class
class Actions:
    def stellaris_government():
        """Clicks on the government icon"""
        global stellaris

    def stellaris_outliner():
        """Toggle the outliner in prep for voice usage"""
        global stellaris
        stellaris.outliner_init()

    def stellaris_hover_topbar(name: str):
        """Hover over a specified resource"""
        global stellaris
        stellaris.hover_topbar(name)

    def stellaris_click_topbar(name: str):
        """Click on a specified resource"""
        global stellaris
        stellaris.click_topbar(name)

    def stellaris_hover_alert(index: int):
        """Place the mouse over the specified alert index"""
        global stellaris
        stellaris.hover_alert(index)

    def stellaris_hover_alert_next():
        """Hover the mouse over the next alert to the right"""
        global stellaris
        stellaris.hover_alert_move_direction(1)

    def stellaris_hover_alert_previous():
        """Hover the mouse over the next alert to the right"""
        global stellaris
        stellaris.hover_alert_move_direction(-1)

    def stellaris_hover(name: str):
        """Hover on a specified coordinate"""
        global stellaris
        stellaris.hover_location(name)

    def stellaris_click(name: str):
        """Click on a specified coordinate"""
        global stellaris
        stellaris.click_location(name)
