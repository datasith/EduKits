"""
  09/01/2015
  Author: Makerbro
  Platforms: Raspberry Pi (Raspbian)
  Language: Python
  File: ultrasonic.py
  ------------------------------------------------------------------------
  Description: 
  Define a simple class for using an HC-SR04 ultrasonic distance sensor.
  ------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We'll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  ------------------------------------------------------------------------
  License:
  Beerware License; if you find the code useful, and we happen to cross 
  paths, you're encouraged to buy us a beer. The code is distributed hoping
  that you in fact find it useful, but  without warranty of any kind.
"""
import RPi.GPIO as GPIO             # Import GPIO library
import time                         # Import time library for sleep delay

# Class that will hold all the functions (methods) that the ultrasonic 
# sensor will need
class Ultrasonic(object):
    def __init__(self, trig_pin=0, echo_pin=0, mode=GPIO.BOARD):
        '''
            Initialize the pins, set them up
        '''
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(mode)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.output(self.trig_pin, GPIO.LOW)
        time.sleep(3)

    def __exit__(self, type, value, traceback):
        GPIO.cleanup(self.trig_pin)
        GPIO.cleanup(self.echo_pin)

    def range_cm(self):
        GPIO.output(self.trig_pin, GPIO.HIGH)
        time.sleep(10/1000/1000)
        cutoff = time.time() + 0.60
        GPIO.output(self.trig_pin, GPIO.LOW)

        pulse_start = 0
        pulse_stop = 0
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            pulse_start = time.time()
            if (pulse_start > cutoff):
                return None
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            pulse_stop = time.time()
            if (pulse_stop > cutoff):
                return None

        # Distance = Time-of-Flight (in one direction) / Inverse of Sound Speed
        distance = (pulse_stop - pulse_start) / 2 * 34000
        distance = round(distance,1)
        if distance >= 400 or distance <= 2:
            return None
        return distance

if __name__ == "__main__":
    try:
        import signal
        import sys
        def signal_handler(signal, frame):
            GPIO.cleanup()
            sys.exit(0)
        signal.signal(signal.SIGINT, signal_handler)

        ultrasonic = Ultrasonic(trig_pin=15,echo_pin=13)

        while True:
            distance = ultrasonic.range_cm()
            if distance:
                print("Distance %s cm" % distance)
            time.sleep(1)
    except KeyboardInterrupt:  
        # here you put any code you want to run before the program   
        # exits when you press CTRL+C  
        print "Quiting..."  
    finally:  
        GPIO.cleanup() # this ensures a clean exit   
