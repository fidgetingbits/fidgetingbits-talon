from talon import Context, Module

mod = Module()
mod.tag("x64", desc="Tag for enabling x64 functionality")
ctx = Context()
ctx.matches = r"""
tag: user.x64
"""

registers = {
    # general purpose
    "racks": "rax",
    "R A X": "rax",
    "R B X": "rbx",
    "R C X": "rcx",
    "R D X": "rdx",
    "R S I": "rsi",
    "R D I": "rdi",
    "stack": "rsp",
    "stack pointer": "rsp",
    "R S P": "rsp",
    "frame": "rbp",
    "frame pointer": "rbp",
    "base": "rbp",
    "base pointer": "rbp",
    "R B P": "rbp",
    "R eight": "r8",
    "R nine": "r9",
    "R ten": "r10",
    "R eleven": "r11",
    "R twelve": "r12",
    "R thirteen": "r13",
    "R fourteen": "r14",
    "R fifteen": "r15",
    # pointers
    "instruction": "rip",
    "rip": "rip",
    "R I P": "rip",
    # segment
}
ctx.lists["user.registers"] = registers
