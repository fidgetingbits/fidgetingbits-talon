from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    # FIXME: This should use the function that will spawn code if it's not running already, once it's implemented
    def vscode_open_workspace(name: str, phrase: str = None):
        """Open a workspace in vscode"""
        actions.user.switcher_focus("code")
        actions.sleep("300ms")
        actions.user.vscode("workbench.action.openRecent")
        actions.sleep("250ms")
        actions.insert(name)
        actions.key("enter")
        actions.sleep("250ms")
        actions.user.parse_phrase(phrase)
