from talon import Context, Module, actions

# Maps language mode names to the extensions that activate them. Only put things
# here which have a supported language mode; that's why there are so many
# commented out entries. TODO: make this a csv file?
language_extensions = {
    ".asm": "assembly",
    ".bat": "batch",
    ".bt": "bpftrace",
    ".c": "c",
    ".cmake": "cmake",
    ".codeql": "ql",
    ".cpp": "cplusplus",
    ".cs": "csharp",
    ".elm": "elm",
    ".gdb": "gdb",
    ".go": "go",
    ".h": "c",
    ".hpp": "cplusplus",
    ".ini": "ini",
    ".java": "java",
    ".js": "javascript",
    ".jsx": "javascript",
    ".json": "json",
    ".json5": "json",
    ".lua": "lua",
    ".php": "php",
    ".md": "markdown",
    ".nix": "nix",
    ".nse": "lua",
    ".pl": "perl",
    ".ps1": "powershell",
    ".ps": "postscript",
    ".py": "python",
    ".ql": "codeql",
    ".r": "r",
    ".rb": "ruby",
    ".rs": "rust",
    ".s": "assembly",
    ".scm": "treesitter",  # NOTE: If you don't write treesitter queries, you may want this to be scheme
    ".sh": "bash",
    ".snippets": "snippets",
    ".sql": "sql",
    ".talon": "talon",
    ".task": "taskwarrior",
    ".toml": "toml",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".vba": "vba",
    ".vim": "vimscript",
    ".vimrc": "vimscript",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".zsh": "zsh",
}

# This list can be indirectly updated by other modules when they know at some
# language should be implicitly enabled for a specific context, for instance
# detecting the application repl is running in a terminal. Note that this is
# different than the auto_lang mode, which sets a global mode across all
# talon contexts.
# XXX - we might want to change this to try to be closer to the new auto_lang
# changes
forced_context_language = None


# Files that don't have specific extensions bit that are known to be associated
# with specific languages. Ex: CMakeLists.txt is cmake
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
    "r": ["are language"],
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
        if file_extension and file_extension in extension_lang_map:
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
