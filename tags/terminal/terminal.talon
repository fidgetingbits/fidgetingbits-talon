tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

file list: user.terminal_list_directories()
file list (long | all): user.terminal_list_all_directories()
<user.go>: user.terminal_change_directory("")
clear screen: user.terminal_clear_screen()
run last [command]: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
#kill all: user.terminal_kill_all()

#copy paste:
#    edit.copy()
#    sleep(50ms)
#    edit.paste()
