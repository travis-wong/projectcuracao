



"""
testModule.py
JCS 9/10/2013 Version 1.0

This program runs the data collection, graph preperation, housekeeping and actions
"""

# shelves:
# 	datacollect - sensor data collection - disabled to RAM
#	graphprep - building system graphs
#	housekeeping - fan check , general health and wellfare
# 	alarmchecks - checks for system health alarms 
#	actions - specific actions scheduled (i.e. camera picture)
 
from datetime import datetime, timedelta
import sys
import time

from apscheduler.scheduler import Scheduler
from apscheduler.jobstores.shelve_store import ShelveJobStore



sys.path.append('./datacollect')
sys.path.append('./graphprep')
sys.path.append('./hardware')
sys.path.append('./housekeeping')

#import powersupplygraph 
import solarwindgraph 



#powersupplygraph.powersystemsupplygraph("test",5)
while (1):
	solarwindgraph.solarwindgraph("test",5,1)
	time.sleep(600)



