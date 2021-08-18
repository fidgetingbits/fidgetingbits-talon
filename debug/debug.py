from collections import OrderedDict
from talon import Context, Module, registry, ui, speech_system, scope, actions
import talon.scripting.core.debug as debug
import talon.scripting.rctx as rctx
import pprint

ctx = Context()
mod = Module()

# Unable to print all window updates the talon sees
# ui.register('', print)
pp = pprint.PrettyPrinter(indent=4)
@mod.action_class
class module_actions:
    def debug_active_context():
        """dump out the active contexts"""
        print(registry.active_contexts())

    def debug_benchmark():
        """dump out the active contexts"""
        rctx.flush()
        actions._debug.dfa_benchmark()

    def debug_dfa_watchdogs():
        """dump out data"""
        print("-------DEBUG DFA WATCHDOGS START-------")
        pp.pprint(scope.data)
        print("-------DEBUG DFA WATCHDOGS END-------")

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


    def debug_registry_commands():
        """dump out the largest registry lists for a given context"""
        d = {}
        print(f"Commands: {len(registry.commands)}")
        for key, item in registry.commands.items():
            print(key)
        for ent in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print(f"{ent[1]}: {ent[0]}")



    def debug_registry_lists():
        """dump out the largest registry lists for a given context"""
        d = {}
        for key, item in registry.lists.items():
            d[key] = len(item[-1])
        for ent in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print(f"{ent[1]}: {ent[0]}")

    def debug_grammar_list():
        """dump out the largest registry lists for a given context"""
        print(f"NFA:")
        d = {}
        for key, item in speech_system.grammar.list_nfas.items():
            d[key] = len(item[0])
        for ent in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print(f"{ent[1]}: {ent[0]}")
