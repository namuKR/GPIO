import datetime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_step = [26, 19, 13, 6]
list
step_count = 4096
seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

for pin in pin_step:
    GPIO.setup(pin, GPIO.OUT, initial=0)
now = datetime.datetime.now()
direction = 2
motor_step_counter = 0
while now.hour == 12:
    for i in range(step_count):
        for pin in range(len(pin_step)):
            GPIO.output(pin_step[pin], seq[motor_step_counter][pin])
        if direction == 1:
            motor_step_counter = (motor_step_counter-1) % 8
        elif direction == 2:
            motor_step_counter = (motor_step_counter+1) % 8
        else:
            print("""direction is wrong.""")
        time.sleep(.0006)
GPIO.cleanup()
