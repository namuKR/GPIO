import RPi.GPIO as GPIO
import time
### CONFIG BCM PORTS ###
LED_RED = 17
LED_YELLOW = 27
LED_BLUE = 22
########################
GPIO.setmode(GPIO.BCM)
########################
### SETUP LED TO OUT ###
GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_YELLOW,GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
########################
# INPUT #
sec = float(input('Enter Interval'))
#########
## BLINK ##
try:
    while True:
        GPIO.output(LED_RED, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(LED_BLUE, GPIO.LOW)
        time.sleep(sec)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        time.sleep(sec)
        GPIO.output(LED_RED, GPIO.LOW)
        time.sleep(sec)
except KeyboardInterrupt:
    GPIO.cleanup()
############