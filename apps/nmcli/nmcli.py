import os
import subprocess
import shlex

from talon import Context, Module, actions, system

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""

mod.list("nmcli_vpns", desc="Configure network manager vpn connections")


@ctx.dynamic_list("user.nmcli_vpns")
def user_nmcli_vpns(m) -> dict[str, str]:
    """A dynamic list of VPN connections"""
    output = subprocess.check_output(
        ("bash", "-c", "nmcli -t -f NAME,TYPE connection show | rg vpn | cut -f1 -d:"),
        text=True,
    )
    if not output:
        print("no output")
        return {}

    return actions.user.create_spoken_forms_from_list(output.splitlines())


@mod.action_class
class NetworkManagerClientActions:
    def nmcli_connection_up(name: str):
        """Bring a network manager connection up using the cli"""
        actions.user.notify(f"Bringing up VPN {name}")
        # This will block on user input, so we have to run it in the background.
        # NOTE: shlex doesn't work on windows, but this is linux only
        args = shlex.split(f"bash -c 'nmcli con up {name}'")
        cmd, args = args[0], args[1:]
        system.launch(path=cmd, args=args)

    def nmcli_connection_down(name: str):
        """Bring a network manager connection down using the cli"""
        actions.user.notify(f"Bringing down VPN {name}")
        args = shlex.split(f"bash -c 'nmcli con down {name}'")
        cmd, args = args[0], args[1:]
        system.launch(path=cmd, args=args)
