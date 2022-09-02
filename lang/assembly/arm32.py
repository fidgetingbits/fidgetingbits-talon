from talon import Context, Module

mod = Module()
mod.tag("arm32", desc=r"Tag for enabling arm32 functionality")
ctx = Context()
ctx.matches = r"""
tag: user.arm32
"""

registers = {
    # general purpose
    "zero": "r0",
    "one": "r1",
    "two": "r2",
    "three": "r3",
    "four": "r4",
    "five": "r5",
    "six": "r6",
    "seven": "r7",
    "eight": "r8",
    "nine": "r9",
    "ten": "r10",
    "eleven": "r11",
    "twelve": "r12",
    "thirteen": "r13",
    "fourteen": "r14",
    "fifteen": "r15",
    "link": "lr",
    "stack": "sp",
    # pointers
    "instruction": "pc",
    "P C": "pc",
}
ctx.lists["user.registers"] = registers
