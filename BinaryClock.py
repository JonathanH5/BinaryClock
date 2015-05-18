####################################################################################################################################
# TODO
####################################################################################################################################

# Refresh Intervall should be set automatically
# create button functionality
# create communication with OpenHab
# create alarm functionality

####################################################################################################################################
# Configuration
####################################################################################################################################

# If true, the gpio ports get changed based on the computed LED configuration, otherwise only the logic part gets executed (good for testing on a device not a raspberry pi.
controlGPIO = True

# Channels: exampleName: ch1 = channelHourOne; cm1 = channelMinuteOne
ch1 = 5
ch2 = 6
ch4 = 13
ch8 = 19
ch16 = 26
cm1 = 24
cm2 = 25
cm4 = 12
cm8 = 16
cm16 = 20
cm32 = 21

# How often should the time get refreshed in seconds?
refresh = 10

####################################################################################################################################
# Imports
####################################################################################################################################

import time
import datetime
from threading import Thread

if controlGPIO == True:
	try:
		import RPi.GPIO as GPIO
	except RuntimeError:
		print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Use 'sudo' to run your script")

####################################################################################################################################
# Global Variables
####################################################################################################################################

keepThreadsAlive = True

####################################################################################################################################
# Classes
####################################################################################################################################

class TimeControl(Thread):
	
	def run(self):
		time.sleep(2) # So that everything else is setup first
		while (keepThreadsAlive):
			now = datetime.datetime.now()
			hour = now.hour
			minute = now.minute
			currentBinaryHour = calculateBinary(hour, 5)
			currentBinaryMinute = calculateBinary(minute, 6)
			print("Time = " + str(hour) + ":" + str(minute) + " Binary = " + currentBinaryHour + ":" + currentBinaryMinute)
			updateGPIOHour(currentBinaryHour)
			updateGPIOMinute(currentBinaryMinute)
			time.sleep(refresh)

####################################################################################################################################
# Methods
####################################################################################################################################

def setUpGPIO():
	if controlGPIO == True:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(ch1, GPIO.OUT)
		GPIO.setup(ch2, GPIO.OUT)
		GPIO.setup(ch4, GPIO.OUT)
		GPIO.setup(ch8, GPIO.OUT)
		GPIO.setup(ch16, GPIO.OUT)
		GPIO.setup(cm1, GPIO.OUT)
		GPIO.setup(cm2, GPIO.OUT)
		GPIO.setup(cm4, GPIO.OUT)
		GPIO.setup(cm8, GPIO.OUT)
		GPIO.setup(cm16, GPIO.OUT)
		GPIO.setup(cm32, GPIO.OUT)
		print("GPIO set up")
	else:
		print("Not using GPIO because controlGPIO is set to False")
		
def calculateBinary(n, wishedLength):
	binary = ""
	if n == 0:
		binary = "0"
	while n > 0:
		binary = str(n % 2) + binary
		n = n >> 1
		
	# correct length
	while len(binary) != wishedLength:
		binary = "0" + binary
				
	return binary
	
def updateGPIOHour(binary):
	if controlGPIO == True:
		chars = list(binary)
		i = 0 # counter
		for c in chars:
			if c == "1":
				if i == 0:
					GPIO.output(ch16, GPIO.HIGH)
				elif i == 1:
					GPIO.output(ch8, GPIO.HIGH)
				elif i == 2:
					GPIO.output(ch4, GPIO.HIGH)
				elif i == 3:
					GPIO.output(ch2, GPIO.HIGH)
				elif i == 4:
					GPIO.output(ch1, GPIO.HIGH)
			elif c == "0":
				if i == 0:
					GPIO.output(ch16, GPIO.LOW)
				elif i == 1:
					GPIO.output(ch8, GPIO.LOW)
				elif i == 2:
					GPIO.output(ch4, GPIO.LOW)
				elif i == 3:
					GPIO.output(ch2, GPIO.LOW)
				elif i == 4:
					GPIO.output(ch1, GPIO.LOW)
			i = i + 1
				
	
def updateGPIOMinute(binary):
	if controlGPIO == True:
		chars = list(binary)
		i = 0 # counter
		for c in chars:
			if c == "1":
				if i == 0:
					GPIO.output(cm32, GPIO.HIGH)
				elif i == 1:
					GPIO.output(cm16, GPIO.HIGH)
				elif i == 2:
					GPIO.output(cm8, GPIO.HIGH)
				elif i == 3:
					GPIO.output(cm4, GPIO.HIGH)
				elif i == 4:
					GPIO.output(cm2, GPIO.HIGH)
				elif i == 5:
					GPIO.output(cm1, GPIO.HIGH)
			elif c == "0":
				if i == 0:
					GPIO.output(cm32, GPIO.LOW)
				elif i == 1:
					GPIO.output(cm16, GPIO.LOW)
				elif i == 2:
					GPIO.output(cm8, GPIO.LOW)
				elif i == 3:
					GPIO.output(cm4, GPIO.LOW)
				elif i == 4:
					GPIO.output(cm2, GPIO.LOW)
				elif i == 5:
					GPIO.output(cm1, GPIO.LOW)
			i = i + 1


####################################################################################################################################
# Code to run
####################################################################################################################################

print("BinaryClock started!")

setUpGPIO()

# start threads

timecontrol = TimeControl()
timecontrol.start()

user_input = raw_input("Shut down by pressing any key!\n\n")

# clean up

keepThreadsAlive = False

if controlGPIO == True:
	GPIO.cleanup()