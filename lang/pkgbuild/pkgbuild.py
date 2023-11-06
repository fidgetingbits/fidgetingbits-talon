from talon import Context

ctx = Context()
ctx.matches = r"""
code.language: pkgbuild
"""

ctx.lists["user.pkgbuild_variables"] = {}
