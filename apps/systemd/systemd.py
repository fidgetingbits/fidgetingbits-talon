from talon import Context, actions

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.systemd
"""


@ctx.action_class("user")
class UserActions:
    # System-wide services
    def service():
        actions.user.insert_between("systemctl --no-pager ", ".service")

    def service_list(all):
        actions.insert(
            f"systemctl list-units --type=service --no-pager {'--all' if all else ''}\n"
        )

    def service_find():
        actions.insert("systemctl list-units --type=service --no-pager | grep ")

    def service_stop():
        actions.user.insert_between("systemctl --no-pager stop ", ".service")

    def service_start():
        actions.user.insert_between("systemctl --no-pager start ", ".service")

    def service_restart():
        actions.user.insert_between("systemctl --no-pager restart ", ".service")

    def service_status():
        actions.user.insert_between("systemctl --no-pager status ", ".service")

    def service_enable():
        actions.user.insert_between("systemctl --no-pager enable ", ".service")

    def service_disable():
        actions.user.insert_between("systemctl --no-pager disable ", ".service")

    def service_status_by_name(name: str):
        actions.insert(f"systemctl --no-pager status {name}")

    def service_stop_by_name(name: str):
        actions.insert(f"systemctl stop {name}")

    def service_start_by_name(name: str):
        actions.insert(f"systemctl start {name}")

    def service_restart_by_name(name: str):
        actions.insert(f"systemctl restart {name}")

    def service_enable_by_name(name: str):
        actions.insert(f"systemctl enable {name}")

    def service_disable_by_name(name: str):
        actions.insert(f"systemctl disable {name}")

    # User services
    def service_user():
        actions.user.insert_between("systemctl --user --no-pager ", ".service")

    def service_user_list(all: bool):
        actions.insert(
            f"systemctl --user list-units --type=service --no-pager {'--all' if all else ''}\n"
        )

    def service_user_find():
        actions.insert("systemctl --user list-units --type=service --no-pager | grep ")

    def service_user_stop():
        actions.user.insert_between("systemctl --user --no-pager stop ", ".service")

    def service_user_start():
        actions.user.insert_between("systemctl --user --no-pager start ", ".service")

    def service_user_restart():
        actions.user.insert_between("systemctl --user --no-pager restart ", ".service")

    def service_user_status():
        actions.user.insert_between("systemctl --user --no-pager status ", ".service")

    def service_user_enable():
        actions.user.insert_between("systemctl --user --no-pager enable ", ".service")

    def service_user_disable():
        actions.user.insert_between("systemctl --user --no-pager disable ", ".service")

    def service_user_status_by_name(name: str):
        actions.insert(f"systemctl --user --no-pager status {name}")

    def service_user_stop_by_name(name: str):
        actions.insert(f"systemctl --user stop {name}")

    def service_user_start_by_name(name: str):
        actions.insert(f"systemctl --user start {name}")

    def service_user_restart_by_name(name: str):
        actions.insert(f"systemctl --user restart {name}")

    def service_user_enable_by_name(name: str):
        actions.insert(f"systemctl --user enable {name}")

    def service_user_disable_by_name(name: str):
        actions.insert(f"systemctl --user disable {name}")

    # System-Wide timers
    def timer():
        actions.user.insert_between("systemctl --no-pager ", ".timer")

    def timer_stop():
        actions.user.insert_between("systemctl --no-pager stop ", ".timer")

    def timer_start():
        actions.user.insert_between("systemctl --no-pager start ", ".timer")

    def timer_restart():
        actions.user.insert_between("systemctl --no-pager restart ", ".timer")

    def timer_status():
        actions.user.insert_between("systemctl --no-pager status ", ".timer")

    def timer_enable():
        actions.user.insert_between("systemctl --no-pager enable ", ".timer")

    def timer_disable():
        actions.user.insert_between("systemctl --no-pager disable ", ".timer")

    # User timers
    def timer_user():
        actions.user.insert_between("systemctl --user --no-pager ", ".timer")

    def timer_user_stop():
        actions.user.insert_between("systemctl --user --no-pager stop ", ".timer")

    def timer_user_start():
        actions.user.insert_between("systemctl --user --no-pager start ", ".timer")

    def timer_user_restart():
        actions.user.insert_between("systemctl --user --no-pager restart ", ".timer")

    def timer_user_status():
        actions.user.insert_between("systemctl --user --no-pager status ", ".timer")

    def timer_user_enable():
        actions.user.insert_between("systemctl --user --no-pager enable ", ".timer")

    def timer_user_disable():
        actions.user.insert_between("systemctl --user --no-pager disable ", ".timer")
