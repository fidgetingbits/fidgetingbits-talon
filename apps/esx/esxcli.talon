app: terminal
tag: user.esxcli
-

E S X get maintenance mode: "esxcli system maintenanceMode get\n"
E S X set maintenance true: "esxcli system maintenanceMode set --enable true"
E S X set maintenance false: "esxcli system maintenanceMode set --enable false"
E S X update depot: "esxcli software profile update --depot=<depot_location> --profile=<profile_name>"
E S X profile list: "esxcli software sources profile list\n"
E S X process list: "esxcli vm process list\n"
E S X process kill: "esxcli vm process kill --type=soft --world-id="

E S X get V M list: "vim-cmd vmsvc/getallvms\n"
E S X V M power on: "vim-cmd vmsvc/power.on "
