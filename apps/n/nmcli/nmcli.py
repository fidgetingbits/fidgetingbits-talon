import os
import subprocess
import shlex

from talon import Context, Module, actions, system, imgui, registry

mod = Module()
ctx = Context()

ctx.matches = """
os: linux
"""

mod.list("nmcli_vpns", desc="Configure network manager vpn connections")
mod.tag(
    "nmcli_vpns_gui_active",
    desc="Active when the vpn picker GUI is showing",
)


def get_vpn_list():
    output = subprocess.check_output(
        ("bash", "-c", "nmcli -t -f NAME,TYPE connection show | rg vpn | cut -f1 -d:"),
        text=True,
    )
    if not output:
        return None
    return output.splitlines()


@imgui.open()
def gui_vpns(gui: imgui.GUI):
    gui.text("NetworkManager VPNs")
    gui.line()

    vpn_list = get_vpn_list()
    if not vpn_list:
        gui.text("No VPNs found")
    else:
        for vpn in vpn_list:
            gui.text(vpn)

    gui.spacer()
    if gui.button("V P N hide (close window)"):
        actions.user.nmcli_connection_toggle_list()


@ctx.dynamic_list("user.nmcli_vpns")
def user_nmcli_vpns(m) -> dict[str, str]:
    """A dynamic list of VPN connections"""
    vpn_list = get_vpn_list()
    if not vpn_list:
        return {}

    return actions.user.create_spoken_forms_from_list(vpn_list)


@mod.action_class
class NetworkManagerClientActions:
    def nmcli_connection_toggle(name: str):
        """Toggle a network manager connection up/down using the cli"""
        # Check if the connection is up or down
        output = subprocess.check_output(
            (
                "bash",
                "-c",
                f"nmcli -t -f NAME,STATE connection show | rg {name } | cut -f2 -d:",
            ),
            text=True,
        )
        if not output:
            actions.user.notify(f"VPN {name} not found")
            return
        if "activated" in output:
            actions.user.nmcli_connection_down(name)
        else:
            actions.user.nmcli_connection_up(name)

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

    def nmcli_connection_toggle_list():
        """Display the detected VPN connections"""
        if gui_vpns.showing:
            gui_vpns.hide()
            ctx.tags = []
        else:
            gui_vpns.show()
            ctx.tags = ["user.nmcli_vpns_gui_active"]
