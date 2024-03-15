tag: user.package_manager
-

pack man reset: user.package_manager_reset()
pack man set {user.package_managers}: user.package_manager_set(package_managers)
pack man show: user.package_manager_show()


packager: user.packager()
package search: user.package_search()
package install: user.package_install()
package remove: user.package_remove()
package update [<user.text>]: user.package_update(text or "")
package update all: user.package_update_all()
package upgrade system: user.package_upgrade_system()
package list: user.package_list()
package dependencies: user.package_dependencies()
package list contents: user.package_list_contents()
package help: user.package_help()
# XXX - add an automatic gui based packager switcher
