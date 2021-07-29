import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rows = [21, 7, 9, 12, 2, 10, 3, 27]
cols = [1, 4, 17, 20, 22, 16, 8, 25]


def init():
    for pin in rows:
        GPIO.setup(pin, GPIO.OUT, initial=0)

    for pin in cols:
        GPIO.setup(pin, GPIO.OUT, initial=1)


num = True


def wait_for_time():
    time.sleep(1)
    num = False


o = True
t = True


def wait_for_o():
    time.sleep(1)
    o = False


def wait_for_t():
    time.sleep(1)
    t = False


init()
try:
    while True:
        while num:
            # for row in range(8):
            #     init()
            #     GPIO.output(rows[row], 1)
            #     for col in range(8):
            #         GPIO.output(cols[col], 0)
            #         time.sleep(0.5)
            # # for i in range(8):
            # #     init()
            # #     GPIO.output(rows[i], 1)
            # #     GPIO.output(cols[0], 0)
            # #     GPIO.output(cols[7], 0)
            # # for i in range(8):
            # #     init()
            # #     GPIO.output(cols[i], 0)
            # #     GPIO.output(rows[0], 1)
            # #     GPIO.output(rows[7], 1)
            # # # for i in range(8):
            # # #     init()
            # # #     GPIO.output(rows[i], 1)
            # # #     GPIO.output(rows[i], 1)
            # # #     GPIO.output(cols[3], 0)
            # # #     GPIO.output(cols[4], 0)
            # # # for i in range(8):
            # # #     init()
            # # #     GPIO.output(rows[3], 1)
            # # #     GPIO.output(rows[4], 1)
            # # #     GPIO.output(cols[i], 0)
            # # #     GPIO.output(cols[i], 0)
            for i in range(1, 6):
                init()
                GPIO.output(rows[0], 1)
                GPIO.output(rows[7], 1)
                GPIO.output(cols[i], 0)
            for i in range(8):
                init()
                GPIO.output(rows[i], 1)
                GPIO.output(cols[1], 0)
            for i in range(1, 7):
                init()
                GPIO.output(rows[i], 1)
                GPIO.output(cols[6], 0)
            wait_for_time()

        while o:
            for i in range(8):
                init()
                GPIO.output(rows[i], 1)
                GPIO.output(cols[0], 0)
                GPIO.output(cols[7], 0)
            for i in range(8):
                init()
                GPIO.output(cols[i], 0)
                GPIO.output(rows[0], 1)
                GPIO.output(rows[7], 1)
            wait_for_o()
        while t:
            for i in range(8):
                init()
                GPIO.output(rows[0], 1)
                GPIO.output(rows[1], 1)
                GPIO.output(cols[i], 0)
            for i in range(8):
                init()
                GPIO.output(rows[i], 1)
                GPIO.output(cols[3], 0)
                GPIO.output(cols[4], 0)
            wait_for_t()
        num = True
        o = True
        t = True

except KeyboardInterrupt:
    GPIO.cleanup()
