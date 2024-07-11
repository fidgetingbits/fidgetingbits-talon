import subprocess
from dataclasses import dataclass
from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app: terminal
tag: user.systemd
"""


@dataclass
class SystemdService:
    unit: str
    load: str
    active: str
    sub: str
    description: str

    @staticmethod
    def from_line(line: str) -> "SystemdService":
        items = line.lstrip().split()
        unit, load, active, sub = items[:4]
        description = " ".join(items[4:])
        return SystemdService(unit, load, active, sub, description)


def get_user_services() -> list[SystemdService]:
    return get_services(user=True)


def get_services(user: bool = False) -> list[SystemdService]:
    user_flag = "--user" if user else ""
    services = subprocess.check_output(
        (
            "systemctl",
            f"{user_flag}",
            "list-units",
            "--type=service",
            "--no-pager",
            "--all",
        ),
    ).decode("utf-8")
    if len(services) == 0:
        return []
    return parse_services(services)


def parse_services(input: str) -> list[SystemdService]:
    services = []
    for line in input.splitlines():
        if not len(line) or line.startswith("UNIT"):
            continue
        if line.startswith("Legend:"):
            break
        services.append(SystemdService.from_line(line))

    return services


def active_services(
    services: list[SystemdService],
) -> list[SystemdService]:
    return [service for service in services if service.active == "active"]


def inactive_services(
    services: list[SystemdService],
) -> list[SystemdService]:
    return [service for service in services if service.active == "inactive"]


@ctx.dynamic_list("user.service_all_system_services")
def user_service_all_system_services(m) -> dict[str, str]:
    """A dynamic list of all running system services"""

    # FIXME: maybe strip off the .service suffix?
    service_names = [service.unit for service in get_services()]
    return actions.user.create_spoken_forms_from_list(service_names)


@ctx.dynamic_list("user.service_all_user_services")
def user_service_all_user_services(m) -> dict[str, str]:
    """A dynamic list of all running user services"""

    # FIXME: maybe strip off the .service suffix?
    service_names = [service.unit for service in get_user_services()]
    return actions.user.create_spoken_forms_from_list(service_names)


@ctx.dynamic_list("user.service_active_user_services")
def user_service_active_user_services(m) -> dict[str, str]:
    """A dynamic list of all active user services"""

    service_names = [service.unit for service in active_services(get_user_services())]
    return actions.user.create_spoken_forms_from_list(service_names)


@ctx.dynamic_list("user.service_inactive_user_services")
def user_service_inactive_user_services(m) -> dict[str, str]:
    """A dynamic list of all inactive user services"""

    service_names = [service.unit for service in inactive_services(get_user_services())]
    return actions.user.create_spoken_forms_from_list(service_names)


# FIXME(systemd): Reuse the same functions across user and system, ant just pass a boolean flag


def _service_list_state(state: str, user: bool = False):
    actions.insert(
        f"systemctl {'--user' if user else ''} list-units --type=service --no-pager --state={state}\n"
    )


@ctx.action_class("user")
class UserActions:
    # System-wide services
    def service():
        actions.user.insert_between("systemctl --no-pager ", ".service")

    def service_list(all):
        actions.insert(
            f"systemctl list-units --type=service --no-pager {'--all' if all else ''}\n"
        )

    def service_list_active():
        _service_list_state("active")

    def service_list_inactive():
        _service_list_state("inactive")

    def service_list_running():
        _service_list_state("running")

    def service_list_exited():
        _service_list_state("exited")

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

    def service_user_list_active():
        _service_list_state("active", user=True)

    def service_user_list_inactive():
        _service_list_state("inactive", user=True)

    def service_user_list_running():
        _service_list_state("running", user=True)

    def service_user_list_exited():
        _service_list_state("exited", user=True)

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
