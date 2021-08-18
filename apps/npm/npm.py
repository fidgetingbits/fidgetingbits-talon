from talon import Context, Module, actions, app, imgui, registry, settings

ctx = Context()
mod = Module()
mod.tag("npm", desc="Tag for enabling npm nodejs package manager in terminal")

ctx.matches = r"""
tag: terminal
and tag: user.npm
"""

