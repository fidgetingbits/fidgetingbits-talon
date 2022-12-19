import os
import os.path
import requests
import time
from pathlib import Path
from talon import ctrl, ui, Module, Context, actions, clip
import tempfile

mod = Module()

mod.tag(
    "line_commands",
    desc="Tag for enabling generic line navigation and selection commands",
)


@mod.action_class
class Actions:
    def extend_until_line(line: int):
        """Extends the selection from current line to the specified line"""

    def select_range(line_start: int, line_end: int):
        """Selects lines from line_start to line line_end"""
        actions.edit.jump_line(line_start)
        actions.edit.extend_line_end()

        number_of_lines = line_end - line_start
        for i in range(0, number_of_lines):
            actions.edit.extend_line_down()
        actions.edit.extend_line_end()

    def extend_camel_left():
        """Extends the selection by camel/subword to the left"""

    def extend_camel_right():
        """Extends the selection by camel/subword to the right"""

    def camel_left():
        """Moves cursor to the left by camel case/subword"""

    def camel_right():
        """Move cursor to the right by camel case/subword"""

    def line_clone(line: int):
        """Clones specified line at current position"""

    def line_find_forward(key: str):
        """Finds the next character in the line"""

    def line_find_backward(key: str):
        """Finds the previous character in the line"""

    def delete_word_right():
        """Delete word to the right or remainder of current word"""

    def delete_word_left():
        """Delete word to the left or remainder of current word"""

    def delete_line_beginning():
        """Delete from the cursor until the start of the line"""

    def delete_line_remaining():
        """Delete from the cursor until the end of the line"""
