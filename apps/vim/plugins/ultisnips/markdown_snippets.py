from talon import Context

ctx = Context()
ctx.matches = r"""
tag: user.vim_ultisnips
and tag: user.markdown
"""
# spoken name -> ultisnips snippet name
ctx.lists["user.snippets"] = {
    # Sections and Paragraphs #
    "section": "sec",
    "sub section": "ssec",
    "sub sub section": "sssec",
    "paragraph": "par",
    "sub paragraph": "spar",
    # Text formatting #
    "italics": "*",
    "bold": "**",
    "bold italics": "***",
    "strike through": "~~",
    "comment": "/*",
    # Common stuff #
    "link": "link",
    "image": "img",
    "inline code": "ilc",
    "code block": "cbl",
    "shell block": "shellcbl",
    "reference link": "refl",
    "footnote": "fnt",
    "detail": "detail",
}
