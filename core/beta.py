from talon import Module, app

mod = Module()


@mod.scope
def scope():
    return {"talon_branch": app.branch}
