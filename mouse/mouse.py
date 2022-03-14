import os
import time


from talon import (
    Module,
    actions,
    app,
    clip,
    cron,
    ctrl,
    imgui,
    noise,
    ui,
)
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control

key = actions.key
self = actions.self
scroll_amount = 0
click_job = None
scroll_job = None
gaze_job = None
cancel_scroll_on_pop = True
control_mouse_forced = False

default_cursor = {
    "AppStarting": r"%SystemRoot%\Cursors\aero_working.ani",
    "Arrow": r"%SystemRoot%\Cursors\aero_arrow.cur",
    "Hand": r"%SystemRoot%\Cursors\aero_link.cur",
    "Help": r"%SystemRoot%\Cursors\aero_helpsel.cur",
    "No": r"%SystemRoot%\Cursors\aero_unavail.cur",
    "NWPen": r"%SystemRoot%\Cursors\aero_pen.cur",
    "Person": r"%SystemRoot%\Cursors\aero_person.cur",
    "Pin": r"%SystemRoot%\Cursors\aero_pin.cur",
    "SizeAll": r"%SystemRoot%\Cursors\aero_move.cur",
    "SizeNESW": r"%SystemRoot%\Cursors\aero_nesw.cur",
    "SizeNS": r"%SystemRoot%\Cursors\aero_ns.cur",
    "SizeNWSE": r"%SystemRoot%\Cursors\aero_nwse.cur",
    "SizeWE": r"%SystemRoot%\Cursors\aero_ew.cur",
    "UpArrow": r"%SystemRoot%\Cursors\aero_up.cur",
    "Wait": r"%SystemRoot%\Cursors\aero_busy.ani",
    "Crosshair": "",
    "IBeam": "",
}

# todo figure out why notepad++ still shows the cursor sometimes.
hidden_cursor = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), r"Resources\HiddenCursor.cur"
)

mod = Module()
mod.list(
    "mouse_button", desc="List of mouse button words to mouse_click index parameter"
)
mod.tag(
    "mouse_cursor_commands_enable", desc="Tag enables hide/show mouse cursor commands"
)
setting_mouse_enable_on_startup = mod.setting(
    "mouse_enable_on_startup",
    type=int,
    default=1,
    desc="Enable the mouse on startup without having to issue command.",
)
setting_mouse_enable_pop_click = mod.setting(
    "mouse_enable_pop_click",
    type=int,
    default=0,
    desc="Enable pop to click when control mouse is enabled.",
)
setting_mouse_enable_zoom_auto_click = mod.setting(
    "mouse_enable_zoom_auto_click",
    type=int,
    default=0,
    desc="Enable zoom to auto click after the configured time out",
)

setting_mouse_zoom_auto_click_timeout = mod.setting(
    "mouse_zoom_auto_click_timeout",
    type=float,
    default=1,
    desc="The time in seconds to delay auto clicking after a zoom occurs",
)
setting_mouse_enable_pop_stops_scroll = mod.setting(
    "mouse_enable_pop_stops_scroll",
    type=int,
    default=0,
    desc="When enabled, pop stops continuous scroll modes (wheel upper/downer/gaze)",
)
setting_mouse_wake_hides_cursor = mod.setting(
    "mouse_wake_hides_cursor",
    type=int,
    default=0,
    desc="When enabled, mouse wake will hide the cursor. mouse_wake enables zoom mouse.",
)
setting_mouse_control_mouse = mod.setting(
    "mouse_control_mouse",
    type=int,
    default=0,
    desc="When enabled, mouse wake will automatically cause the cursor to track your eyes",
)

setting_mouse_control_mouse_zoom = mod.setting(
    "mouse_control_mouse_zoom",
    type=int,
    default=1,
    desc="When enabled, mouse wake will automatically cause the cursor to track your eyes, using zoom",
)

