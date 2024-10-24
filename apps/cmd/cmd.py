from talon import Context, Module, actions

mod = Module()
mod.apps.cmd = r"""
win.title: /TERM:C:\\windows\\system32\\cmd.exe/
"""
mod.tag(
    "windows_cli",
    desc="Tag for enabling windows command line when not running windows os (ie: wine)",
)

ctx = Context()
ctx.matches = r"""
app: cmd
"""
