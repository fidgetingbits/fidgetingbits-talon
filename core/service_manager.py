from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: terminal
and tag: user.service_manager
"""

mod.tag("service_manager", desc="generic service manager support")
mod.tag("launchctl", desc="darwin service management")
mod.tag("systemd", desc="systemd service management")
mod.tag("upstart", desc="ubuntu upstart service management")

# FIXME: Automatically update service list based on the service manager and use
# the spoken form API
mod.list("service_names", desc="List of services")


@mod.action_class
class Actions:
    def service():
        """Run the default service manager"""

    def service_list(all: bool):
        """List services"""

    def service_find():
        """Find a service"""

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
        """Start a service by name"""

    def service_restart_by_name(name: str):
        """Restart a service by name"""

    def service_enable_by_name(name: str):
        """Enable a service by name"""

    def service_disable_by_name(name: str):
        """Disable a service by name"""

    def service_user():
        """Run the default user service manager"""

    def service_user_list(all: bool):
        """List user services"""

    def service_user_find():
        """Find an user service"""

    def service_user_status():
        """Show the user service status"""

    def service_user_stop():
        """Stop an user service"""

    def service_user_start():
        """Start an user service"""

    def service_user_disable():
        """Disable an user service"""

    def service_user_enable():
        """Enable an user service"""

    def service_user_reload():
        """Reload an user service"""

    def service_user_restart():
        """Restart an user service"""

    def service_user_kill():
        """Kill an user service"""

    def service_user_is_enabled():
        """List if an user service is enabled"""

    def service_user_status_by_name(name: str):
        """List an user service's status by name"""

    def service_user_stop_by_name(name: str):
        """Stop an user service by name"""

    def service_user_start_by_name(name: str):
        """Start an user service by name"""

    def service_user_restart_by_name(name: str):
        """Restart an user service by name"""

    def service_user_enable_by_name(name: str):
        """Enable an user service by name"""

    def service_user_disable_by_name(name: str):
        """Disable an user service by name"""
