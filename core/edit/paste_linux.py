# Note: This isn't inside of edit_linux.py because of some terminal quirks, but this one does apply to everything
import subprocess

from talon import Context, actions, clip

ctx = Context()
ctx.matches = r"""
os: linux
"""


@ctx.action_class("user")
class UserActions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

        # with clip.revert():
        #     clip.set_text(text)
        #     actions.edit.paste()
        #     # sleep here so that clip.revert doesn't revert the clipboard too soon
        #     actions.sleep("100ms")

        old = subprocess.check_output(["xsel", "-o", "-b"])
        clip.set_text(text)
        actions.edit.paste()
        actions.sleep("200ms")
        clip.set_text(old.decode("utf-8"))