setting_mouse_hide_mouse_gui = mod.setting(
    "mouse_hide_mouse_gui",
    type=int,
    default=0,
    desc="When enabled, the 'Scroll Mouse' GUI will not be shown.",
)
setting_mouse_continuous_scroll_amount = mod.setting(
    "mouse_continuous_scroll_amount",
    type=int,
    default=80,
    desc="The default amount used when scrolling continuously",
)
setting_mouse_wheel_down_amount = mod.setting(
    "mouse_wheel_down_amount",
    type=int,
    default=120,
    desc="The amount to scroll up/down (equivalent to mouse wheel on Windows by default)",
)
setting_mouse_wheel_horizontal_amount = mod.setting(
    "mouse_wheel_horizontal_amount",
    type=int,
    default=40,
    desc="The amount to scroll left/right",
)

continuous_scroll_mode = ""


@imgui.open(x=700, y=0)
def gui_wheel(gui: imgui.GUI):
    gui.text("Scroll mode: {}".format(continuous_scroll_mode))
    gui.line()
    if gui.button("Wheel Stop [stop scrolling]"):
        actions.user.mouse_scroll_stop()


# XXX - add gui for showing cursor positions
class MouseTracker(object):

    """Tracks and gives mouse positions"""

    def __init__(self):
        """Prepare the tracking stack"""
        self.cursor_log = []
        self.max_log_size = 10

    def log_cursor(self):
        """Store the most most recent mouse position."""
        if len(self.cursor_log) > self.max_log_size:
            self.cursor_log.pop(0)
        self.cursor_log.append(ctrl.mouse_pos())


def mouse_wake():
    """Enable control mouse, zoom mouse, and disables cursor"""
    time.sleep(1)
    if setting_mouse_control_mouse_zoom.get() >= 1:
        eye_zoom_mouse.toggle_zoom_mouse(True)
    if setting_mouse_control_mouse.get() >= 1:
        eye_mouse.control_mouse.enable()
    if setting_mouse_wake_hides_cursor.get() >= 1:
        show_cursor_helper(False)


