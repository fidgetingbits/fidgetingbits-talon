import time
import shlex
import subprocess

from talon import Context, Module, actions, app, clip

mod = Module()
ctx = Context()
ctx_open = Context()

ctx.matches = """
os: linux
and user.running: copyq

os:mac
"""

ctx_open.matches = """
app: copyq
"""


class CopyQ:
    """Helper class for executing copyq commands"""

    def __init__(self):
        if app.platform == "mac":
            # FIXME: this should just be part of PATH, but just in case
            # also once nix-darwin supports copyq, this will be wrong
            self.bin = "/opt/homebrew/bin/copyq"
        else:
            self.bin = "copyq"

    def _run(self, args):
        """Run copyq with the specified arguments"""
        try:
            subprocess.Popen([self.bin] + args.split())
        except Exception:
            print("copyq.py error: unable to run copyq")

    def _read_output(self, args):
        """Run copyq with the specified arguments"""
        try:
            return subprocess.check_output([self.bin] + args.split())
        except Exception:
            print("copyq.py error: unable to run copyq")

    def toggle(self):
        self._run("toggle")

    def hide(self):
        self._run("hide")

    def show(self):
        self._run("show")

    def validate(self, indexes: list[int]):
        count = self.count()
        for i in indexes:
            if i > count or i == 0:
                self.error(f"ERROR: {i} is not a valid index")

    def read(self, row: int):
        return self._read_output(f"read {row}")

    def add(self, content: str, row: int = 0):
        return self._run(f"add {content}")

    def insert(self, content: str, row: int = 0):
        if not isinstance(content, str):
            content = str(content)
        return self._run(f"insert {row} {content}")

    def write(self, content: str, row: int = 0):
        if not isinstance(content, str):
            content = str(content)
        return self._run(f"write {row} {content}")

    def count(self):
        return int(self._read_output("count").decode("utf-8"))

    def paste(self, index: int = 0):
        self._run("paste")

    def remove(self, row: int = 0):
        self._read_output(f"remove {row}")

    def enable(self):
        self._run("enable")

    def disable(self):
        self._run("disable")

    def pin(self, rows: str):
        self._run(f"plugins.itempinned.pin {rows}")

    def unpin(self, rows: str):
        self._run(f"plugins.itempinned.unpin {rows}")

    def separator(self, sep="\n"):
        self.run(f"separator {shlex.quote(sep)}")

    def error(msg: str):
        error_msg = f"CopyQ - {msg}"
        actions.user.notify(error_msg)
        raise ValueError(error_msg)


copyq = CopyQ()


@ctx.action_class("user")
class UserActions:
    def clipboard_manager_toggle():
        copyq.toggle()

    def clipboard_manager_hide():
        copyq.hide()

    def clipboard_manager_show():
        copyq.show()

    def clipboard_manager_enable():
        copyq.enable()

    def clipboard_manager_disable():
        copyq.disable()

    def clipboard_manager_remove(numbers: list[int]):
        if not numbers:
            # remove first item
            copyq.remove()
        else:
            copyq.validate(numbers)
            for n in reversed(sorted(numbers)):
                copyq.remove(n - 1)

    def clipboard_manager_remove_range(start: int, end: int):
        copyq.validate([start, end])
        for i in range(end, start - 1, -1):
            copyq.remove(i - 1)

    def clipboard_manager_remove_all():
        for i in reversed(range(0, copyq.count())):
            copyq.remove(i)

    def clipboard_manager_get(numbers: list[int]):
        copyq.validate(numbers)
        items = []
        # FIXME: for image pasting, we want to special handle utf-8
        for n in numbers:
            items.append(copyq.read(n - 1).decode("utf-8"))
        return items

    def clipboard_manager_copy(numbers: list[int]):
        items = actions.user.clipboard_manager_get(numbers)
        clip.set_text("\n".join(items))

    # FIXME: Should this delete the originals?
    # FIXME: This should allow splitting on an arbitrary separator
    def clipboard_manager_split(numbers: list[int]):
        copyq.validate(numbers)
        new_items = []
        for i in reversed(numbers):
            split_entry = reversed(copyq.read(i - 1).decode("utf-8").split("\n"))
            for item in split_entry:
                new_items.append(item)
        for item in new_items:
            copyq.insert(item)

    def clipboard_manager_paste(numbers: list[int], match_style: bool = False):
        actions.user.clipboard_manager_copy(numbers)
        actions.edit.paste()
        # Remove the new entry created by clipboard_manager_copy() ?
        # FIXME: Not sure I want to keep this yet
        copyq.remove()

    def clipboard_manager_clear_all():
        items = copyq.count()
        for i in range(0, items):
            copyq.remove()

    def clipboard_manager_launch():
        copyq.launch()

    def clipboard_manager_pin(numbers: list[int]):
        copyq.pin(" ".join(map(lambda n: str(n - 1), numbers)))

    def clipboard_manager_unpin(numbers: list[int]):
        copyq.unpin(" ".join(map(lambda n: str(n - 1), numbers)))

    def clipboard_manager_open(numbers: list[int]):
        copyq.open(numbers)

    def clipboard_manager_move(src_row: int, dest_row: int):
        if src_row == dest_row:
            return
        copyq.validate([src_row, dest_row])
        source_row = copyq.read(src_row - 1)
        copyq.remove(src_row - 1)
        copyq.insert(source_row, dest_row - 1)

    def clipboard_manager_swap(src_row: int, dest_row: int):
        if src_row == dest_row:
            return
        copyq.validate([src_row, dest_row])
        # FIXME: Need to check of any of these are pinned
        src_row = src_row - 1
        dest_row = dest_row - 1
        source_contents = copyq.read(src_row).decode("utf-8")
        dest_contents = copyq.read(dest_row).decode("utf-8")
        print(f"source_contents: {source_contents}")
        print(f"dest_contents: {dest_contents}")
        copyq.remove(dest_row)
        if " " in source_contents or "\n" in source_contents:
            source_contents = f'"{source_contents}"'
        if " " in dest_contents or "\n" in dest_contents:
            dest_contents = f'"{dest_contents}"'
        copyq.insert(dest_contents, src_row)
        copyq.remove(src_row)
        copyq.insert(source_contents, dest_row)


# Actions for when CopyQ is focused
@ctx_open.action_class("app")
class app_actions:
    def tab_open():
        actions.key("ctrl-t")

    def tab_close():
        actions.key("ctrl-w")

    def tab_next():
        actions.key("right")

    def tab_previous():
        actions.key("left")


@ctx_open.action_class("user")
class user_actions:
    # FIXME: They should have some formatter probably
    def tab_rename(name):
        actions.key("ctrl-f2")
        actions.insert(name)
