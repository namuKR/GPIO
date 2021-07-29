import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

LEDs = [19, 0, 17, 3, 2, 13, 27, 4]
digits = [26, 6, 5, 22]

for led in LEDs:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(led, 1)

numbers = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]  # 9
]

input_num = [0, 0, 0, 0]
for i in range(4):
    input_num[i] = int(input(f'enter {i+1}\'th number: '))
try:
    while True:
        for digit in range(4):
            GPIO.output(digits[digit], 0)
            for led in range(7):
                GPIO.output(LEDs[led], numbers[input_num[digit]][led])
            time.sleep(0.0035)
            GPIO.output(digits[digit], 1)

except KeyboardInterrupt:
    GPIO.cleanup()
