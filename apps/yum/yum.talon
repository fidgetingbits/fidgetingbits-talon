tag: user.packager_yum
-

(yum | package) downgrade: "yum downgrade "
(yum | package) fuzzy downgrade: user.insert_between("yum downgrade ", "\\*")
(yum | package) source [download]: "yumdownloader --source "
