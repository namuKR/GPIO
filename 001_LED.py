import RPi.GPIO as GPIO
import time
# LINE 17
LED_RED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED,GPIO.OUT)

sec = int(input('Enter Interval'))
try:
    while True:
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(LED_RED, GPIO.LOW)
        time.sleep(sec)
except KeyboardInterrupt:
    GPIO.cleanup()
