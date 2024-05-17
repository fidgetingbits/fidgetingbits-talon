import subprocess
import os
from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: terminal
and tag: user.nix_cli
"""

mod.list("flake_inputs", desc="Extensions currently installed in Gnome shell")


@ctx.dynamic_list("user.flake_inputs")
def user_flake_inputs(m) -> dict[str, str]:
    """A dynamic list of nix flake inputs"""

    # FIXME: We should probably jump to the git root and test again to make this more powerful
    if not os.path.exists(f"{actions.user.zsh_get_cwd()}/flake.nix"):
        print("no flake.nix")
        return {}
    # nix flake metadata --json | jq -r '.locks.nodes.root.inputs | keys[]'
    result = subprocess.run(
        ["nix", "flake", "metadata", "--json"],
        capture_output=True,
        text=True,
        check=True,
        cwd=actions.user.zsh_get_cwd(),
        # stdout=subprocess.PIPE,
    )
    output = subprocess.run(
        ["jq", "-r", ".locks.nodes.root.inputs | keys[]"],
        input=result.stdout,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    # print(output)

    return actions.user.create_spoken_forms_from_list(output.splitlines())
