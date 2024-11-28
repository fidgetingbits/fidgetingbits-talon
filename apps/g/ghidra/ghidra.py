import time

from talon import Context, Module, actions

mod = Module()
mod.apps.ghidra = """
app.name: Ghidra
app.name: ghidra-Ghidra
"""

ctx = Context()
ctx.matches = r"""
app: ghidra
"""
