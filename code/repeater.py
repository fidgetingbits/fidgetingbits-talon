import time

from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def repeat_insert(text: str, count: int):
        """Repeat and insert count number of times"""
        for i in range(1, count):
            actions.insert(text)
            time.sleep(0.15)
