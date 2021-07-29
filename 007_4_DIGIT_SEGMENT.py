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

try:
    while True:
        now = datetime.datetime.now()
        hr = now.hour
        hr_0 = int(str(hr)[0])
        hr_1 = int(str(hr)[1])
        min = now.minute
        min_0 = int(str(min)[0] if min >= 10 else 0)
        if min >= 10 and min != 0:
            min_1 = int(str(min)[1])
        elif min >= 10:
            min_1 = 0
        elif min != 0:          
            min_1 = int(str(min)[0])
        # for digit in range(4):
        #     GPIO.output(digits[digit], 0)
        #     for led in range(7):
        #         GPIO.output(LEDs[led], numbers[digit][led])
        #     time.sleep(0.0035)
        #     GPIO.output(digits[digit], 1)
        for digit in range(4):
            GPIO.output(digits[digit], 0)
            for led in range(7):
                if digit == 0:
                    GPIO.output(LEDs[led], numbers[hr_0][led])
                elif digit == 1:
                    GPIO.output(LEDs[led], numbers[hr_1][led])
                elif digit == 2:
                    GPIO.output(LEDs[led], numbers[min_0][led])
                else:
                    GPIO.output(LEDs[led], numbers[min_1][led])
            time.sleep(0.0035)
            GPIO.output(digits[digit], 1)

except KeyboardInterrupt:
    GPIO.cleanup()
