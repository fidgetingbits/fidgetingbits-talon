app: vscode
and tag: user.markdown
-

# This includes built-in markdown settings, as well as the markdown-all-in-one extension

# built-in
file preview: user.vscode("markdown.showPreview")

# markdown-all-in-one
# Actions: https://github.com/yzhang-gh/vscode-markdown/blob/master/package.json
# NOTE: Also see cursorless actions_custom.csv

generate talk: user.vscode("markdown.extension.toc.create")
toggle item: user.vscode("markdown.extension.checkTaskList")
