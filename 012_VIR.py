import random
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

pin_pir = 14
pin_red = 2
pin_blue = 3
sound = 26
GPIO.setup(pin_pir, GPIO.IN)
GPIO.setup(pin_red, GPIO.OUT)
GPIO.setup(pin_blue, GPIO.OUT)
GPIO.setup(sound, GPIO.OUT)
pwm = GPIO.PWM(sound, 0.1)
pwm.start(90)
scale = [523, 660, 782, 523]
try:
    while True:
        if GPIO.input(pin_pir) == GPIO.HIGH:
            for i in range(3):
                GPIO.output(pin_red, 1)
                GPIO.output(pin_blue, 1)
                pwm.start(90)
                pwm.ChangeFrequency(scale[i])
                time.sleep(0.45)
                pwm.stop()
                GPIO.output(pin_red, 0)
                GPIO.output(pin_blue, 0)

        else:
            GPIO.output(pin_red, 0)
            GPIO.output(pin_blue, 0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
