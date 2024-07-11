from talon import Context, Module

mod = Module()
mod.tag("bash", desc="Bash shell")

ctx = Context()
ctx.matches = r"""
tag: user.bash
"""

# FIXME(bash): Add automatic readline parsing
# # https://www.gnu.org/software/bash/manual/html_node/Commands-For-Moving.html
