app: terminal
tag: user.timer_manager
-

[system] timer: user.timer()
[system] timer list: user.timer_list()
[system] timer list all: user.timer_list_all()
[system] timer log: user.timer_log()
[system] timer restart: user.timer_restart()
[system] timer reload: user.timer_reload()
[system] timer stop: user.timer_stop()
[system] timer start: user.timer_start()
[system] timer status: user.timer_status()
[system] timer enable: user.timer_enable()
[system] timer disable: user.timer_disable()
[system] timer help: user.timer_help()
[system] timer kill: user.timer_kill()
[system] timer is enabled: user.timer_is_enabled()

# timer's specific to user vs system-wide
user timer: user.timer()
user timer list: user.timer_user_list()
user timer list all: user.timer_user_list_all()
user timer restart: user.timer_user_restart()
user timer reload: user.timer_user_reload()
user timer stop: user.timer_user_stop()
user timer start: user.timer_user_start()
user timer status: user.timer_user_status()
user timer enable: user.timer_user_enable()
user timer disable: user.timer_user_disable()
user timer help: user.timer_user_help()
user timer kill: user.timer_user_kill()
user timer is enabled: user.timer_user_is_enabled()
