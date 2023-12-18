from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: user.muslheap
"""


@ctx.action_class("user")
class UserActions:
    def heap_analysis_chunk():
        actions.auto_insert("mchunkinfo ")
