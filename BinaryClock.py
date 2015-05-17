import time
import datetime
from threading import Thread

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Use 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

outputChannelList = [5, 6, 12, 13, 16, 19, 20, 21, 24, 25, 26]  

GPIO.setup(outputChannelList, GPIO.OUT)
GPIO.output(outputChannelList, GPIO.HIGH) 

timecontrol = TimeControl()
timecontrol.start()  

print("Binary Clock running, shut down by pressing any key .")
user_input = raw_input("Waiting to shutdown")

GPIO.cleanup()

class TimeControl(Thread):
	
	def run(self):
		while (true)
			now = datetime.datetime.now()
			hour = now.hour
			minute = now.minute
			print("Hour " + hour)
			print("Minute " + minute)
			time.sleep(60)

