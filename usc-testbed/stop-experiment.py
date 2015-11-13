import subprocess
import datetime
import time



end = datetime.time(20, 8, 0)

while True:
	now = datetime.datetime.now().time()
	
	if(now.hour == end.hour and now.minute >= end.minute):
		subprocess.call(["pkill", "socat"])
		subprocess.call(["pkill", "python serial_aggregator.py"])
		break

	time.sleep(10)

