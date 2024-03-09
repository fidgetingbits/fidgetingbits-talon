from talon import Module, Context, actions, clip, app, cron, settings
from typing import Optional

mod = Module()
ctx = Context()

mod.tag("clipboard_manager", desc="Indicates a clipboard manager is running")


@mod.action_class
class Actions:
    def clipboard_manager_toggle():
        """Toggle clipboard manager"""

    def clipboard_manager_hide():
        """Hide clipboard manager"""

    def clipboard_manager_remove(numbers: list[int] = None):
        """Remove clipboard manager history"""

    def clipboard_manager_split(numbers: list[int]):
        """Split clipboard content on new line to add new items to clipboard manager history"""

    def clipboard_manager_copy(numbers: list[int]):
        """Copy from clipboard manager"""

    def clipboard_manager_paste(numbers: list[int], match_style: bool = False):
        """Paste from clipboard manager"""
        actions.user.clipboard_manager_copy(numbers)
        if match_style:
            actions.edit.paste_match_style()
        else:
            actions.edit.paste()
