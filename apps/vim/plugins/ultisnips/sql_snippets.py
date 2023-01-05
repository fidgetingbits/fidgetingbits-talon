from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.sql
"""

# spoken name -> snippet name
# see plsql.snippets.
# TODO: only a limited number are added for now
ultisnips_snippets = {
    "comment": "doc",
    "header": "hdr",
    "select all": "sel",
    "select": "selc",
    "where row": "wrn",
    "and row": "arn",
    "prompt": "prmpt",
    "drop table": "drtab",
    "create table": "crtab",
    "column": "ccol",
    "add date": "dcol",
    "add number": "ncol",
    "alter table": "at",
}

private_snippets = {}

# TODO - when creating snippets from multiple language types, like python and
# SQL at the same time, we need a way to look for a conflict in the update.
ctx.lists["user.snippets"] = {**ultisnips_snippets, **private_snippets}
