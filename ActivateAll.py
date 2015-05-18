from threading import Thread
import time

if controlGPIO == True:
	try:
		import RPi.GPIO as GPIO
	except RuntimeError:
		print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Use 'sudo' to run your script")

clist = [5, 6, 13, 19, 26, 24, 25, 12, 16, 20, 21]
		
GPIO.setmode(GPIO.BCM)	
GPIO.setup(clist, GPIO.OUT)
GPIO.output(clist, GPIO.HIGH)

time.sleep(3)
GPIO.cleanup()