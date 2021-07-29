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

arrSeg=[
[1,1,1,1,1,1,0], [0,1,1,0,0,0,0], [1,1,0,1,1,0,1], [1,1,1,1,0,0,1], [0,1,1,0,0,1,1], [0,0,0,0,0,0,0]
]



try:
    cnt = 0
    for pin in pin_num:
        if arrSeg[0][cnt]==1:
            GPIO.output(pin, GPIO.HIGH)
        cnt += 1

except KeyboardInterrupt:
    GPIO.cleanup()