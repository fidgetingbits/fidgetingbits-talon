tag: user.talon
-
tag(): user.code_operators_math
tag(): user.code_operators_assignment
tag(): user.code_comment_line
tag(): user.code_functions_common
# uncomment user.talon_populate_lists tag to activate talon-specific lists of actions, scopes, modes etcetera.
# with conformer, the latency increase may also be unacceptable depending on your cpu
# see https://github.com/knausj85/knausj_talon/issues/600
# tag(): user.talon_populate_lists

user dot:
    "user."
#defintion blocks for the context
action block:
    user.insert_between("action(", "):")
setting block:
    insert("settings():\n\t")
setting {user.talon_settings}:
    user.paste("{talon_settings} = ")
require win:
    insert("os: windows\n")
require mac:
    insert("os: mac\n")
require linux:
    insert("os: linux\n")
require title:
    insert("win.title: ")
require (application | app) [{user.talon_apps}]:
    app = talon_apps or ""
    user.paste("app: {app}")
require mode [{user.talon_modes}]:
    mode = talon_modes or ""
    user.paste("mode: {mode}")
require tag [{user.talon_tags}]:
    tag = talon_tags or ""
    user.paste("tag: {tag}")
#commands for dictating key combos
func key enter:
    "key(enter)"
funk key [<user.modifiers>+] <user.keys>:
    insert("key(")
    insert(modifiers or "")
    insert("{keys}")
    insert(")")
press [<user.modifiers>+] <user.keys>:
    insert(modifiers or "")
    insert("{keys}")
tag set [{user.talon_tags}]:
    tag = talon_tags or ""
    user.paste("tag(): {tag}")
host require:
    hostname = user.talon_get_hostname()
    user.paste("hostname: {hostname}\n")
# requires user.talon_populate_lists tag. do not use with dragon
list {user.talon_lists}:
    "{{{talon_lists}}}"
# requires user.talon_populate_lists tag. do not use with dragon
capture {user.talon_captures}:
    "<{talon_captures}>"

#commands for dictating key combos
key <user.keys> over:
    "{keys}"
key <user.modifiers> over:
    "{modifiers}"

# all actions (requires uncommenting user.talon_populate_lists tag above)
action {user.talon_actions}:
    user.code_insert_function(talon_actions, edit.selected_text())
