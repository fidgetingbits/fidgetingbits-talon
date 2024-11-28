app: vscode
and win.title: /Merging:/
-

conflict next: user.vscode("merge.goToNextUnhandledConflict")
conflict prev: user.vscode("merge.goToPreviousUnhandledConflict")

merge complete: user.vscode("git.acceptMerge")
merge left: user.vscode("merge.acceptAllInput1")
merge right: user.vscode("merge.acceptAllInput2")
