import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_RED = 21

GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)

pwm = GPIO.PWM(LED_RED, 50)
pwm.start(0)

for i in range(30):
    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.2)
    for dc in range(100, -1, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.2)

pwm.stop()
GPIO.cleanup()