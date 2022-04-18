from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.x86
"""

registers = {
    "E A X": "eax",
    "E B X": "ebx",
    "E C X": "ecx",
    "E D X": "edx",
    "E S I": "esi",
    "E D I": "edi",
    "stack": "esp",
    "E S P": "esp",
    "frame": "ebp",
    "E B P": "ebp",
    "E I P": "eip",
}

ctx.lists["user.registers"] = registers
