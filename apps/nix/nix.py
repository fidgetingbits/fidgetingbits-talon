import subprocess
import os
from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: terminal
and tag: user.nix_cli
"""

mod.list("flake_inputs", desc="Inputs defined by a nix foodflake")
mod.list("flake_outputs", desc="Outputs defined by a nix foodflake")


def read_flake_metadata() -> str:
    """Ensure flake exists and return metadata as json string"""
    if not os.path.exists(f"{actions.user.zsh_get_cwd()}/flake.nix"):
        print("no flake.nix")
        return {}

    result = subprocess.run(
        ["nix", "flake", "metadata", "--json"],
        capture_output=True,
        text=True,
        check=True,
        cwd=actions.user.zsh_get_cwd(),
        # stdout=subprocess.PIPE,
    )
    return result.stdout


@ctx.dynamic_list("user.flake_outputs")
def user_flake_outputs(m) -> dict[str, str]:
    """A dynamic list of nix flake outputs"""
    result = read_flake_metadata()
    output = subprocess.run(
        ["jq", "-r", ".locks.nodes.root.outputs | keys[]"],
        input=result,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    print(output)


@ctx.dynamic_list("user.flake_inputs")
def user_flake_inputs(m) -> dict[str, str]:
    """A dynamic list of nix flake inputs"""

    # FIXME: We should probably jump to the git root and test again to make this more powerful
    result = read_flake_metadata()
    output = subprocess.run(
        ["jq", "-r", ".locks.nodes.root.inputs | keys[]"],
        input=result,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    # print(output)

    return actions.user.create_spoken_forms_from_list(output.splitlines())
