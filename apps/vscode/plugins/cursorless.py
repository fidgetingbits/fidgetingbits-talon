# From https://github.com/AndreasArvidsson/andreas-talon/blob/master/apps/vscode/cursorless.py
from typing import Any

from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def c_browser_open_target(target: Any):
        """Search for target text in browser"""
        texts = actions.user.c_get_texts(target)
        text = " + ".join(texts)
        actions.user.browser_open(text)

    def c_get_texts(target: Any) -> list[str]:
        """Get text for Cursorless target"""
        return actions.user.private_cursorless_command_get(
            {
                "name": "getText",
                "target": target,
            }
        )

    def c_get_target_length(target: str) -> int:
        """Return the length of a cursorless target"""
        texts = actions.user.c_get_texts(target)
        return len(texts[0])

    def c_wrap_with_symbol(target: Any, symbol: str):
        """Wrap the target with <symbol>"""
        if symbol == "space":
            symbol = " "

        actions.user.private_cursorless_command_and_wait(
            {
                "name": "wrapWithPairedDelimiter",
                "left": symbol,
                "right": symbol,
                "target": target,
            }
        )

    def c_wrap_with_snippet(target: Any, id: str):
        """Wrap the target with snippet <id>"""
        index = id.rindex(".")
        snippet_id = id[:index]
        var_name = id[index + 1]
        snippet = actions.user.get_snippet(snippet_id)
        variable = next(v for v in snippet.variables if v.name == var_name)
        body = snippet.body.replace(f"${var_name}", "$TM_SELECTED_TEXT")
        actions.user.cursorless_wrap_with_snippet(
            body, target, None, variable.wrapperScope
        )
