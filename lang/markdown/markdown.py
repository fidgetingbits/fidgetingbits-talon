from talon import Context, Module

mod = Module()
ctx = Context()

ctx.matches = r"""
code.language: markdown
"""

mod.list("markdown_code_block_language", desc="Languages for code blocks")
# You can find lists of languages here: https://github.com/github-linguist/linguist/blob/master/vendor/README.md
ctx.lists["user.markdown_code_block_language"] = {
    "typescript": "typescript",
    "python": "python",
    "ruby": "ruby",
    "shell": "shell",
    "bash": "bash",
    "json": "json",
    "rust": "rust",
    "java script": "js",
    "makefile": "makefile",
    "assembly": "nasm",
    "post script": "postscript",
    "see": "cpp",
    "vim": "vim",
    "lua": "lua",
    "yaml": "yaml",
    "X M L": "xml",
    "go": "go",
    "diff": "diff",
    "patch": "diff",
    "C sharp": "csharp",
    "nix": "nix",
}
