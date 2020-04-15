import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, True)
time.sleep(2)
GPIO.output(8, False)
time.sleep(2)

GPIO.cleanup() # this ensures a clean exit  
