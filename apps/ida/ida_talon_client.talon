app: ida
and tag: user.command_client
-

copy address:
    user.ida_copy_address_cursor()

make ({user.data_widths}|last):
    user.ida_modify_raw_datatype(data_widths or "last")

