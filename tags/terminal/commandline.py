import subprocess

from talon import Context, Module, actions

mod = Module()
ctx = Context()

ctx.matches = """
tag: terminal
"""

mod.list("executable_files", desc="Executable script files")


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
