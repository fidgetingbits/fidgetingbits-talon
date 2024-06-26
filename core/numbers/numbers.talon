tag: user.prefixed_numbers
-
# Decimal
count from <number_small> (to | till | through) <number_small>:
    user.count_numbers(number_small_1, number_small_2)
numb <user.number_string>: "{number_string}"
no mate [<user.number_string>]: user.insert_formatted("8{number_string or ''}", "NOOP")

# XXX - it would be nice to make dot <user.number_string> repeatable together
# or just used dotted formatter adapted for numbers

# Useful version numbering commands
# 7.0
numb <user.number_string> (point | dot) <user.number_string>:
    "{number_string_1}.{number_string_2}"
numb <user.number_string> (point | dot) X: "{number_string}.x"
numb <user.number_string> (point | dot) X [(point | dot)] Y: "{number_string}.x.y"

# 7.0-7
numb <user.number_string> (point | dot) <user.number_string> dash <user.number_string>:
    "{number_string_1}.{number_string_2}-{number_string_3}"
# 7.0.0
numb <user.number_string> (point | dot) <user.number_string> (point | dot) <user.number_string>:
    "{number_string_1}.{number_string_2}.{number_string_3}"
# 7.0.0-7
numb <user.number_string> (point | dot) <user.number_string> (point | dot) <user.number_string> dash <user.number_string>:
    "{number_string_1}.{number_string_2}.{number_string_3}-{number_string_4}"
# 2-4
numb <user.number_string> dash <user.number_string>:
    "{number_string_1}-{number_string_2}"
# 2-4-6
numb <user.number_string> dash <user.number_string> dash <user.number_string>:
    "{number_string_1}-{number_string_2}-{number_string_3}"

# space separated numbers
numb <user.number_string> and <user.number_string>:
    "{number_string_1} {number_string_2}"
numb <user.number_string> and <user.number_string> and <user.number_string>:
    "{number_string_1} {number_string_2} {number_string_3}"
numb <user.number_string> and <user.number_string> and <user.number_string> and <user.number_string>:
    "{number_string_1} {number_string_2} {number_string_3} {number_string_4}"

(point | dot) <user.number_string>: ".{number_string}"

negative <user.number_string>: "-{number_string}"
numb page size: "4096"

# Hexadecimal
# XXX - should handle actual number string, atm cant hex eighty, only hex
# eighth zero
hex <user.number_string>: "0x{number_string}"
hex numb <user.hex_letters>$: "0x{hex_letters}"
negative hex <user.hex_letters>: "-0x{hex_letters}"
# "hex short four one" produces 0x4141
hex short <user.hex_letters>: user.expand_to_int16_hex(hex_letters)
# "hex int four one" produces 0x41414141
hex int <user.hex_letters>: user.expand_to_int32_hex(hex_letters)
# "hex long four one" produces 0x4141414141414141
hex long <user.hex_letters>: user.expand_to_int64_hex(hex_letters)

hex delimited short <user.hex_letters>: user.expand_to_delimited_int16_hex(hex_letters)
hex delimited int <user.hex_letters>: user.expand_to_delimited_int32_hex(hex_letters)
hex delimited long <user.hex_letters>: user.expand_to_delimited_int64_hex(hex_letters)


hex code <user.hex_letters>$: user.escape_hex_string(hex_letters)
hex convert <user.number_string>: user.convert_number_to_hex(number_string)
(hex dump pointer | paste as pointer): user.convert_hex_dump_pointer()
hex escape <user.number_string>: user.convert_number_to_escaped_hex(number_string)
(paste | clip) as hex: user.paste_clipboard_as_hex()
(paste | clip) as deck: user.paste_clipboard_as_dec()
