tag: user.cursorless
-

# Example usage:
#  0x7fffd000 0x2000 0x100
# swan add three tokens <user.cursorless_target>:
# 0x7ffff100

# swan because 算 is is pronounced the same, and means calculate in Mandarin
swan {user.calculator_operators} <user.cursorless_target>:
    user.cursorless_command("copyToClipboard", cursorless_target)
    user.calculator_compute(calculator_operators, clip.text())
