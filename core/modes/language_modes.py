from talon import Context, Module, actions

ctx = Context()
mod = Module()

extension_lang_map = {
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
    ".sh": "bash",
    ".snippets": "snippets",
    ".sql": "sql",
    ".talon": "talon",
    ".task": "taskwarrior",
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

# Maps language mode names to the extensions that activate them. Only put things
# here which have a supported language mode; that's why there are so many
# commented out entries. TODO: make this a csv file?
language_extensions = {
    # 'assembly': 'asm s',
    "bash": "bashbook sh",
    "batch": "bat",
    "c": "c h",
    "codeql": "codeql",
    "cmake": "cmake",
    # 'cplusplus': 'cpp hpp',
    "csharp": "cs",
    "css": "css",
    # 'elisp': 'el',
    # 'elm': 'elm',
    "gdb": "gdb",
    "go": "go",
    # 'html': 'html',
    "java": "java",
    "javascript": "js",
    "javascriptreact": "jsx",
    # 'json': 'json',
    "lua": "lua",
    "make": "make",
    "markdown": "md",
    # 'perl': 'pl',
    "php": "php",
    # 'powershell': 'ps1',
    "python": "py",
    "protobuf": "proto",
    "r": "r",
    # 'racket': 'rkt',
    "ruby": "rb",
    "rust": "rs",
    "scala": "scala",
    "scss": "scss",
    # 'snippets': 'snippets',
    "sql": "sql",
    "talon": "talon",
    "terraform": "tf",
    "typescript": "ts",
    "typescriptreact": "tsx",
    # 'vba': 'vba',
    "vimscript": "vim vimrc",
    "zsh": "zsh",
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
}
mod.list("language_mode", desc="Name of a programming language mode.")
ctx.lists["self.language_mode"] = {
    name: language
    for language in language_extensions
    for name in language_name_overrides.get(language, [language])
}

# Maps extension to languages.
# XXX - Override this for now to use my hardcoded one above vs only what has
# known modes
# extension_lang_map = {
#    '.' + ext: language
#    for language, extensions in language_extensions.items()
#    for ext in extensions.split()
# }

# Create a context for each defined language
for lang in language_extensions.keys():
    mod.tag(lang)
    mod.tag(f"{lang}_forced")
    c = Context()
    # Context is active if language is forced or auto language matches
    # NOTE: I a special case vim here because otherwise even in normal and visual mode
    # their certain commands that will conflict, for instance commenting code like
    # "block comment" in visual mode
    c.matches = f"""

    not app: vim
    and tag: user.{lang}_forced

    not app: vim
    and tag: user.auto_lang
    and code.language: {lang}

    app: vim
    and tag: user.vim_insert_mode
    and tag: user.{lang}_forced

    app: vim
    and tag: user.vim_insert_mode
    and tag: user.auto_lang
    and code.language: {lang}

    """
    c.tags = [f"user.{lang}"]

# Create a mode for the automated language detection. This is active when no lang is forced.
mod.tag("auto_lang")
ctx.tags = ["user.auto_lang"]


@ctx.action_class("code")
class code_actions:
    def language():
        if forced_context_language is not None:
            return forced_context_language
        file_extension = actions.win.file_ext()
        file_name = actions.win.filename()
        # print(f"file_name: {file_name}")
        # print(f"file_extension: {file_extension}")
        # Favor full matches
        if file_name in special_file_map:
            return special_file_map[file_name]

        if file_extension and file_extension in extension_lang_map:
            return extension_lang_map[file_extension]


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
        assert language in language_extensions
        ctx.tags = [f"user.{language}_forced"]

    def code_clear_language_mode():
        """Clears the active language mode, and re-enables code.language: extension matching"""
        ctx.tags = ["user.auto_lang"]
