from talon import Module, actions, app
import time

mod = Module()
setting = mod.setting("sleep_word", type=str)
time_last_pop = 0


@mod.action_class
class Actions:

    # XXX - should go through and disable all of the currently activated modes,
    # and then wake up should reactivate all of them
    def talon_sleep():
        """Put Talon to sleep"""
        # XXX - why doesn't this show?
        actions.user.notify("Talon sleeping")
        actions.speech.disable()
        actions.user.mouse_sleep()
        #actions.user.talon_sleep_callback()

    def talon_wake():
        """Wake Talon from sleep"""
        actions.speech.enable()
        actions.user.mouse_wake()
        #actions.user.talon_wake_callback()
        actions.user.notify("Talon awake")

    def talon_wake_on_pop():
        """Use pop sound to wake from sleep"""
        global time_last_pop
        delta = time.time() - time_last_pop
        if delta >= 0.1 and delta <= 0.3:
            actions.user.talon_wake()
        time_last_pop = time.time()

    def talon_sleep_status():
        """Notify about Talon sleep status"""
        if actions.speech.enabled():
            actions.user.notify("Talon is: awake")
        else:
            actions.user.notify("Talon is: sleeping")

    def talon_sleep_update_phrase(words: list[str]) -> tuple[bool, str]:
        """Update spoke in words in case of sleep command"""
        sleep_word = setting.get()
        if sleep_word in words:
            index = words.index(sleep_word)
            text = " ".join(words[: index + 1])
            if index < len(words) - 1:
                text += " ..."
            return True, text
        return False, " ".join(words)