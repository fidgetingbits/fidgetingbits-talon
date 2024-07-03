import pathlib
import json
from talon import Module, actions, ui, registry

mod = Module()

vscode_plugin_cache = None


@mod.scope
def scope():
    return {"vscode_plugin": vscode_plugin_list()}


def vscode_update_plugin_list():
    """Queries the list of vscode plugins"""
    extensions = pathlib.Path.home() / ".vscode/extensions/extensions.json"
    if not extensions.exists():
        return []
    with extensions.open() as f:
        return [x["identifier"]["id"] for x in json.loads(f.read())]


def vscode_plugin_list():
    """Returns a cached or new list of installed vscode plugins"""
    global vscode_plugin_cache
    if vscode_plugin_cache is None:
        vscode_plugin_cache = vscode_update_plugin_list()
    if vscode_plugin_cache is None:
        return []
    return set(vscode_plugin_cache)


@mod.action_class
class PluginActions:
    def vscode_plugin_list_refresh():
        """Refresh the cached list of installed vscode plugins"""
        global vscode_plugin_cache
        vscode_plugin_cache = vscode_update_plugin_list()
        scope.update()

    def vscode_plugin_list_print():
        """Print the list of installed vscode plugins"""
        global vscode_plugin_cache
        if vscode_plugin_cache is None:
            actions.user.vscode_plugin_list_refresh()
        print(vscode_plugin_cache)


ui.register("win_focus", scope.update)
ui.register("win_title", scope.update)
