import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# Initialize PWM on pin 12 at 1KHz
pwm_obj = GPIO.PWM(12, 1000)

# Start PWM with duty cycle of 0
pwm_obj.start(0)
time.sleep(1)
# Change PWM to a 25% duty cycle
pwm_obj.ChangeDutyCycle(25)
time.sleep(1)
# Change PWM to a 50% duty cycle
pwm_obj.ChangeDutyCycle(50)
time.sleep(1)
# Change PWM to a 100% duty cycle
pwm_obj.ChangeDutyCycle(100)
time.sleep(1)

GPIO.cleanup()
