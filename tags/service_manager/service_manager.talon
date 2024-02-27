tag: terminal
and tag: user.service_manager
-

# service: user.service()
service name {user.service_names}: "{service_names}"
service list: user.service_list()
service find: user.service_find()
service restart: user.service_restart()
service restart {user.service_names}: user.service_restart_by_name(service_names)
service reload: user.service_reload()
service stop: user.service_stop()
service stop {user.service_names}: user.service_stop_by_name(service_names)
service start: user.service_start()
service start {user.service_names}: user.service_start_by_name(service_names)
service enable: user.service_enable()
service enable {user.service_names}: user.service_enable_by_name(service_names)
service disable: user.service_disable()
service disable {user.service_names}: user.service_disable_by_name(service_names)
service status: user.service_status()
service status {user.service_names}: user.service_status_by_name(service_names)
service help: user.service_help()
service kill: user.service_kill()
service kill {user.service_names}: user.service_kill_by_name(service_names)
service is enabled: user.service_is_enabled()