@mod.action_class
class Actions:
    def mouse_center():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.main_screen().rect
        center = (rect.x + rect.width / 2, rect.y + rect.height / 2)
        ctrl.mouse_move(center)

    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the active window"""

        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))

    def mouse_click(button: int, count: int):
        """Click the specified mouse button a certain number of times."""
        for i in range(count):
            ctrl.mouse_click(button=button)
        if (
            eye_zoom_mouse.zoom_mouse.enabled
            and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE
        ):
            eye_zoom_mouse.zoom_mouse.cancel()

    def mouse_show_cursor():
        """Shows the cursor"""
        show_cursor_helper(True)

    def mouse_hide_cursor():
        """Hides the cursor"""
        show_cursor_helper(False)

    def mouse_wake():
        """Enable control mouse, zoom mouse, and disables cursor"""
        app.notify(subtitle="Waking mouse")
        mouse_wake()

    def mouse_calibrate():
        """Start calibration"""
        eye_mouse.calib_start()

    def mouse_enable_control_mouse():
        """Enables control mouse if disabled"""
        if not config.control_mouse:
            toggle_control(True)

    def mouse_disable_control_mouse():
        """Disables control mouse if enabled"""
        if config.control_mouse:
            toggle_control(False)

    def mouse_toggle_control_mouse():
        """Toggles control mouse"""
        if not config.control_mouse:
            app.notify(subtitle="Control mouse: ON")
        else:
            app.notify(subtitle="Control mouse: OFF")
        toggle_control(not config.control_mouse)

    def mouse_toggle_camera_overlay():
        """Toggles camera overlay"""
        toggle_camera_overlay(not config.show_camera)

    def mouse_toggle_zoom_mouse():
        """Toggles zoom mouse setting"""
        eye_zoom_mouse.toggle_zoom_mouse(not eye_zoom_mouse.zoom_mouse.enabled)
        s = "Zoom mouse: "
        if eye_zoom_mouse.zoom_mouse.enabled:
            s += "ENABLED"
        else:
            s += "DISABLED"
        app.notify(subtitle=s)

    def mouse_cancel_zoom_mouse():
        """Cancel zoom mouse if pending"""
        if (
            eye_zoom_mouse.zoom_mouse.enabled
            and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE
        ):
            eye_zoom_mouse.zoom_mouse.cancel()

    # XXX - you should all get a property to test zoom mouse enabled
    def mouse_zoom_single_click(count: int = 1):
        """Click the mouse and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, count)

    def mouse_zoom_click(count: int = 1):
        """Click the mouse count times and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, count)

    def mouse_zoom_single_click():
        """Click the mouse, prime one click, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 1)

    def mouse_zoom_double_click():
        """Click the mouse, prime two clicks, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 2)

    def mouse_zoom_triple_click():
        """Click the mouse, prime three clicks, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 3)

    def mouse_move_cursor():
        """Move the cursor but don't actually click, and disable control mouse"""
        if config.control_mouse:
            eye_mouse.control_mouse.disable()
        _, origin = eye_zoom_mouse.zoom_mouse.get_pos()
        ctrl.mouse_move(origin.x, origin.y)

    def mouse_capture_coordinates():
        """copy the current coordinate tuple to the clipboard"""
        print(ctrl.mouse_pos())
        x, y = ctrl.mouse_pos()
        clip.set_text(f"{x},{y}")

    def mouse_zoom_move_cursor():
        """Move the cursor but don't actually click, an zoom if necessary"""
        if not config.control_mouse:
            eye_zoom_mouse.zoom_mouse.on_pop(0, 1, auto=False, click=False)

    def mouse_zoom_capture_coordinates():
        """Zoom and copy the clicked coordinate tuple to the clipboard"""
        pass

    def mouse_log_clicks():
        """Cause coordinates to be logged a small stack"""
        pass

    def mouse_zoom_auto_single_click(count: int = 1):
        """Click the mouse, prime count clicks, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, count, auto=True)

    def mouse_zoom_auto_single_click():
        """Click the mouse, prime one click, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 1, auto=True)

    def mouse_zoom_auto_double_click():
        """Click the mouse, prime two clicks, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 2, auto=True)

    def mouse_zoom_auto_triple_click():
        """Click the mouse, prime three clicks, and zoom if necessary."""
        eye_zoom_mouse.zoom_mouse.on_pop(0, 3, auto=True)

    def mouse_zoom_auto_move_cursor():
        """Move the cursor but don't actually click, an zoom if necessary"""
        if not config.control_mouse:
            eye_zoom_mouse.zoom_mouse.on_pop(0, 1, auto=True, click=False)

    def mouse_zoom_auto_capture_coordinates():
        """Zoom and copy the auto click coordinate tuple to the clipboard"""
        pass

    def mouse_toggle_zoom_auto_click():
        """Enable auto click"""
        eye_zoom_mouse.zoom_mouse.auto_click_timeout = (
            setting_mouse_zoom_auto_click_timeout.get()
        )
        eye_zoom_mouse.zoom_mouse.toggle_auto_click()
        s = "Auto-click zoom mouse: "
        if eye_zoom_mouse.zoom_mouse.auto_click_enabled:
            s += "ENABLED"
        else:
            s += "DISABLED"
        app.notify(subtitle=s)

    def mouse_trigger_zoom_mouse():
        """Trigger zoom mouse if enabled"""
        if eye_zoom_mouse.zoom_mouse.enabled:
            eye_zoom_mouse.zoom_mouse.on_pop(eye_zoom_mouse.zoom_mouse.state)

    def mouse_drag(button: int):
        """Press and hold/release a specific mouse button for dragging"""
        # Clear any existing drags
        self.mouse_drag_end()

        # Start drag
        ctrl.mouse_click(button=button, down=True)

    def mouse_drag_end():
        """Releases any held mouse buttons"""
        buttons_held_down = list(ctrl.mouse_buttons_down())
        for button in buttons_held_down:
            ctrl.mouse_click(button=button, up=True)

        if (
            eye_zoom_mouse.zoom_mouse.enabled
            and eye_zoom_mouse.zoom_mouse.state != eye_zoom_mouse.STATE_IDLE
        ):
            eye_zoom_mouse.zoom_mouse.cancel()

    def mouse_zoom_drag():
        """zoom end press in hold/release button 0 depending on state"""

        eye_zoom_mouse.zoom_mouse.on_pop(0, 1, auto=False, click=False, drag=True)

    def mouse_sleep():
        """Disables control mouse, zoom mouse, and re-enables cursor"""
        eye_zoom_mouse.toggle_zoom_mouse(False)
        toggle_control(False)
        show_cursor_helper(True)
        stop_scroll()

        # todo: fixme temporary fix for drag command
        button_down = len(list(ctrl.mouse_buttons_down())) > 0
        if button_down:
            ctrl.mouse_click(button=0, up=True)

    def mouse_scroll_down(amount: float = 1):
        """Scrolls down"""
        mouse_scroll(amount * setting_mouse_wheel_down_amount.get())()

    def mouse_scroll_down_continuous():
        """Scrolls down continuously"""
        global continuous_scroll_mode
        continuous_scroll_mode = "scroll down continuous"
        mouse_scroll(setting_mouse_continuous_scroll_amount.get())()

        if scroll_job is None:
            start_scroll()

        if setting_mouse_hide_mouse_gui.get() == 0:
            gui_wheel.show()

    def mouse_scroll_up(amount: float = 1):
        """Scrolls up"""
        mouse_scroll(-amount * setting_mouse_wheel_down_amount.get())()

    def mouse_scroll_up_continuous():
        """Scrolls up continuously"""
        global continuous_scroll_mode
        continuous_scroll_mode = "scroll up continuous"
        mouse_scroll(-setting_mouse_continuous_scroll_amount.get())()

        if scroll_job is None:
            start_scroll()
        if setting_mouse_hide_mouse_gui.get() == 0:
            gui_wheel.show()

    def mouse_scroll_left(amount: float = 1):
        """Scrolls left"""
        actions.mouse_scroll(0, -amount * setting_mouse_wheel_horizontal_amount.get())

    def mouse_scroll_right(amount: float = 1):
        """Scrolls right"""
        actions.mouse_scroll(0, amount * setting_mouse_wheel_horizontal_amount.get())

    def mouse_scroll_stop():
        """Stops scrolling"""
        stop_scroll()

    def mouse_gaze_scroll():
        """Starts gaze scroll"""
        global continuous_scroll_mode
        continuous_scroll_mode = "gaze scroll"

        if gaze_job or scroll_job:
            stop_scroll()
            return

        start_cursor_scrolling()
        if setting_mouse_hide_mouse_gui.get() == 0:
            gui_wheel.show()

        # enable 'control mouse' if eye tracker is present and not enabled already
        global control_mouse_forced
        if eye_mouse.tracker is not None and not config.control_mouse:
            toggle_control(True)
            control_mouse_forced = True

    def copy_mouse_position():
        """Copy the current mouse position coordinates"""
        position = ctrl.mouse_pos()
        clip.set_text((repr(position)))

    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))

    def mouse():
        """An abstracted generic mouse click for using with pop

        States:
         - If in a gaze or scroll job, cancel it
         - If zoom is disabled, we allow pop to click even if there is no tracker.
         - If zoom is enabled and tracker is connected, zoom click
        """
        if setting_mouse_enable_pop_stops_scroll.get() >= 1 and (
            gaze_job or scroll_job
        ):
            stop_scroll()
        elif (
            not eye_zoom_mouse.zoom_mouse.enabled
            and eye_mouse.mouse.attached_tracker is not None
        ):
            if setting_mouse_enable_pop_click.get() >= 1:
                ctrl.mouse_click(button=0, hold=16000)
        else:
            eye_zoom_mouse.zoom_mouse.on_pop(True)


