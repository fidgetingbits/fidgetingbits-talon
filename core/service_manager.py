from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
os: linux
tag: terminal
and tag: user.service_manager
"""

mod.tag("service_manager", desc="generic service manager support")
mod.tag("systemd", desc="systemd service management")
mod.tag("upstart", desc="ubuntu upstart service management")


@mod.action_class
class Actions:
    def service():
        """Run the default service manager"""

    def service_status():
        """Show the service status"""

    def service_stop():
        """Stop a service"""

    def service_start():
        """Start a service"""

    def service_disable():
        """Disable a service"""

    def service_enable():
        """Enable a service"""

    def service_reload():
        """Reload a service"""

    def service_restart():
        """Restart a service"""

    def service_help():
        """Service manager help"""

    def service_kill():
        """Kill a service"""

    def service_is_enabled():
        """List if a service is enabled"""

    def service_status_by_name(name: str):
        """List a services status by name"""

    def service_stop_by_name(name: str):
        """Stop a service by name"""

    def service_start_by_name(name: str):
        """Start to service by name"""

    def service_restart_by_name(name: str):
        """Start to service by name"""

    def service_enable_by_name(name: str):
        """Enable a service by name"""

    def service_disable_by_name(name: str):
        """Disable a service by name"""
