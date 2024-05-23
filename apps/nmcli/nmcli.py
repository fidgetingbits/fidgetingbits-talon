import os
import subprocess

from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
tag: terminal
and tag: user.nmcli
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
