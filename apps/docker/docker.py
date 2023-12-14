from talon import Context, Module, actions

mod = Module()
mod.tag("docker", desc="tag for enabling docker commands in your terminal")
mod.setting(
    "docker_uses_sudo",
    type=bool,
    default=False,
    desc="Whether or not docker commands should be prefixed with sudo.",
)

ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.docker

tag: terminal
and tag: user.podman
"""


@mod.action_class
class Actions:
    def docker(command: str = ""):
        """Run docker command"""
        actions.insert("docker " + command)

    def docker_compose(command: str = ""):
        """Run docker compose command"""
        actions.insert("docker compose " + command)

    def docker_viz(command: str = ""):
        """Run dockviz command"""
        actions.insert("dockviz " + command)
