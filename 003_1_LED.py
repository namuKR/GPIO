import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_RED = 2
LED_BLUE = 3
LED_YELLOW = 4

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
try:

    while True:
        GPIO.output(LED_RED, 1)
        GPIO.output(LED_BLUE, 1)
        GPIO.output(LED_YELLOW, 1)
        time.sleep(1)
        GPIO.output(LED_RED, 0)
        GPIO.output(LED_BLUE, 0)
        GPIO.output(LED_YELLOW, 0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()