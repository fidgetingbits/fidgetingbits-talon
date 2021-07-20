from collections import OrderedDict
from talon import Context, Module, registry, ui, speech_system, scope

ctx = Context()
mod = Module()

# Unable to print all window updates the talon sees
# ui.register('', print)

@mod.action_class
class module_actions:
    def debug_active_context():
        """dump out the active contexts"""
        print(registry.active_contexts())

    def debug_lost_context():
        """TODO: Docstring for debug_lost_context.
        :returns: TODO

        """
        print("-------DEBUG LOST CONTEXT START-------")
        print(scope.data)
        print(registry.last_active_contexts)
        print(ui.active_app())
        print(ui.active_window())
        print(registry.commands)
        print(speech_system.engine.engine.cfg_blobs)
        print("-------DEBUG LOST CONTEXT END-------")
        pass

    def debug_registry_lists():
        """dump out the largest registry lists for a given context"""
        d = {}
        for key, item in registry.lists.items():
            d[key] = len(item[-1])
        for ent in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print(f"{ent[1]}: {ent[0]}")
