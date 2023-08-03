from talon import Context, Module

mod = Module()
mod.tag("arm", desc=r"Tag for enabling arm assembly functionality")
ctx = Context()
ctx.matches = r"""
tag: user.aarch64
"""

registers = {
    # 64-bit registers
    "zero": "x0",
    "one": "x1",
    "two": "x2",
    "three": "x3",
    "four": "x4",
    "five": "x5",
    "six": "x6",
    "seven": "x7",
    "eight": "x8",
    "nine": "x9",
    "ten": "x10",
    "eleven": "x11",
    "twelve": "x12",
    "thirteen": "x13",
    "fourteen": "x14",
    "fifteen": "x15",
    "sixteen": "x16",
    "seventeen": "x17",
    "eighteen": "x18",
    "nineteen": "x19",
    "twenty": "x20",
    "twenty one": "x21",
    "twenty two": "x22",
    "twenty three": "x23",
    "twenty four": "x24",
    "twenty five": "x25",
    "twenty six": "x26",
    "twenty seven": "x27",
    "twenty eight": "x28",
    "twenty nine": "x29",
    "thirty": "x30",
    # 32-bit registers
    "half zero": "w0",
    "half one": "w1",
    "half two": "w2",
    "half three": "w3",
    "half four": "w4",
    "half five": "w5",
    "half six": "w6",
    "half seven": "w7",
    "half eight": "w8",
    "half nine": "w9",
    "half ten": "w10",
    "half eleven": "w11",
    "half twelve": "w12",
    "half thirteen": "w13",
    "half fourteen": "w14",
    "half fifteen": "w15",
    "half sixteen": "w16",
    "half seventeen": "w17",
    "half eighteen": "w18",
    "half nineteen": "w19",
    "half twenty": "w20",
    "half twenty one": "w21",
    "half twenty two": "w22",
    "half twenty three": "w23",
    "half twenty four": "w24",
    "half twenty five": "w25",
    # special names
    "stack pointer": "sp",
    "program counter": "pc",
}


ctx.lists["user.registers"] = registers
