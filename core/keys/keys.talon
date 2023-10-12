go <user.arrow_keys>: user.move_cursor(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
press <user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.all_unmodified_key>: key("{modifiers}-{all_unmodified_key}")
press control alt: key("ctrl-alt")
num pad dash: key("keypad_minus")
num pad plus: key("keypad_plus")

# TODO: Would be nice to have an on-screen indicator of special keys pressed
hold {user.modifier_key}: key("{modifier_key}:down")
release {user.modifier_key}: key("{modifier_key}:up")
release all keys: user.keys_release_all()
