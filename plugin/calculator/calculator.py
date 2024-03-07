from itertools import chain

from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.list("calculator_operators", "Basic calculator operators like add, sub, etc")

ctx.lists["user.calculator_operators"] = {
    "add": "add",
    "sub": "sub",
    "times": "multiply",
    "div": "divide",
}


@mod.action_class
class Actions:
    def calculator_compute(operator: str, text: str):
        """Calculate some text using the specified operators"""
        use_hex = False
        if "0x" in text:
            use_hex = True
        # 1\n2\n3 becomes ["1", "2", "3"]
        operands = text.split("\n")
        # ["1 2 3", "4"] becomes ["1", "2", "3", "4"]
        operands = list(chain(*[i.split() for i in operands]))
        operands = [int(i, 0) for i in operands]
        match operator:
            case "add":
                result = sum(operands)
            case "sub":
                result = operands[0] - sum(operands[1:])
            case "multiply":
                result = 1
                for i in operands:
                    result *= i
            case "divide":
                result = operands[0]
                for i in operands[1:]:
                    result /= i
        if use_hex:
            # int() because it could be a float from division
            result = hex(int(result))
        actions.insert(f"{result}")
