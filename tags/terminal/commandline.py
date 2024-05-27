import subprocess

from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: terminal
"""

mod.list("executable_files", desc="Executable script files")
mod.list(
    "runtime_environment_variables",
    desc="Environment variables in the underlying shell",
)


@ctx.dynamic_list("user.runtime_environment_variables")
def user_runtime_environment_variables(m) -> dict[str, str]:
    """A dynamic list of environment variables in this shell

    NOTE: This won't apply to variables that are unique to that specific session
    because we can't enter the same shell
    """

    try:
        output = subprocess.check_output(
            ("env",),
            cwd=actions.user.zsh_get_cwd(),
        ).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.output)
    if not output:
        print("no output")
        return {}
    # We only care about the variable names
    output = [line.split("=")[0] for line in output.splitlines()]
    # print(len(output))
    return actions.user.create_spoken_forms_from_list(output)


@ctx.dynamic_list("user.executable_files")
def executable_files(m) -> dict[str, str]:
    """A dynamic list of executable script files in the current folder"""

    try:
        output = subprocess.check_output(
            (
                "find",
                ".",
                "-maxdepth",
                "1",
                "-type",
                "f",
                "-executable",
                "-printf",
                "%P\n",
            ),
            cwd=actions.user.zsh_get_cwd(),
        ).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(e.output)
    if not output:
        print("no output")
        return {}
    print(output)
    return actions.user.create_spoken_forms_from_list(output.splitlines())
