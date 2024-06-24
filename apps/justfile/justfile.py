import subprocess

from talon import Context, Module, actions

mod = Module()
mod.setting(
    "justfile_auto_completion",
    type=bool,
    default=False,
    desc="Whether or not to automatically complete just commands with justfile contents",
)

ctx = Context()
ctx.matches = r"""
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
        commands.append(line.strip())
    return actions.user.create_spoken_forms_from_list(commands)
