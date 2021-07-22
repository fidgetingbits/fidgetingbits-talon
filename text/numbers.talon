not tag: user.mouse_grid_showing
-
count from <number_small> (to|till|through) <number_small>: user.count_numbers(number_small_1, number_small_2)
numb <user.number_string>: "{number_string}"
# XXX - it would be nice to make dot <user.number_string> repeatable together
# or just used dotted formatter adapted for numbers
numb <user.number_string> dot <user.number_string>: "{number_string_1}.{number_string_2}"
negative <user.number_string>: "-{number_string}"
# XXX - should handle more complex hexadecimal number invocations
(hex|hexadecimal) [(num|number)] <user.number_string>: "0x{number_string}"
hex string <user.hex_letters>: user.escape_hex_string(hex_letters)
