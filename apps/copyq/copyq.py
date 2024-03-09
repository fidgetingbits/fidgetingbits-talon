from talon import Module, Context, actions, clip, app, cron, settings
from typing import Optional
import subprocess


mod = Module()
ctx = Context()

ctx.matches = """
user.running: copyq
"""


class CopyQ:

    def run(self, args):
        """Run copyq with the specified arguments and return output"""
        try:
            subprocess.Popen(["copyq"] + args.split())
        except Exception:
            print("copyq.py error: unable to run copyq")

    def toggle(self):
        self.run("toggle")

    def hide(self):
        self.run("hide")

    def show(self):
        self.run("show")


copyq = CopyQ()


@ctx.action_class("user")
class UserActions:
    def clipboard_manager_toggle():
        copyq.toggle()

    def clipboard_manager_hide():
        copyq.hide()

    def clipboard_manager_show():
        copyq.show()
