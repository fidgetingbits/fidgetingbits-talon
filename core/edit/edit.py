from talon import Context, Module, actions, clip

ctx = Context()
mod = Module()

END_OF_WORD_SYMBOLS = ".!?;:—_/\\|@#$%^&*()[]{}<>=+-~`"


@ctx.action_class("edit")
class EditActions:
    # actions that should be set no matter what context we are in
    # for generic os-specific see apps/linux/edit.talon
    # for more application-specific see apps/linux/shell_edit_emacs.talon,
    # apps/linux/vim/editing.talon, etc

    def delete():
        actions.key("backspace")

    def down():
        actions.key("down")

    def up():
        actions.key("up")

    def left():
        actions.key("left")

    def right():
        actions.key("right")

    def select_none():
        actions.key("right")

    def selected_text() -> str:
        with clip.capture() as s:
            actions.edit.copy()
        try:
            return s.text()
        except clip.NoChange:
            return ""

    def line_insert_down():
        actions.edit.line_end()
        actions.key("enter")

    def selection_clone():
        actions.edit.copy()
        actions.edit.select_none()
        actions.edit.paste()

    def line_clone():
        # This may not work if editor auto-indents. Is there a better way?
        actions.edit.line_start()
        actions.edit.extend_line_end()
        actions.edit.copy()
        actions.edit.right()
        actions.key("enter")
        actions.edit.paste()

    # # This simpler implementation of select_word mostly works, but in some apps it doesn't.
    # # See https://github.com/talonhub/community/issues/1084.
    # def select_word():
    #     actions.edit.right()
    #     actions.edit.word_left()
    #     actions.edit.extend_word_right()

    def select_word():
        actions.edit.extend_right()
        character_to_right_of_initial_caret_position = actions.edit.selected_text()

        # Occasionally apps won't let you edit.extend_right()
        # and therefore won't select text if your caret is on the rightmost character
        # such as in the Chrome URL bar
        did_select_text = character_to_right_of_initial_caret_position != ""

        if did_select_text:
            # .strip() turns newline & space characters into empty string; the empty
            # string is in any other string, so this works.
            if (
                character_to_right_of_initial_caret_position.strip()
                in END_OF_WORD_SYMBOLS
            ):
                # Come out of the highlight in the initial position.
                actions.edit.left()
            else:
                # Come out of the highlight one character
                # to the right of the initial position.
                actions.edit.right()

        actions.edit.word_left()
        actions.edit.extend_word_right()


