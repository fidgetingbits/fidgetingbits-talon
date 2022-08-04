import collections
from os import system
from sys import platform
from time import sleep, time

from talon import Module, actions, app, ctrl, settings, ui
from talon.types import Point2d
from talon_plugins.eye_mouse import menu, tracker

mod = Module()


class EyeMouseSleepTracker(object):

    """Track whether or not eyes are present. Wake and sleep the screen
    accordingly"""

    enabled = False

    def __init__(self):
        """Set up sleep states"""
        self.nosignal = 0  # Number of ticks there have been no signal
        self.sleeping = False
        self.main_screen = ui.main_screen()
        self.size_px = Point2d(self.main_screen.width, self.main_screen.height)
        self.settings = {
            "max_eyeless_ticks": settings.get(
                "user.mouse_sleep_tracker_timeout_frames"
            ),
            "sleep_mode": settings.get("user.mouse_sleep_tracker_sleep_mode"),
            "suspend_screen": settings.get("user.mouse_sleep_tracker_suspend_screen"),
        }

    def suspend_screen(self):
        """Place the monitor into energy saving mode"""
        if platform == "darwin":
            cmd = "pmset displaysleepnow"
        elif platform == "linux":
            app.notify(subtitle="would sleep screen")
            # cmd = "xset dpms force standby"
            cmd = ""
        else:
            return

        print("sleeping in two seconds")
        sleep(2)
        system(cmd)

    def wake_screen(self):
        """Force fully wake the screen upsteep"""
        if platform == "linux":
            cmd = "xset dpms force on"
        print("waking up screen")
        # system(cmd)

    def wake(self):
        self.sleeping = False
        app.notify(subtitle="waking from eye sleep state")
        if self.settings["sleep_mode"]:
            actions.speech.enable()
        if self.settings["suspend_screen"]:
            self.wake_screen()

    def suspend(self):
        self.sleeping = True
        app.notify(subtitle="entering eye sleep state")
        if self.settings["sleep_mode"]:
            actions.speech.disable()
        if self.settings["suspend_screen"]:
            self.suspend_screen()

    def on_gaze(self, frame):
        pos = frame.gaze
        pos *= self.size_px
        max_ticks = self.settings["max_eyeless_ticks"]
        if not (pos.x <= 0 and pos.y <= 0):
            self.nosignal = 0
            if self.sleeping:
                self.wake()
        else:
            if self.sleeping:
                if self.nosignal < max_ticks:
                    self.wake()
            else:
                if self.nosignal == max_ticks:
                    self.suspend()
            self.nosignal = min(max_ticks, self.nosignal + 1)


