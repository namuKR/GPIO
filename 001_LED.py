import RPi.GPIO as GPIO
import time
### CONFIG BCM PORTS ###
LED_RED = 17
LED_YELLOW = 27
########################
GPIO.setmode(GPIO.BCM)
########################
### SETUP LED TO OUT ###
GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_YELLOW,GPIO.OUT)
########################
# INPUT #
sec = int(input('Enter Interval'))
#########
## BLINK ##
try:
    while True:
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        time.sleep(sec)
except KeyboardInterrupt:
    GPIO.cleanup()
############