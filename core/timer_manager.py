from talon import Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
os: linux
tag: user.timer_manager
"""

# systemd is already in service_manager
# mod.tag("systemd", desc="systemd management")
mod.tag("timer_manager", desc="generic timer manager support")
mod.tag("cron", desc="non-systemd timer timer")


@mod.action_class
class Actions:
    # System-wide timer control
    def timer():
        """Run the default timer manager"""

    def timer_status():
        """Show the timer status"""

    def timer_stop():
        """Stop a timer"""

    def timer_start():
        """Start a timer"""

    def timer_disable():
        """Disable a timer"""

    def timer_enable():
        """Enable a timer"""

    def timer_reload():
        """Reload a timer"""

    def timer_restart():
        """Restart a timer"""

    def timer_help():
        """Service manager help"""

    def timer_kill():
        """Kill a timer"""

    def timer_is_enabled():
        """List if a timer is enabled"""

    def timer_status_by_name(name: str):
        """List a timers status by name"""

    def timer_stop_by_name(name: str):
        """Stop a timer by name"""

    def timer_start_by_name(name: str):
        """Start to timer by name"""

    def timer_enable_by_name(name: str):
        """Enable a timer by name"""

    def timer_disable_by_name(name: str):
        """Disable a timer by name"""

    # User timers vs system-wide timers
    def timer_user():
        """Run the default timer manager"""

    def timer_user_status():
        """Show the timer status"""

    def timer_user_stop():
        """Stop a timer"""

    def timer_user_start():
        """Start a timer"""

    def timer_user_disable():
        """Disable a timer"""

    def timer_user_enable():
        """Enable a timer"""

    def timer_user_reload():
        """Reload a timer"""

    def timer_user_restart():
        """Restart a timer"""

    def timer_user_help():
        """Service manager help"""

    def timer_user_kill():
        """Kill a timer"""

    def timer_user_is_enabled():
        """List if a timer is enabled"""

    def timer_user_status_by_name(name: str):
        """List a timers status by name"""

    def timer_user_stop_by_name(name: str):
        """Stop a timer by name"""

    def timer_user_start_by_name(name: str):
        """Start to timer by name"""

    def timer_user_enable_by_name(name: str):
        """Enable a timer by name"""

    def timer_user_disable_by_name(name: str):
        """Disable a timer by name"""
