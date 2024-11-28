from talon import Context, Module

mod = Module()
mod.apps.nix_repl = """
win.title: /nix repl/
"""

ctx = Context()
ctx.matches = r"""
app: nix_repl
not tag: user.code_language_forced
"""


@ctx.action_class("code")
class CodeActions:
    def language():
        return "nix"
