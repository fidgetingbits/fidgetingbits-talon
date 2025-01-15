app: vscode
-
# FIXME: Some of these should be generic for suggestions, and may be the copilot specific ones key to off of the plugin being installed

pilot jest: user.vscode("editor.action.inlineSuggest.trigger")
previous | pilot next: user.vscode("editor.action.inlineSuggest.showNext")
pilot (last): user.vscode("editor.action.inlineSuggest.showPrevious")
(pie dog|pilot dog|copilot): user.vscode("workbench.action.toggleAuxiliaryBar")
pilot word: user.vscode("editor.action.inlineSuggest.acceptNextWord")
pilot nope: user.vscode("editor.action.inlineSuggest.undo")
pilot cancel: user.vscode("editor.action.inlineSuggest.hide")
pilot generate: user.vscode("github.copilot.generate")
pilot pan next: user.vscode("github.copilot.nextPanelSuggestion")
pilot pan (previous | last): user.vscode("github.copilot.previousPanelSuggestion")
pilot [pan] (accept | commit): user.vscode("github.copilot.acceptPanelSuggestion")
[pilot] (keeper | keep): user.vscode("editor.action.inlineSuggest.commit")
# FIXME: add the ability to add cursorless targets to this
pilot explain: user.vscode("github.copilot.chat.explain.palette")
