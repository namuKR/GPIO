import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26

scale = [262, 294, 330, 349, 391, 440, 493, 523]
twimkile = [1,1,5,5,6,6,5,4,4,3,3,2,2,1,5,5,4,4,3,3,2,5,5,4,4,3,3,2,1,1,5,5,6,6,5,4,4,3,3,2,2,1]

GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)



for i in range(42):
    pwm.start(90)
    pwm.ChangeFrequency(scale[twimkile[i]-1])
    time.sleep(.5)
    pwm.stop()
    time.sleep(.1)

pwm.stop()
GPIO.cleanup()
