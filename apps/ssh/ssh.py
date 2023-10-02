import logging
import pathlib
import pprint

from talon import Context, Module, actions, app, fs

mod = Module()
mod.tag("ssh", desc="tag for ssh functionality")
mod.list("ssh_hosts", desc="List for storing speakable ssh hosts")

ctx = Context()
ctx.matches = r"""
tag: user.ssh
"""
ctx.lists["user.ssh_hosts"] = {}


def on_ready():
    """Trigger one list update soon is talon is ready"""
    ssh_config_change(None, None)


def ssh_config_change(path, flags):
    """Update the ssh host list based off of a change of ssh config"""
    host_list = []
    global ssh_configs
    for file in ssh_configs:
        with open(file) as f:
            for line in f:
                if line.startswith("Host "):
                    host_list.extend(line.split()[1:])
    ctx.lists["user.ssh_hosts"] = actions.user.create_spoken_forms_from_list(host_list)


ssh_configs = []
ssh_config = pathlib.Path.home() / ".ssh/config"
if ssh_config.exists():
    ssh_configs.append(ssh_config)
    fs.watch(ssh_config, ssh_config_change)
ssh_config_dir = pathlib.Path.home() / ".ssh/config.d"
if ssh_config_dir.exists():
    ssh_configs.extend(ssh_config_dir.glob("*"))
    for path in ssh_config_dir.glob("*"):
        fs.watch(path, ssh_config_change)
# print(f"SSH Configs: {ssh_configs}")
app.register("ready", on_ready)


@mod.action_class
class Actions:
    def ssh_dump_hosts_list():
        """Dump add a pretty version of the file completions to the log"""
        logging.info("SSH Host Completions:")
        logging.info(pprint.pformat(ctx.lists["user.ssh_hosts"]))
