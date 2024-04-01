from talon import Module, actions

mod = Module()


@mod.action_class
class tab_actions:
    def tab_jump(number: int):
        """Jumps to the specified tab"""

    def tab_jump_name(name: str):
        """Jumps to the specified tab"""

    def tab_final():
        """Jumps to the final tab"""

    def tab_first():
        """Jumps to the first tab"""

    def tab_search():
        """Search through tabs"""

    def tab_close_wrapper():
        """Closes the current tab.
        Exists so that apps can implement their own delay before running tab_close() to handle repetitions better.
        """
        actions.app.tab_close()

    def tab_duplicate():
        """Duplicates the current tab."""

    def tab_pin():
        """Pin the current tab"""

    def tab_unpin():
        """Unpin the current tab"""

    def tabs_show():
        """Show all tabs"""

    def tab_last():
        """Go to the most recently focused tab"""

    def tab_rename(name: str):
        """Rename the current tab"""

    def tab_name_format():
        """Formatters for tab names in given app"""
        return "ALL_CAPS,DASH_SEPARATED"
