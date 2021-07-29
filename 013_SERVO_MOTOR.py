import RPi.GPIO as GPIO
import time

servoPin = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)

try:
    while True:
        pwm.start(0)
        # for dc in range(3, 13, 1):
        #     pwm.ChangeDutyCycle(dc)
        #     time.sleep(.1)
        # pwm.start(12)
        # for dc in range(12, 3, -1):
        #     pwm.ChangeDutyCycle(dc)
        #     time.sleep(.1)

        pwm.ChangeDutyCycle(5)
        time.sleep(2)
        pwm.ChangeDutyCycle(10)
        time.sleep(2)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
