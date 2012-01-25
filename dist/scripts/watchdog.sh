#!/bin/bash

echo "Watchdog has ran" >> /acquaniebla/log/watchdog.log

python /acquaniebla/watchdog/watchdog.py >> /acquaniebla/log/watchdog.log
RETVAL=$?

[ $RETVAL -eq 0 ] && echo "Everything is under control"
[ $RETVAL -ne 0 ] && echo "This is chaos! Run for your life"


if [ $RETVAL -ne 0 ]; then
	echo $RETVAL >> /acquaniebla/log/watchdog.log
	echo "Ok... is not THAT terrible but we need to reboot it anyways"
	echo "Dropping MOAA..." >>/acquaniebla/log/watchdog.log
	killall -9 python
	echo "...What have we done?"
	echo "Restarting..."
	sudo shutdown -r now
fi


