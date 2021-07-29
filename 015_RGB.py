import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_RED = 2
LED_GREEN = 3
LED_BLUE = 4

LEDs = [2, 3, 4]

for i in range(3):
    GPIO.setup(LEDs[i], GPIO.OUT, initial=0)

p = ["","",""]
try:
    for i in range(3):
        p[i] = GPIO.PWM(LEDs[i], 2000)
        p[i].start(0)

    def setColor(list_):
        for i in range(3):
            list_[i]=list_[i]/3 # Ah My EYES!
            p[i].ChangeDutyCycle(list_[i])
    while True:
        setColor([100, 0, 0])
        time.sleep(1)
        setColor([100, 40, 0])
        time.sleep(1)
        setColor([100, 100, 0]) # YELLOW
        time.sleep(1)
        setColor([0, 100, 0])
        time.sleep(1)
        setColor([0, 0, 100])
        time.sleep(1)
        setColor([50, 0, 50])
        time.sleep(1)
        setColor([0,0,50])
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
