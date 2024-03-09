from talon import Module, Context, actions, clip, app, cron, settings
from typing import Optional
import subprocess


mod = Module()
ctx = Context()

ctx.matches = """
user.running: copyq
"""


class CopyQ:
    """Helper class for executing copyq commands"""

    def _run(self, args):
        """Run copyq with the specified arguments"""
        try:
            subprocess.Popen(["copyq"] + args.split())
        except Exception:
            print("copyq.py error: unable to run copyq")

    def _read_output(self, args):
        """Run copyq with the specified arguments"""
        try:
            return subprocess.check_output(["copyq"] + args.split())
        except Exception:
            print("copyq.py error: unable to run copyq")

    def toggle(self):
        self._run("toggle")

    def hide(self):
        self._run("hide")

    def show(self):
        self._run("show")

    def read(self, row: int):
        return self._read_output(f"read {row}")

    def paste(self, index: int = 0):
        self._run("paste")

    def paste_many(self, indexes: list[int] = [0]):
        self._run("paste")

    def remove(self, row: int = 0):
        self._read_output(f"remove {row}")


copyq = CopyQ()


@ctx.action_class("user")
class UserActions:
    def clipboard_manager_toggle():
        copyq.toggle()

    def clipboard_manager_hide():
        copyq.hide()

    def clipboard_manager_show():
        copyq.show()

    def clipboard_manager_remove(numbers: list[int]):
        if 0 in numbers:
            print("ERROR: 0 is not a valid copyq index")
            return
        if not numbers:
            # remove index 0 only
            copyq.remove()
            return
        for n in numbers:
            copyq.remove(n - 1)

    def clipboard_manager_paste(numbers: list[int], match_style: bool = False):
        if 0 in numbers:
            print("ERROR: 0 is not a valid copyq index")
            return
        items = []
        # FIXME: for image pasting, we want to special handle utf-8
        for n in numbers:
            items.append(copyq.read(n - 1).decode("utf-8"))
        print(items)
        clip.set_text("\n".join(items))
        actions.edit.paste()
        copyq.remove()
