from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

key = actions.key
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
    ".py": "python",
    ".ql": "codeql",
    ".r": "r",
    ".rb": "ruby",
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


@ctx.action_class("code")
class code_actions:
    def language():
        if forced_context_language is not None:
            return forced_context_language
        file_extension = actions.win.file_ext()
        # print(f"!! file extension: {file_extension}")
        file_name = actions.win.filename()
        # print(f"!! file name: {file_name}")

        # Favor full matches
        if file_name in special_file_map:
            return special_file_map[file_name]

        if file_extension and file_extension in extension_lang_map:
            return extension_lang_map[file_extension]


# create a mode for each defined language
for d in (extension_lang_map, special_file_map):
    for __, lang in d.items():
        mod.mode(lang)
        mod.tag(lang)

# Create a mode for the automated language detection. This is active when no
# lang is forced.
mod.mode("auto_lang")

# Auto lang is enabled by default
app.register("ready", lambda: actions.user.code_clear_language_mode())


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
        actions.user.code_clear_language_mode()
        actions.mode.disable("user.auto_lang")
        actions.mode.enable("user.{}".format(language))
        app.notify(subtitle="Enabled {} mode".format(language))

    def code_clear_language_mode():
        """Clears the active language mode, and re-enables code.language: extension matching"""
        actions.mode.enable("user.auto_lang")
        for _, lang in extension_lang_map.items():
            actions.mode.disable("user.{}".format(lang))
