app: vscode
user.vscode_plugin: paulschaaf.talon-filetree
-
# See https://github.com/paul-schaaf/talon-filetree-commands/blob/master/tree.talon for original file
# This opens thbe file tree in the sidebar
bar tree: user.vscode("workbench.view.extension.filetree")

# File tree commands
tree <user.letters>:
    user.run_rpc_command("talon-filetree.toggleDirectoryOrOpenFile", letters)
tree parent <user.letters>: user.run_rpc_command("talon-filetree.closeParent", letters)
tree [unfold] <user.letters> <number>:
    user.run_rpc_command("talon-filetree.expandDirectory", letters, number)
tree (fold | collapse) <user.letters>:
    user.run_rpc_command("talon-filetree.expandDirectory", letters, 0)
tree move <user.letters> to <user.letters>:
    user.run_rpc_command("talon-filetree.moveFile", letters_1, letters_2)
tree move <user.letters> [to] root:
    user.run_rpc_command("talon-filetree.moveFile", letters_1)
# the recommended way to open a file is using the "toggleDirectoryOrOpenFile" command
# but this may be useful for people that want to separate the two actions
# e.g. to create very distinct commands that are easier for talon to differentiate
tree open <user.letters>: user.run_rpc_command("talon-filetree.openFile", letters)
tree rename <user.letters>: user.run_rpc_command("talon-filetree.renameFile", letters)
tree [file] new <user.letters>: user.run_rpc_command("talon-filetree.createFile", letters)
tree folder new <user.letters>:
    user.run_rpc_command("talon-filetree.createFile", letters)
    sleep(1)
    insert("/")
    key(left)
tree delete <user.letters>: user.run_rpc_command("talon-filetree.deleteFile", letters)
tree collapse root: user.run_rpc_command("talon-filetree.collapseRoot")
tree select <user.letters>: user.run_rpc_command("talon-filetree.select", letters)
tree git: user.run_rpc_command("talon-filetree.toggleGitIgnoredFiles")
tree current: user.run_rpc_command("talon-filetree.revealCurrentFile")
