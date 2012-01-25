# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:31:43 2012

@author: francisco
"""


import os
import datetime
import sys

#Fast track
sys.exit(0)


file_timestamp = os.path.getmtime("/tmp/aquaniebla.watchdog")
file_date = datetime.datetime.fromtimestamp(file_timestamp)
five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes = 6) 
print str(file_date) + "  ... " + str(five_minutes_ago)
if file_date < five_minutes_ago:
    print "older"     
    sys.exit(1)
else:
    print "newer"
    sys.exit(0)
