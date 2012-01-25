# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:31:43 2012

@author: francisco
"""


import os
import datetime
import sys

if os.path.isfile("/acquaniebla/watchdog/.lock"):
     print "Lock file exists"
     sys.exit(0)

five_minutes = 5

file_timestamp = os.path.getmtime("/acquaniebla/log/acquaniebla.watchdog")
file_date = datetime.datetime.fromtimestamp(file_timestamp)
five_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes = five_minutes) 
print str(file_date) + "  ... " + str(five_minutes_ago)
if file_date < five_minutes_ago:
    print "older"     
    sys.exit(1)
else:
    print "newer"
    sys.exit(0)
