import time
import subprocess
from talon import Context, Module, actions, clip, ui

ctx = Context()
mod = Module()


@ctx.action_class("edit")
class edit_actions:
    def selected_text() -> str:
        with clip.capture() as s:
            actions.edit.copy()
        try:
            return s.get()
        except clip.NoChange:
            return ""


@mod.action_class
class Actions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

#        with clip.revert():
#            clip.set_text(text)
#            actions.edit.paste()
#            # sleep here so that clip.revert doesn't revert the clipboard too soon
#            actions.sleep("100ms")

        old = subprocess.check_output(['xsel', '-o', '-b'])
        clip.set_text(text)
        actions.edit.paste()
        actions.sleep("200ms")
        clip.set_text(old.decode("utf-8"))

    def words_left(n: int):
        """Moves left by n words."""
        for _ in range(n):
            actions.edit.word_left()

    def words_right(n: int):
        """Moves right by n words."""
        for _ in range(n):
            actions.edit.word_right()
