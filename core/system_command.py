import os
import subprocess

from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def bash_command_quiet(cmd: str):
        """execute a command on the system using bash

        This is useful if the command your executing is noisy,
        like the i3-msg commands
        """
        os.system('bash -c "' + cmd + '" > /dev/null 2>&1')

    def system_command(cmd: str):
        """execute a command on the system"""
        os.system(cmd)

    def system_command_nb(cmd: str):
        """execute a command on the system without blocking"""
        subprocess.Popen(cmd, shell=True)

    def system_command_output(cmd: str):
        """execute a command on the system and return it's output"""

        output = subprocess.check_output(cmd.split(" "), shell=True)
        actions.insert(output.decode("utf-8"))
