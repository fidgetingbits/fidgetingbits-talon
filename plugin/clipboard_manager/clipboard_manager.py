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

    def clipboard_manager_show():
        """Show the clipboard manager"""

    def clipboard_manager_clear_all():
        """Clear all entries from the clipboard manager"""

    def clipboard_manager_launch():
        """Launch the clipboard manager"""

    def clipboard_manager_remove(numbers: list[int] = None):
        """Remove specified row of clipboard manager history"""

    def clipboard_manager_remove_range(start: int, end: int):
        """Remove clipboard manager from start index to end index"""

    def clipboard_manager_split(numbers: list[int]):
        """Split clipboard content on new line to add new items to clipboard manager history"""

    def clipboard_manager_pin(numbers: list[int]):
        """Pin clipboard specified rows"""

    def clipboard_manager_unpin(numbers: list[int]):
        """Unpin clipboard specified rows"""

    def clipboard_manager_copy(numbers: list[int]):
        """Copy from clipboard manager"""

    def clipboard_manager_paste(numbers: list[int], match_style: bool = False):
        """Paste from clipboard manager"""

    def clipboard_manager_enable():
        """Enable the clipboard manager"""

    def clipboard_manager_disable():
        """Disable the clipboard manager"""

    def clipboard_manager_tag():
        """Tag a clipboard entry"""

    def clipboard_manager_open(numbers: list[int]):
        """Open items from clipboard manager (eg: urls)"""