def show_cursor_helper(show):
    """Show/hide the cursor"""
    if app.platform == "windows":
        import ctypes
        import winreg

        import win32con

        try:
            Registrykey = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_WRITE
            )

            for value_name, value in default_cursor.items():
                if show:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, value
                    )
                else:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, hidden_cursor
                    )

            winreg.CloseKey(Registrykey)

            ctypes.windll.user32.SystemParametersInfoA(
                win32con.SPI_SETCURSORS, 0, None, 0
            )

        except WindowsError:
            print("Unable to show_cursor({})".format(str(show)))
    else:
        ctrl.cursor_visible(show)


if setting_mouse_enable_on_startup.get() >= 1:
    app.register("ready", mouse_wake)


def on_pop(active):
    if setting_mouse_enable_pop_stops_scroll.get() >= 1 and (gaze_job or scroll_job):
        stop_scroll()
    elif (
        not eye_zoom_mouse.zoom_mouse.enabled
        and eye_mouse.mouse.attached_tracker is not None
    ):
        print("Triggering non-zoom click")
        if setting_mouse_enable_pop_click.get() >= 1:
            ctrl.mouse_click(button=0, hold=16000)


def mouse_scroll(amount):
    def scroll():
        global scroll_amount
        if continuous_scroll_mode:
            if (scroll_amount >= 0) == (amount >= 0):
                scroll_amount += amount
            else:
                scroll_amount = amount
        actions.mouse_scroll(y=int(amount))

    return scroll


