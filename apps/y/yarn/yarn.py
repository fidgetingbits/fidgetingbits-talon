from talon import Context, Module

ctx = Context()
mod = Module()
mod.tag("yarn", desc="Tag for enabling yarn nodejs package manager in terminal")

ctx.matches = r"""
tag: terminal
and tag: user.yarn
"""
