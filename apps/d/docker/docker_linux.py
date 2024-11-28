from talon import Context, actions, settings

ctx = Context()
ctx.matches = r"""
os: linux
and tag: terminal
and tag: user.docker

os: linux
and tag: terminal
and tag: user.podman
"""

prefix = settings.get("user.docker_uses_sudo", False) and "sudo " or ""


@ctx.action_class("user")
class UserActions:
    def docker(command: str = ""):
        actions.insert(f"{prefix}docker " + command)

    def docker_compose(command: str = ""):
        actions.insert(f"{prefix}docker compose " + command)

    def docker_viz(command: str = ""):
        actions.insert(f"{prefix}dockviz " + command)
