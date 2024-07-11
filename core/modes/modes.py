from typing import Union

from talon import Module, actions
from talon.grammar import Phrase
from talon import Context, Module, actions, app, speech_system

mod = Module()
ctx_sleep = Context()
ctx_awake = Context()

modes = {
    "admin": "enable extra administration commands terminal (docker, etc)",
    "debug": "a way to force debugger commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
}

for key, value in modes.items():
    mod.mode(key, value)

ctx_sleep.matches = r"""
mode: sleep
"""

ctx_awake.matches = r"""
not mode: sleep
"""


@ctx_sleep.action_class("speech")
class ActionsSleepMode:
    def disable():
        actions.app.notify("Talon is already asleep")


@ctx_awake.action_class("speech")
class ActionsAwakeMode:
    def enable():
        actions.app.notify("Talon is already awake")


@mod.action_class
class Actions:
    def talon_sleep_callback():
        """Additional actions to be run when talon goes to sleep"""
        actions.user.system_command_nb(
            "/home/aa/source/obs-cli/obs-cli.py --stop-recording"
        )

    def talon_wake_callback():
        """Additional actions to be run when talon wakes up"""
        actions.user.system_command_nb(
            "/home/aa/source/obs-cli/obs-cli.py --start-recording"
        )

    # From https://github.com/AndreasArvidsson/andreas-talon/blob/master/misc/modes/modes.py

    def command_mode(phrase: Union[Phrase, str] = None):
        """Enter command mode and re-evaluate phrase"""
        ctx.tags = []
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def dictation_mode(phrase: Union[Phrase, str] = None):
        """Enter dictation mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)

    def mixed_mode(phrase: Union[Phrase, str] = None):
        """Enter mixed mode and re-evaluate phrase"""
        actions.user.dictation_format_reset()
        actions.mode.enable("dictation")
        if phrase:
            actions.user.rephrase(phrase, run_async=True)
