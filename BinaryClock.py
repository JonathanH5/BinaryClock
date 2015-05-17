import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Use 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

outputChannelList = [5, 6, 12, 13, 16, 19, 20, 21, 26]  

GPIO.setup(chan_list, GPIO.OUT)
GPIO.output(chan_list, GPIO.HIGH) 

time.sleep(5)  

#print("Binary Clock running, shut down with ctrl-c .")

GPIO.cleanup()