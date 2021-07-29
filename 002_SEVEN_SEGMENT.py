import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

pin_num=[16, 12, 13, 19, 26, 20, 21]
pin_dp = 6
GPIO.setwarnings(False)
for num in pin_num:
    GPIO.setup(num, GPIO.OUT)
    GPIO.output(num, GPIO.LOW)
GPIO.setup(pin_dp, GPIO.LOW)
GPIO.setwarnings(True)
########################
# INPUT #
sec = int(input('Enter Interval'))
#########

seg = [
    [16, 12, 13, 19, 26, 20]
    ,[16, 13]
    ,[16, 12, 21, 26, 19]
    ,[16, 12, 13, 19, 21]
    ,[20, 21, 12, 13]
    ,[16, 20, 21, 13, 19]
    ,[16, 20, 26, 19, 13, 21]
    ,[20, 16, 12, 13]
    ,[16, 12, 13, 19, 26, 20, 21]
    ,[16, 12, 13, 19, 26, 21]
]


## BLINK ##
try:
    while True:
        for i in seg[sec]:
            GPIO.output(i, GPIO.HIGH)
                
        
except KeyboardInterrupt:
    GPIO.cleanup()
############