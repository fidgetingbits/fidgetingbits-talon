not tag: user.mouse_grid_showing
-
# Decimal
count from <number_small> (to|till|through) <number_small>: user.count_numbers(number_small_1, number_small_2)
numb <user.number_string>: "{number_string}"
# XXX - it would be nice to make dot <user.number_string> repeatable together
# or just used dotted formatter adapted for numbers
#numb <user.number_string> dot <user.number_string>: "{number_string_1}.{number_string_2}"
negative <user.number_string>: "-{number_string}"

# Hexadecimal
# XXX - should handle actual number string, atm cant hex eighty, only hex
# eighth zero
hex <user.hex_letters>$: "0x{hex_letters}"
negative hex <user.hex_letters>: "-0x{hex_letters}"
hex code <user.hex_letters>$: user.escape_hex_string(hex_letters)
hex convert <user.number_string>: user.convert_number_to_hex(number_string)
hex escape <user.number_string>: user.convert_number_to_escaped_hex(number_string)

