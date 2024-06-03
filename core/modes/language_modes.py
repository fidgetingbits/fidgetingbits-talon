from talon import Context, Module, actions, app

# Maps language mode names to the extensions that activate them. Only put things
# here which have a supported language mode; that's why there are so many
# commented out entries. TODO: make this a csv file?
language_extensions = {
    "assembly": "asm",
    "bash": "sh",
    "batch": "bat",
    "bpftrace": "bt",
    "c": "c h",
    "cmake": "cmake",
    "ql": "codeql",
    "cplusplus": "cpp hpp",
    "csharp": "cs",
    "elm": "elm",
    "gdb": "gdb",
    "go": "go",
    "ini": "ini",
    "java": "java",
    "javascript": "js",
    "javascriptreact": "jsx",
    "json": "json json5",
    "lua": "lua nse",
    "php": "php",
    "markdown": "md",
    "nix": "nix",
    "perl": "pl",
    "powershell": "ps1",
    "postscript": "ps",
    "python": "py",
    "codeql": "ql",
    "r": "r",
    "ruby": "rb",
    "rust": "rs",
    "treesitter": "scm",  # NOTE: If you don't write treesitter queries, you may want this to be scheme
    "snippet": "snippet",
    "sql": "sql",
    "talon": "talon",
    "taskwarrior": "task",
    "toml": "toml",
    "typescript": "ts",
    "typescriptreact": "tsx",
    "vba": "vba",
    "vimscript": "vim vimrc",
    "yaml": "yaml yml",
    "zsh": "zsh",
}

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
        return actions.user.code_get_forced_language()


@mod.action_class
class Actions:
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
        """Show the active language for this context"""
        forced = actions.user.code_get_forced_language()
        if len(forced):
            app.notify(f"Forced language: {forced}")

    def code_get_forced_language_with_fallback(fallback: str) -> str:
        """Allows an app to force a language as a fallback, but still favor the user's forced language if it's set"""
        if len(forced_language):
            return forced_language
        if fallback:
            if fallback in language_ids:
                return fallback
            else:
                print(f"ERROR: Invalid fallback language specified: {fallback}")
        return None

    def code_get_forced_language():
        """Return the currently forced language"""
        return actions.user.code_get_forced_language_with_fallback(None)
