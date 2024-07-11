app: terminal
tag: user.service_manager
-

# service: user.service()
service name {user.service_all_system_services}: "{service_all_system_services}"
service list: user.service_list(false)
service list all: user.service_list(true)
service list active: user.service_list_active()
service list inactive: user.service_list_inactive()
service list running: user.service_list_running()
service last (exited|stopped): user.service_last_exited()
service find: user.service_find()
service restart: user.service_restart()
service restart {user.service_all_system_services}: user.service_restart_by_name(service_all_system_services)
service reload: user.service_reload()
service stop: user.service_stop()
service stop {user.service_active_system_services}: user.service_stop_by_name(service_active_system_services)
service start: user.service_start()
service start {user.service_inactive_system_services}: user.service_start_by_name(service_inactive_system_services)
service enable: user.service_enable()
service enable {user.service_all_system_services}: user.service_enable_by_name(service_all_system_services)
service disable: user.service_disable()
service disable {user.service_all_system_services}: user.service_disable_by_name(service_all_system_services)
service status: user.service_status()
service status {user.service_all_system_services}: user.service_status_by_name(service_all_system_services)
service help: user.service_help()
service kill: user.service_kill()
service kill {user.service_active_system_services}: user.service_kill_by_name(serviceactive_system_services)
service is enabled: user.service_is_enabled()

service user name {user.service_all_user_services}: "{service_all_user_services}"
service user list: user.service_user_list(false)
service user list all: user.service_user_list(true)
service user list active: user.service_user_list_active()
service user list inactive: user.service_user_list_inactive()
service user list running: user.service_user_list_running()
service user last (exited|stopped): user.service_user_last_exited()
service user find: user.service_user_find()
service user restart: user.service_user_restart()
service user restart {user.service_all_user_services}: user.service_user_restart_by_name(service_all_user_services)
service user reload: user.service_user_reload()
service user stop: user.service_user_stop()
service user stop {user.service_active_user_services}: user.service_user_stop_by_name(service_active_user_services)
service user start: user.service_user_start()
service user start {user.service_inactive_user_services}: user.service_user_start_by_name(service_inactive_user_services)
service user enable: user.service_user_enable()
service user enable {user.service_all_user_services}: user.service_user_enable_by_name(service_all_user_services)
service user disable: user.service_user_disable()
service user disable {user.service_all_user_services}: user.service_user_disable_by_name(service_all_user_services)
service user status: user.service_user_status()
service user status {user.service_all_user_services}: user.service_user_status_by_name(service_all_user_services)
# FIXME: Do we need this?
# service user help: user.service_user_help()
service user kill: user.service_user_kill()
service user kill {user.service_active_user_services}: user.service_user_kill_by_name(service_active_user_services)
service user is enabled: user.service_user_is_enabled()
