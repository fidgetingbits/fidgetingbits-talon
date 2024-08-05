# This is for editing Cargo.toml files
code.language: toml
title: /Cargo.toml/
-

<user.operator> table ({self.cargo_toml_tables}|<user.text>):
    key("[)
     user.formatted_text(cargo_toml_tables or text, "DASH_SEPARATED")
    insert("]\n")
<user.operator> key ({self.cargo_toml_keys}|<user.text>):
    user.formatted_text(cargo_toml_keys or text, "DASH_SEPARATED")
    " = "
<user.operator> array ({self.cargo_toml_arrays}|<user.text>):
    insert("[[")
    user.formatted_text(cargo_toml_arrays or text, "DASH_SEPARATED")
    insert("]]")