def scroll_continuous_helper():
    global scroll_amount
    # print("scroll_continuous_helper")
    if scroll_amount and (
        eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE
    ):  # or eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_SLEEP):
        actions.mouse_scroll(by_lines=False, y=int(scroll_amount / 10))


def start_scroll():
    global scroll_job
    scroll_job = cron.interval("60ms", scroll_continuous_helper)
    # if eye_zoom_mouse.zoom_mouse.enabled and eye_mouse.mouse.attached_tracker is not None:
    #    eye_zoom_mouse.zoom_mouse.sleep(True)


def gaze_scroll():
    # print("gaze_scroll")
    if (
        eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_IDLE
    ):  # or eye_zoom_mouse.zoom_mouse.state == eye_zoom_mouse.STATE_SLEEP:
        x, y = ctrl.mouse_pos()

        # the rect for the window containing the mouse
        rect = None

        # on windows, check the active_window first since ui.windows() is not z-ordered
        if app.platform == "windows" and ui.active_window().rect.contains(x, y):
            rect = ui.active_window().rect
        else:
            windows = ui.windows()
            for w in windows:
                if w.rect.contains(x, y):
                    rect = w.rect
                    break

        if rect is None:
            # print("no window found!")
            return

        midpoint = rect.y + rect.height / 2
        amount = int(((y - midpoint) / (rect.height / 10)) ** 3)
        actions.mouse_scroll(by_lines=False, y=amount)

    # print(f"gaze_scroll: {midpoint} {rect.height} {amount}")


def stop_scroll():
    global scroll_amount, scroll_job, gaze_job, continuous_scroll_mode
    scroll_amount = 0
    if scroll_job:
        cron.cancel(scroll_job)

    if gaze_job:
        cron.cancel(gaze_job)

    global control_mouse_forced
    if control_mouse_forced and config.control_mouse:
        toggle_control(False)
        control_mouse_forced = False

    scroll_job = None
    gaze_job = None
    gui_wheel.hide()

    continuous_scroll_mode = ""

    # if eye_zoom_mouse.zoom_mouse.enabled and eye_mouse.mouse.attached_tracker is not None:
    #    eye_zoom_mouse.zoom_mouse.sleep(False)


def start_cursor_scrolling():
    global scroll_job, gaze_job
    stop_scroll()
    gaze_job = cron.interval("60ms", gaze_scroll)
    # if eye_zoom_mouse.zoom_mouse.enabled and eye_mouse.mouse.attached_tracker is not None:
    #    eye_zoom_mouse.zoom_mouse.sleep(True)


if app.platform == "mac":
    from talon import tap

    def on_move(e):
        if not config.control_mouse:
            buttons = ctrl.mouse_buttons_down()
            # print(str(ctrl.mouse_buttons_down()))
            if not e.flags & tap.DRAG and buttons:
                e.flags |= tap.DRAG
                # buttons is a set now
                e.button = list(buttons)[0]
                e.modify()

    tap.register(tap.MMOVE | tap.HOOK, on_move)
