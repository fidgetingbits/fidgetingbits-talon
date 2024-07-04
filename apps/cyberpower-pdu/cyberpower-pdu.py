from talon import Module, actions, settings

mod = Module()
mod.tag("cyberpower-pdu", desc="tag for enabling cyberpower-pdu in your terminal")
mod.list("cyberpower_outlets", desc="List of outlets on a CyberPower PDU")
mod.setting(
    "cyberpower_host",
    type=str,
    default=None,
    desc="The IP address or host name of the CyberPower PDU",
)


@mod.capture(rule="({user.cyberpower_outlets}|<number_small>)")
def cyberpower_outlet(m) -> str:
    """Return a number or specific outlet name"""
    if isinstance(m, int):
        return str(m)
    return m


def run_cyberpower_cmd(args: str, auto=True):
    host = settings.get("user.cyberpower_host")
    if host:
        actions.insert(f"cyberpower-pdu {host} {args}")
        if auto:
            actions.key("enter")


@mod.action_class
class Actions:
    def cyberpower_list():
        """List the outlets on a CyberPower PDU"""
        run_cyberpower_cmd("")

    def cyberpower_outlet_status(outlet: str):
        """Get the status of a CyberPower PDU outlet"""
        run_cyberpower_cmd("{outlet}")

    def cyberpower_outlet_on(outlet: str):
        """Turn on a CyberPower PDU outlet"""
        run_cyberpower_cmd("{outlet} on")

    def cyberpower_outlet_off(outlet: str):
        """Turn off a CyberPower PDU outlet"""
        run_cyberpower_cmd("{outlet} off")

    def cyberpower_outlet_reboot(outlet: str):
        """Reboot a CyberPower PDU outlet"""
        run_cyberpower_cmd("{outlet} reboot")

    def cyberpower_outlet_rename(outlet: str):
        """Rename a CyberPower PDU outlet"""
        run_cyberpower_cmd(f"{outlet} rename ", auto=False)
