tag: user.code_imperative
-

put block: user.code_block()
(state | put) if: user.code_state_if()
(state | put) else if: user.code_state_else_if()
(state | put) else: user.code_state_else()
(state | put) while: user.code_state_while()
(state | put) loop: user.code_state_infinite_loop()
(state | put) for: user.code_state_for()
(state | put) for in: user.code_state_for_each()
(state | put) switch: user.code_state_switch()
(state | put) case: user.code_state_case()
(state | put) do: user.code_state_do()
(state | put) goto: user.code_state_go_to()
(state | put) return: user.code_state_return()
(state | put) break: user.code_break()
(state | put) (continue|next): user.code_next()
(state | put) try catch: user.code_try_catch()

