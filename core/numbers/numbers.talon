not tag: user.mouse_grid_showing
-
# Decimal
count from <number_small> (to | till | through) <number_small>:
    user.count_numbers(number_small_1, number_small_2)
numb <user.number_string>: "{number_string}"
no mate [<user.number_string>]:
    user.insert_formatted("8{number_string or ''}", "NOOP")
# XXX - it would be nice to make dot <user.number_string> repeatable together
# or just used dotted formatter adapted for numbers
numb <user.number_string> dot <user.number_string>:
    "{number_string_1}.{number_string_2}"
negative <user.number_string>: "-{number_string}"
numb page size: "4096"

# Hexadecimal
# XXX - should handle actual number string, atm cant hex eighty, only hex
# eighth zero
hex numb <user.hex_letters>$: "0x{hex_letters}"
negative hex <user.hex_letters>: "-0x{hex_letters}"
# "hex short four one" produces 0x4141
hex short <user.hex_letters>: user.expand_to_int16_hex(hex_letters)
# "hex int four one" produces 0x41414141
hex int <user.hex_letters>: user.expand_to_int32_hex(hex_letters)
# "hex long four one" produces 0x4141414141414141
hex long <user.hex_letters>: user.expand_to_int64_hex(hex_letters)
hex code <user.hex_letters>$: user.escape_hex_string(hex_letters)
hex convert <user.number_string>: user.convert_number_to_hex(number_string)
(hex dump pointer | paste as pointer): user.convert_hex_dump_pointer()
hex escape <user.number_string>:
    user.convert_number_to_escaped_hex(number_string)
(paste | clip) as hex: user.paste_clipboard_as_hex()
(paste | clip) as deck: user.paste_clipboard_as_dec()
