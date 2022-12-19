from talon import Context, Module, actions, scripting

mod = Module()
ctx = Context()
#@ctx.action_class("main")
#class main_actions:
#    def insert(text: str):
#       """override global insert action to improve speed in some scenarios"""
#       actions.next(text)
#       #scripting.core.main.MainActions.insert(text)
