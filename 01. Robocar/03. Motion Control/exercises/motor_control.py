from PCA9685 import Driver
import time

# Create an instance of PWM Driver class
driver = Driver()
driver.setFrequency(1000)

pwm_dir = driver.CHANNEL_0
pwm_spd = driver.CHANNEL_1

try:
    driver.setOn(pwm_dir)
    driver.setPWM(pwm_spd,4095)
    time.sleep(5)
    driver.setOff(pwm_dir)
    driver.setPWM(pwm_spd,512)
    time.sleep(5)
except KeyboardInterrupt:
    print "Program interrupted...!"
finally:
    print "Turning Off All Channels...!"
    driver.setAllOff()

