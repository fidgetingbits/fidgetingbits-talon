app: vscode
and code.language: markdown
-

# This includes built-in markdown settings, as well as the markdown-all-in-one extension

# built-in
[file] preview: user.vscode("markdown.showPreview")
file split preview: user.vscode("markdown.showPreviewToSide")

# markdown-all-in-one
# Actions: https://github.com/yzhang-gh/vscode-markdown/blob/master/package.json
# NOTE: Also see cursorless actions_custom.csv

generate talk:
    edit.file_start()
    user.vscode("markdown.extension.toc.create")
    key(enter)
toggle item: user.vscode("markdown.extension.checkTaskList")
