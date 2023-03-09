app: ida
and tag: user.command_client
-

copy [cursor] address:
    user.ida_copy_address_cursor()

copy funk address:
    user.ida_copy_address_function()

copy base address:
    user.ida_copy_address_base()

copy [cursor] offset:
    user.ida_copy_relative_offset_cursor()

copy funk offset:
    user.ida_copy_relative_offset_function()

copy [cursor] label:
    user.ida_copy_label_cursor()

copy [cursor] demangled [(name | label)]:
    user.ida_copy_demangled_label_cursor()

copy [cursor] funk [(name | label)]:
    user.ida_copy_label_function()

copy [cursor] demangled funk [(name | label)]:
    user.ida_copy_demangled_label_function()

make ({user.data_widths} | last):
    user.ida_modify_raw_datatype(data_widths or "last")

# rename
