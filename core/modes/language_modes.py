from talon import Context, Module, actions

# Maps language mode names to the extensions that activate them. Only put things
# here which have a supported language mode; that's why there are so many
# commented out entries. TODO: make this a csv file?
language_extensions = {
    "assembly": "asm",
    "batch": "bat",
    "bpftrace": "bt",
    "c": "c",
    "cmake": "cmake",
    "ql": "codeql",
    "cplusplus": "cpp",
    "csharp": "cs",
    "elm": "elm",
    "gdb": "gdb",
    "go": "go",
    "c": "h",
    "cplusplus": "hpp",
    "ini": "ini",
    "java": "java",
    "javascript": "js",
    "javascript": "jsx",
    "json": "json",
    "json": "json5",
    "lua": "lua",
    "php": "php",
    "markdown": "md",
    "nix": "nix",
    "lua": "nse",
    "perl": "pl",
    "powershell": "ps1",
    "postscript": "ps",
    "python": "py",
    "codeql": "ql",
    "r": "r",
    "ruby": "rb",
    "rust": "rs",
    "assembly": "s",
    "treesitter": "scm",  # NOTE: If you don't write treesitter queries, you may want this to be scheme
    "bash": "sh",
    "snippet": "snippet",
    "sql": "sql",
    "talon": "talon",
    "taskwarrior": "task",
    "toml": "toml",
    "typescript": "ts",
    "typescript": "tsx",
    "vba": "vba",
    "vimscript": "vim",
    "vimscript": "vimrc",
    "yaml": "yaml",
    "yaml": "yml",
    "zsh": "zsh",
}

# This list can be indirectly updated by other modules when they know at some
# language should be implicitly enabled for a specific context, for instance
# detecting the application repl is running in a terminal. Note that this is
# different than the auto_lang mode, which sets a global mode across all
# talon contexts.
# XXX - we might want to change this to try to be closer to the new auto_lang
# changes
forced_context_language = None


# Files without specific extensions but are associated with languages
special_file_map = {
    "CMakeLists.txt": "cmake",
    "Makefile": "make",
    "Dockerfile": "docker",
    "meson.build": "meson",
    ".bashrc": "bash",
    ".zshrc": "zsh",
    "PKGBUILD": "pkgbuild",
    ".vimrc": "vimscript",
    "vimrc": "vimscript",
}

# Override speakable forms for language modes. If not present, a language mode's
# name is used directly.
language_name_overrides = {
    "cplusplus": ["see plus plus"],
    "csharp": ["see sharp"],
    "css": ["c s s"],
    "gdb": ["g d b"],
    "go": ["go", "go lang", "go language"],
    "r": ["are lang", "are language"],
    "scm": ["scheme", "s c m", "tree sitter"],
    "tex": ["tech", "lay tech", "latex"],
}

mod = Module()
ctx = Context()

ctx_forced = Context()
ctx_forced.matches = r"""
tag: user.code_language_forced
"""


mod.tag("code_language_forced", "This tag is active when a language mode is forced")
mod.list("language_mode", desc="Name of a programming language mode.")

ctx.lists["self.language_mode"] = {
    name: language
    for language in language_extensions
    for name in language_name_overrides.get(language, [language])
}

# Maps extension to languages.
extension_lang_map = {
    "." + ext: language
    for language, extensions in language_extensions.items()
    for ext in extensions.split()
}

language_ids = set(language_extensions.keys())

forced_language = ""


@ctx.action_class("code")
class CodeActions:
    def language():
        file_name = actions.win.filename()
        if file_name in special_file_map:
            return special_file_map[file_name]

        file_extension = actions.win.file_ext()
        return extension_lang_map.get(file_extension, "")


@ctx_forced.action_class("code")
class ForcedCodeActions:
    def language():
        return forced_language


@mod.action_class
class Actions:
    def code_set_context_language(language: str):
        """Sets the active language for this context"""
        global forced_context_language
        forced_context_language = language

    def code_clear_context_language():
        """Unsets the active language for this context"""
        global forced_context_language
        forced_context_language = None

    def code_set_language_mode(language: str):
        """Sets the active language mode, and disables extension matching"""
        global forced_language
        assert language in language_extensions
        forced_language = language
        # Update tags to force a context refresh. Otherwise `code.language` will not update.
        # Necessary to first set an empty list otherwise you can't move from one forced language to another.
        ctx.tags = []
        ctx.tags = ["user.code_language_forced"]

    def code_clear_language_mode():
        """Clears the active language mode, and re-enables code.language: extension matching"""
        global forced_language
        forced_language = ""
        ctx.tags = []

    def code_show_forced_language_mode():
        """Unsets the active language for this context"""
        print(
            f"Forced languages: {[t[:len('_forced')] for t in ctx.tags if t.endswith('_forced')]}"
        )
