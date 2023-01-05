# from user.knausj_talon.code.snippet_watcher import snippet_watcher

from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.vimscript
"""

# short name -> UltiSnip clip name
ctx.lists["user.snippets"] = {
    "global variable": "gvar",
    "script guard": "guard",
    "function": "f",
    # custom
    "auto group": "aug",
}
