# XXX - detect were actually specifically in something with a task before
tag: user.vim_taskwiki
and tag: user.markdown
-

task (annotate | meta): user.vim_command_mode(":TaskWikiAnnotate\n")
task burn [down] daily: user.vim_command_mode(":TaskWikiBurndownDaily\n")
task burn [down] weekly: user.vim_command_mode(":TaskWikiBurndownWeekly\n")
task burn [down] monthly: user.vim_command_mode(":TaskWikiBurndownMonthly\n")

# Interactive
task choose project: user.vim_command_mode(":TaskWikiChooseProject\n")
task choose tag: user.vim_command_mode(":TaskWikiChooseTag\n")

task calendar: user.vim_command_mode(":TaskWikiCalendar\n")
task done: user.vim_command_mode(":TaskWikiDone\n")
task delete: user.vim_command_mode(":TaskWikiDelete\n")
task edit: user.vim_command_mode(":TaskWikiEdit\n")
task grid: user.vim_command_mode(":TaskWikiGrid\n")
task grid monthly: user.vim_command_mode(":TaskWikiGhistoryMonthly\n")
task great yearly: user.vim_command_mode(":TaskWikiGhistoryAnnual\n")
task history: user.vim_command_mode(":TaskWikiHistoryMonthly\n")
task history yearly: user.vim_command_mode(":TaskWikiHistoryAnnual\n")
task info: user.vim_command_mode(":TaskWikiInfo\n")
task link: user.vim_command_mode(":TaskWikiLink\n")
task mod: user.vim_command_mode(":TaskWikiMod\n")
task projects: user.vim_command_mode(":TaskWikiProjects\n")
task summary: user.vim_command_mode(":TaskWikiProjectsSummary\n")
task stats: user.vim_command_mode(":TaskWikiStats")
task stats all: user.vim_command_mode(":TaskWikiStats global\n")
task tags: user.vim_command_mode(":TaskWikiTags\n")
task start: user.vim_command_mode(":TaskWikiStart\n")
task stop: user.vim_command_mode(":TaskWikiStop\n")

task (refresh | reload): user.vim_command_mode(":TaskWikiBufferLoad\n")
task save: user.vim_command_mode(":TaskWikiBufferSave\n")
task inspect: user.vim_command_mode(":TaskWikiInspect\n")

# This is for undelete
task mark pending:
    user.vim_command_mode(":TaskWikiMod\n")
    insert("status:pending\n")