@mod.action_class
class Actions:
    def paste(text: str):
        """Pastes text and preserves clipboard"""

        with clip.revert():
            clip.set_text(text)
            # Some apps don't like ctrl-shift-v, so we use ctrl-v instead, which is okay, because
            # we are just pasting text here anyway
            actions.edit.paste_match_style()
            # sleep here so that clip.revert doesn't revert the clipboard too soon
            actions.sleep("150ms")

    def delete_right():
        """Delete character to the right"""
        actions.key("delete")

    def word_short_left():
        """Moves left by one special-char-delimited word."""
        actions.edit.word_left()

    def word_short_right():
        """Moves right by one special-char-delimited word."""
        actions.edit.word_right()

    def word_long_left():
        """Moves left by a space-delimited word."""

    def word_long_right():
        """Moves right by a space-delimited word."""

    def words_left(n: int):
        """Alias for words_short_left"""
        actions.user.words_short_left(n)

    def words_right(n: int):
        """Alias for words_short_right"""
        actions.user.words_short_right(n)

    def words_short_left(n: int):
        """Moves left by n special-char-delimited words."""
        for _ in range(n):
            actions.user.word_short_left()

    def words_short_right(n: int):
        """Moves right by n special-char-delimited words."""
        for _ in range(n):
            actions.user.word_short_right()

    # FIXME: The should all use the new short/long versions
    def cut_word():
        """Cut word under cursor"""
        actions.edit.select_word()
        actions.edit.cut()

    def cut_word_left():
        """Cuts the word to the left."""
        actions.edit.extend_word_left()
        actions.edit.cut()

    def cut_word_right():
        """Cuts the word to the right."""
        actions.edit.extend_word_right()
        actions.edit.cut()

    def copy_word():
        """Copy word under cursor"""
        actions.edit.select_word()
        actions.edit.copy()

    def copy_word_left():
        """Copies the word to the left."""
        actions.edit.extend_word_left()
        actions.edit.copy()

    def copy_word_right():
        """Copies the word to the right."""
        actions.edit.extend_word_right()
        actions.edit.copy()

    def paste_word():
        """Paste to word under cursor"""
        actions.edit.select_word()
        actions.edit.paste()

    def cut_all():
        """Cut all text in the current document"""
        actions.edit.select_all()
        actions.edit.cut()

    def copy_all():
        """Copy all text in the current document"""
        actions.edit.select_all()
        actions.edit.copy()

    def paste_without_new_lines():
        """Paste to the current entry without new lines

        This is mostly centered around copy and paste in the terminal, which will insert a new line if what you copy
        crosses two lines. For example, given a line like:

        ```
        -lm -lgcc -lmingwex -lmingw32 -lkernel32 -luser32 -lshell32 -llibwindows -L native=/nix/store/hmypgg46gh6mi918hml3l7nmmpw80zr2-v
        endor-cargo-deps/c19b7c6f923b580ac259164a89f2577984ad5ab09ee9d583b888f934adbbe8d0/windows_x86_64_gnu-0.52.6/lib` (exit status: 1)
        ```

        If selecting the /nix/store/ path and pasting it, it will insert a new line. This command will remove it

        """
        entry = clip.get().strip()
        for line in entry.split("\n"):
            actions.insert(line)

    def paste_all():
        """Paste to the current document"""
        actions.edit.select_all()
        actions.edit.paste()

    def delete_all():
        """Delete all text in the current document"""
        actions.edit.select_all()
        actions.edit.delete()

    def cut_line():
        """Cut current line"""
        actions.edit.select_line()
        actions.edit.cut()

    def copy_line():
        """Copy current line"""
        actions.edit.select_line()
        actions.edit.copy()

    def paste_line():
        """Paste to current line"""
        actions.edit.select_line()
        actions.edit.paste()

    # ----- Start / End of line -----
    def select_line_start():
        """Select to start of current line"""
        if actions.edit.selected_text():
            actions.edit.left()
        actions.edit.extend_line_start()

    def select_line_end():
        """Select to end of current line"""
        if actions.edit.selected_text():
            actions.edit.right()
        actions.edit.extend_line_end()

    def cut_line_start():
        """Cut to start of current line"""
        actions.user.select_line_start()
        actions.edit.cut()

    def cut_line_end():
        """Cut to end of current line"""
        actions.user.select_line_end()
        actions.edit.cut()

    def copy_line_start():
        """Copy to start of current line"""
        actions.user.select_line_start()
        actions.edit.copy()

    def copy_line_end():
        """Copy to end of current line"""
        actions.user.select_line_end()
        actions.edit.copy()

    def paste_line_start():
        """Paste to start of current line"""
        actions.user.select_line_start()
        actions.edit.paste()

    def paste_line_end():
        """Paste to end of current line"""
        actions.user.select_line_end()
        actions.edit.paste()

    def delete_line_start():
        """Delete to start of current line"""
        actions.user.select_line_start()
        actions.edit.delete()

    def delete_line_end():
        """Delete to end of current line"""
        actions.user.select_line_end()
        actions.edit.delete()

    def delete_word_right():
        """Alias for delete_word_short_right"""
        actions.user.delete_word_short_right()

    def delete_word_left():
        """Alias for delete_word_short_left"""
        actions.user.delete_word_short_left()

    def delete_word_short_right():
        """Delete to end of special-char-delimited current word"""
        actions.edit.extend_word_right()
        actions.edit.delete()

    def delete_word_short_left():
        """Delete to start of special-char-delimited current word"""
        actions.edit.extend_word_left()
        actions.edit.delete()

    def delete_word_long_right():
        """Delete to end of space-delimited current word"""
        actions.edit.extend_word_right()
        actions.edit.delete()

    def delete_word_long_left():
        """Delete to start of space-delimited current word"""
        actions.edit.extend_word_left()
        actions.edit.delete()

    def line_middle():
        """Go to the middle of the line"""
        actions.edit.select_line()
        half_line_length = int(len(actions.edit.selected_text()) / 2)
        actions.edit.left()
        for i in range(0, half_line_length):
            actions.edit.right()

    def jump_cursor_to_matching_char():
        """Jump cursor to matching character

        For example, jump from an opening bracket to its closing bracket.
        """
