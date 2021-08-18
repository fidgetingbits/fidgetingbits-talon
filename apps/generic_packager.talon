os: linux
tag: terminal
and tag: user.package_manager
-
# assert your system packager here
tag(): user.packager_yay

packager: user.packager()
package search: user.package_search()
package install: user.package_install()
package remove: user.package_remove()
package update: user.package_update()
package update all: user.package_update_all()
package upgrade system: user.package_upgrade_system()
package list: user.package_list()
package help: user.package_help()
# XXX - add an automatic gui based packager switcher
