import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rows = [21, 7, 9, 12, 2, 10, 3, 27]
cols = [1, 4, 17, 20, 22, 16, 8, 25]

heart = [
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


def init():
    for pin in rows:
        GPIO.setup(pin, GPIO.OUT, initial=0)

    for pin in cols:
        GPIO.setup(pin, GPIO.OUT, initial=1)


init()
try:
    while True:
        for row in range(8):
            init()
            GPIO.output(rows[row], 1)
            for col in range(8):
                GPIO.output(cols[col], heart[row][col])

except KeyboardInterrupt:
    GPIO.cleanup()
