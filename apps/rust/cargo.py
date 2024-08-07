import subprocess
import shutil
from pathlib import Path

from talon import Context, Module, actions, resource

mod = Module()
ctx = Context()

mod.list("cargo_crates", desc="Install packages inside a Cargo.toml")


def cargo_crates():
    # tomlq '.["dependencies"] | keys[]' Cargo.toml
    if not shutil.which("tomlq"):
        return []
    query = '.["dependencies"] | keys[]'
    return subprocess.check_output(
        ("tomlq", query, "Cargo.toml"), cwd=actions.user.get_cwd()
    ).decode("utf-8")


@ctx.dynamic_list("user.cargo_crates")
def user_cargo_crates(m) -> dict[str, str]:
    """A dynamic list of staged git files"""

    crates = cargo_crates()
    return actions.user.create_spoken_forms_from_list(crates)
