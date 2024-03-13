import logging
import pathlib
import pprint

from talon import Context, Module, actions

mod = Module()
mod.tag("ssh", desc="tag for ssh functionality")
mod.list("ssh_hosts", desc="List for storing speakable ssh hosts")
mod.list("ssh_keys", desc="List for storing speakable ssh keys")

ctx = Context()
ctx.matches = r"""
tag: user.ssh
"""


# This is slower than using fs.watch in that we have to parse every time, but the benefit is it will pick up
# the case where say someone creates .ssh/config.d/ or .ssh/config if its created after talon starts.
@ctx.dynamic_list("user.ssh_hosts")
def user_ssh_hosts(m) -> dict[str, str]:
    """This is a dynamic list of ssh hosts"""
    ssh_configs = []
    ssh_config = pathlib.Path.home() / ".ssh/config"
    if ssh_config.exists():
        ssh_configs.append(ssh_config)
    ssh_config_dir = pathlib.Path.home() / ".ssh/config.d"
    if ssh_config_dir.exists():
        ssh_configs.extend(ssh_config_dir.glob("*"))
    host_list = []
    for file in ssh_configs:
        with open(file) as f:
            for line in f:
                if line.startswith("Host "):
                    host_list.extend(line.split()[1:])
    return actions.user.create_spoken_forms_from_list(host_list)


@ctx.dynamic_list("user.ssh_keys")
def user_ssh_keys(m) -> dict[str, str]:
    """This is a dynamic list of ssh keys"""
    ssh_keys = []
    ssh_dir = pathlib.Path.home() / ".ssh"
    if ssh_dir.exists():
        ssh_keys.extend([str(key) for key in ssh_dir.glob("*.pub")])
    return actions.user.create_spoken_forms_from_list(ssh_keys)


@mod.action_class
class Actions:
    def ssh_dump_hosts_list():
        """Dump add a pretty version of the file completions to the log"""
        logging.info("SSH Host Completions:")
        logging.info(pprint.pformat(ctx.lists["user.ssh_hosts"]))
