#!/bin/bash

echo "Watchdog has ran" >> /var/log/acuaniebla/watchdog.log

python /acuaniebla/watchdog.py >> /var/log/acuaniebla/watchdog.log
RETVAL=$?

[ $RETVAL -eq 0 ] && echo "Everything is under control"
[ $RETVAL -ne 0 ] && echo "This is chaos! Run for your life"


if [ $RETVAL -ne 0 ]; then
	echo $RETVAL >> /var/log/acuaniebla/watchdog.log
	echo "Ok... is not THAT terrible but we need to reboot it anyways"
	echo "Dropping MOAA..." >> /var/log/acuaniebla/watchdog.log
	killall -9 python
	echo "...What have we done?"
	echo "Restarting..."
	sudo shutdown -r now
fi


