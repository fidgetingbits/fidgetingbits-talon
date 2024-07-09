# Expose a number of common commands for printing out dates in various formats
# TODO - add some unix epoch, microsoft
-
date time: insert(user.date_now())
date today: insert(user.date_today())
date yesterday: insert(user.date_yesterday())
date tomorrow: insert(user.date_tomorrow())
