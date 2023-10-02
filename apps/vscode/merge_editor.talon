app: vscode
and win.title: /Merging:/
-

conflict next: user.vscode("merge.goToNextUnhandledConflict")
conflict prev: user.vscode("merge.goToPreviousUnhandledConflict")

merge complete: user.vscode("git.acceptMerge")
