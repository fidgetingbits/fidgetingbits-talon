tag: user.packager_yum
-

(yum | package) downgrade: "yum downgrade "
(yum | package) fuzzy downgrade: user.insert_between("yum downgrade ", "\\*")
(yum | package) source [download]: "yumdownloader --source "
# Shows every historical version of a given package
yum list all version: user.insert_between("yum list", " --showduplicates")
