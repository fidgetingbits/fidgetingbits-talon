app: vscode
code.language: python
-

# FIXME: Make this abstract so that you can just quick fix and it defaults to whatever linter is there for the language
ruff quick fix all: user.vscode("ruff.executeAutofix")
