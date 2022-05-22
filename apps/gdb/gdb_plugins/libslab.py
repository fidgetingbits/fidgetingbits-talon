from talon import Context, Module, actions, app, settings

mod = Module()
mod.list("slabs", desc="A list of linux kernel slabs")

ctx = Context()
ctx.matches = r"""
tag: user.libslab
"""

ctx.lists["user.slabs"] = {
    "eight kay": "kmalloc-8k",
    "for kay": "kmalloc-4k",
    "to kay": "kmalloc-2k",
    "one ka": "kmalloc-1k",
    "five twelve": "kmalloc-512",
    "two fifty six": "kmalloc-256",
    "one nine two": "kmalloc-192",
    "one twenty eight": "kmalloc-128",
    "ninety six": "kmalloc-96",
    "sixty four": "kmalloc-64",
    "thirty two": "kmalloc-32",
    "sixteen": "kmalloc-16",
    "eight": "kmalloc-8",
}
