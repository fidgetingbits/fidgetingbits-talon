from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.pkgbuild
"""

ctx.lists["user.pkgbuild_variables"] = {}