# Tobii 4C verson, @Dan on slack for help!
# Change self.magic = 4 for Tobii 5 it ahould work, unless scroll is breaks that.
class EyeMouseBlink:
    enabled = False

    def __init__(self):
        # tweakable variables
        self.beep = False  # requires windows
        self.two_blinks = (
            True  # depricated - one blink means you will have lots of misclicks
        )
        self.magic = 24  # works on 4c might not be optimized # CHANGME if not clicking accuratley (won't work on 4C speed probably like =35)
        self.scroll_sensitivity = 1  # I like it kinda fast. 6-7 slower.

        # state tracking
        self.second = False
        self.blinking = False
        self.nosignal = 0
        self.sleep = False
        self.right_px, self.right_py = 0, 0
        self.lcurclosed = 0
        self.rcurclosed = 0
        self.signal = 0
        self.left_px, self.left_py = 0, 0
        self.counter = 0
        self.invalid_left = 0
        self.invalid_right = 0
        self.left_closed_count = 0
        self.right_closed_count = 0
        self.expire = 700  # lower if you blink twice a lot
        self.focus_sensitivity = 48  # can go lower on 4C Tobii 5 recomended = 50
        self.MAXSIZE = 120  # if memory starts to be a problem
        self.eye_history = []
        self.main_screen = ui.main_screen()
        self.size_px = Point2d(self.main_screen.width, self.main_screen.height)
        self.get_time = lambda: int(round(time() * 1000))
        self.current_time = 0
        self.first_blink = 0
        self.eyes = True
        self.last_blink = False
        self.right_history = self.momentum_state()
        self.left_history = self.momentum_state()
        self.right_open = 1
        self.left_open = 1

    def momentum_state(self):
        # Here we story the history of sensor readings from the last time steps.
        # The length of the history defines how snappy vs sluggish the scrolling feels
        # at the same time a longer history will lead to less false positives and false negatives
        buffer = collections.deque(maxlen=30)
        while True:
            data = yield
            buffer.append(data)
            ratio = buffer.count(0) / len(buffer)
            # At least from my experiments sometimes when an eye is closed, the sensor will only
            # yield false intermittently. This means that we want to set an eye as closes as soon as the history
            # containts a certain (low) amount of eye closed signals.
            # I tried out a few values and set it to 0.1 (10% of eye closed sensor readings)
            if ratio >= 0.1:
                yield False
            else:
                yield True

    def hist_add(self, key, value):
        if len(self.eye_history) == self.MAXSIZE:
            min = int(self.MAXSIZE // 2)
            self.eye_history = self.eye_history[self.MAXSIZE // 2 :]
        self.eye_history.append(value)

    def beep_win(self, freq=9000, dur=35):
        try:
            import winsound

            winsound.Beep(freq, dur)
        except Exception as e:
            pass

    def estimate_focus(self, eye_history, magic):
        # rewrite for tobii 4c even though it does work good..
        # ugly ugly ugly temporary
        # poorly set up and only for tobii 5.. todo
        # should I use self.eyehist?
        if magic <= 6:
            lo = magic - 3  # 3
        elif magic <= 5:
            lo = magic - 2  # 3
        elif magic <= 3:
            lo = magic - 2  # 1
        else:
            lo = 1
        hi = lo + magic + 8
        counter = 0
        x_avg = 0
        y_avg = 0
        for i in range(lo, hi + 1):
            x = eye_history[-1 * i][0]
            y = eye_history[-1 * i][1]
            x_avg += x
            y_avg += y
            counter += 1
            # print("History #-"+str(i),x,y)
        x_avg = x_avg / counter
        y_avg = y_avg / counter
        # print("Average = ",x_avg,',',y_avg)
        return x_avg, y_avg

    def eye_scroll_left(self, frame):
        if not self.left_open and self.right_open:
            ctrl.mouse_scroll(-self.scroll_sensitivity)

    def eye_scroll_right(self, frame):
        if self.left_open and not self.right_open:
            ctrl.mouse_scroll(self.scroll_sensitivity)

    def on_gaze(self, frame):
        l, r = frame.left, frame.right
        # print("GGG",frame.gaze)
        # print(l, r)
        pos = frame.gaze
        pos *= self.size_px
        self.current_time = int(self.get_time())
        # randomly flickers 0 and 1 so needs a filter
        # glitchy, also mouse_scroll "down" key is lame cheat, im sure talon has a 'scroll x'
        # print("POS",pos)
        # print(frame.left.gaze.x, frame.right.gaze.x)
        # print("Present: ",frame.left.detected, frame.right.detected)#not reliable
        if not (pos.x <= 0 and pos.y <= 0):

            next(self.right_history)
            self.right_open = self.right_history.send(frame.right.detected)
            next(self.left_history)
            self.left_open = self.left_history.send(frame.left.detected)
            # Eye signal
            self.nosignal = 0
            self.signal += 1
            if self.signal < 3:  # 4:
                return  # print("Open your eyes more between blinks!"); return

            if self.eyes == False:
                if self.two_blinks:
                    if abs(self.current_time - self.first_blink) > self.expire:
                        # Second blink, but expired.
                        print("Click expired:", self.current_time - self.first_blink)
                        self.first_blink = self.current_time
                        self.second = False
                    if not self.second:
                        try:
                            # print("[First Blink] Started")
                            try:
                                self.target_history = self.eye_history[-1 * self.magic]
                            except Exception as e:
                                print(e)
                                self.target_history = self.eye_history[
                                    len(self.eye_history) * -1
                                ]

                            fx, fy = self.estimate_focus(self.eye_history, self.magic)
                            # print("Focus:",fx,fy,self.target_history)
                            self.target_x, self.target_y = (
                                self.target_history[0],
                                self.target_history[1],
                            )
                            # print(abs(fx-self.target_x),abs(fy-self.target_y))

                            if (
                                abs(fx - self.target_x) > self.focus_sensitivity
                                or abs(fy - self.target_y) > self.focus_sensitivity
                            ):
                                print(
                                    "Misclick assumed, not focusing enough or change params."
                                )
                                print(abs(fx - self.target_x), abs(fy - self.target_y))
                                self.first_blink = (
                                    self.current_time - 15000
                                )  # expires cheap method
                                if self.beep:
                                    self.beep_win(3500, 20)
                            else:
                                self.first_blink = self.current_time
                            # if self.beep: self.beep_win(8000,50) #debug
                            self.second = True
                        except Exception as e:
                            print("ERR", e)
                    else:
                        print("Second blink click going through: ", pos)
                        ctrl.mouse_move(self.target_x, self.target_y)
                        if self.beep:
                            self.beep_win()
                        if self.left_closed_count > 5 or self.right_closed_count > 5:
                            pass  # print("Eyes are closed oddly..")
                        else:
                            # print("Allowing it")
                            # ctrl.mouse_click(
                            #    pos=(self.target_x, self.target_y), hold=32000
                            # )
                            # app.notify(subtitle="blink click")
                            pass
                        # ctrl.mouse_click(pos=(self.target_x, self.target_y), hold=32000)
                        self.second = False
            self.eyes = True
            px, py = ctrl.mouse_pos()
            self.hist_add(self.current_time, [px, py])
            # Eye scroll left
            self.eye_scroll_right(frame)
            self.eye_scroll_left(frame)
        else:
            self.signal = 0
            if self.nosignal == 0:
                self.eyes = False
            self.nosignal += 1


blink = EyeMouseBlink()
sleep_tracker = EyeMouseSleepTracker()


@mod.action_class
class Actions:
    def mouse_toggle_blink_click():
        """Turn on an off blink clicking"""
        global blink
        if not blink.enabled:
            tracker.register("gaze", blink.on_gaze)
            blink.enabled = True
        else:
            tracker.unregister("gaze", blink.on_gaze)
            blink.enabled = False
        app.notify(subtitle="blink click: %s" % blink.enabled)

    def mouse_toggle_eye_mouse_sleep_tracker():
        """Turn on an off eye mouse sleep tracker"""
        global sleep_tracker
        if not sleep_tracker.enabled:
            tracker.register("gaze", sleep_tracker.on_gaze)
            sleep_tracker.enabled = True
        else:
            tracker.unregister("gaze", sleep_tracker.on_gaze)
            sleep_tracker.enabled = False
        app.notify(subtitle="eye sleep tracker: %s" % sleep_tracker.enabled)


# menu.toggle('Blink Click + Wink Scroll', weight=2, cb=toggle_blink_click)
