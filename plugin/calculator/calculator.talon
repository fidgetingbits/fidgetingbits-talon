tag: user.cursorless
-

# FIXME: Make it work for numbered clipboard entries as well

# Example usage:
#  0x7fffd000 0x2000 0x100
# swan add three tokens <user.cursorless_target>:
# 0x7ffff100

# swan because 算
swan {user.calculator_operators} <user.cursorless_target>:
    user.cursorless_command("copyToClipboard", cursorless_target)
    user.calculator_compute(calculator_operators, clip.text())
