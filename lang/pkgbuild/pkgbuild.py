from talon import Context, Module, actions, app, settings

ctx = Context()
ctx.matches = r"""
tag: user.pkgbuild 
"""

ctx.lists["user.pkgbuild_variables"] = {

}
