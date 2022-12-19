from talon import Context, Module

ctx = Context()
mod = Module()
mod.tag("python_repl", desc="Tag for indicating a generic python repl")
mod.tag("talon_repl", desc="Tag for indicating the talon repl")

ctx.matches = r"""
mode: command
tag: user.python_repl

mode: command
tag: user.talon_repl
"""
