from talon import Context, Module, actions, app, speech_system

ctx = Context()
mod = Module()
ABORT_WORDS = ["abort"]

mod.list("abort_word", desc="Aborts the current command if heard")
ctx.lists["self.abort_word"] = ABORT_WORDS


def fn(d):
    if "parsed" not in d.keys():
        return
    words = d["parsed"]._unmapped
    if words[-1] in ABORT_WORDS and actions.speech.enabled():
        d["parsed"]._sequence = []
        app.notify(subtitle=f"Command aborted due to one of {ABORT_WORDS}")


speech_system.register("pre:phrase", fn)
