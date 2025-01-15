import subprocess

from talon import Context, Module, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
user.talon_branch: beta
tag: user.just_commands
"""

mod.list("justfile_commands", desc="Just commands from the justfile")


@ctx.dynamic_list("user.justfile_commands")
def user_justfile_commands(m) -> dict[str, str]:
    """A dynamic list of available just commands"""
    ps = subprocess.Popen(
        ("just", "--list"), stdout=subprocess.PIPE, cwd=actions.user.get_cwd()
    )
    output = subprocess.check_output(
        ("grep", "-v", "'(Available recipes|Error:)'"), stdin=ps.stdout
    ).decode("utf-8")
    ps.wait()
    if not output:
        print("no output")
        return {}

    commands = []
    for line in output.splitlines():
        if "#" in line:
            line = line.split("#")[0]
        # Some commands may take arguments, but we don't want those pasted. The assumption if you're speaking one of
        # those, is that the options will use defaults you don't need to dictate.

        commands.append(line.strip().split()[0])
    return actions.user.create_spoken_forms_from_list(commands)
