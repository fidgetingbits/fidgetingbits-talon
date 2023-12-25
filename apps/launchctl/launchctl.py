from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.launchctl
"""

mod = Module()

macos_services = {
    "home D": "com.apple.homed",
}

nix_services = {
    "sops": "org.nix-community.home.sops-nix",
}

ctx.lists["user.service_names"] = {
    **macos_services,
    **nix_services,
}


@ctx.action_class("user")
class UserActions:
    def service():
        actions.insert("launchctl ")

    def service_list():
        actions.insert("launchctl list\n")

    def service_find():
        actions.insert("launchctl list | grep ")

    def service_help():
        actions.insert("launchctl help\n")

    def service_stop():
        actions.insert("launchctl stop ")

    def service_start():
        actions.insert("launchctl start ")

    def service_restart():
        actions.insert_between("launchctl stop ", " && launchctl start ")

    def service_status():
        actions.insert("launchctl list ")

    def service_enable():
        actions.insert("launchctl enable")

    def service_disable():
        actions.insert("launchctl disable")

    # System-Wide timers
    # def timer():
    #     actions.insert("launchctl ")

    # def timer_stop():
    #     actions.insert("launchctl ")

    # def timer_start():
    #     actions.insert("launchctl ")

    # def timer_restart():
    #     actions.insert("launchctl ")

    # def timer_status():
    #     actions.insert("launchctl ")

    # def timer_enable():
    #     actions.insert("launchctl ")

    # def timer_disable():
    #     actions.insert("launchctl ")

    # # User timers
    # def timer_user():
    #     actions.insert("launchctl ")

    # def timer_user_stop():
    #     actions.insert("launchctl ")

    # def timer_user_start():
    #     actions.insert("launchctl ")

    # def timer_user_restart():
    #     actions.insert("launchctl ")

    # def timer_user_status():
    #     actions.insert("launchctl ")

    # def timer_user_enable():
    #     actions.insert("launchctl ")

    # def timer_user_disable():
    #     actions.insert("launchctl ")

    def service_status_by_name(name: str):
        actions.insert(f"launchctl list {name}\n")

    def service_stop_by_name(name: str):
        actions.insert(f"launchctl stop {name}\n")

    def service_start_by_name(name: str):
        actions.insert(f"launchctl start {name}\n")

    def service_restart_by_name(name: str):
        actions.insert(f"launchctl stop {name}\n")
        actions.insert(f"launchctl start {name}\n")

    def service_enable_by_name(name: str):
        actions.insert(f"launchctl enable {name}\n")

    def service_disable_by_name(name: str):
        actions.insert(f"launchctl disable {name}\n")
