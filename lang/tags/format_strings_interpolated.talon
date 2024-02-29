tag: user.code_format_strings_interpolated

# e.g. {:#08x} in python
# will insert_between like "{", ":#08x}"
inner speck [width <number>] {user.code_format_specifiers}:
    user.code_interpolated_format_specifier(code_format_specifiers, number or 0)
