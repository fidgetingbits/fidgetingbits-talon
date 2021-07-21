from talon import Context, actions

ctx = Context()


@ctx.action_class("edit")
class EditActions:
    # actions that should be set no matter what context we are in
    # for generic os-specific see apps/linux/edit.talon
    # for more application-specific see apps/linux/shell_edit_emacs.talon,
    # apps/linux/vim/editing.talon, etc

    def delete():
        actions.key("backspace")

    def down():
        actions.key("down")

    def up():
        actions.key("up")

    def left():
        actions.key("left")

    def right():
        actions.key("right")
