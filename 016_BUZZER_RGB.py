import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26

LED_RED = 2
LED_GREEN = 3
LED_BLUE = 4

LEDs = [2, 3, 4]

for i in range(3):
    GPIO.setup(LEDs[i], GPIO.OUT, initial=0)
p = ["", "", ""]

scale = [262, 294, 330, 349, 391, 440, 493, 523]
twimkile = [1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1, 5, 5, 4, 4, 3,
    3, 2, 5, 5, 4, 4, 3, 3, 2, 1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1]

GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)
for i in range(3):
    p[i] = GPIO.PWM(LEDs[i], 2000)
    p[i].start(0)


def setColor(list_):
    for i in range(3):
        list_[i] = list_[i]/3  # Ah My EYES!
        p[i].ChangeDutyCycle(list_[i])


keys = [[100, 0, 0], [100, 40, 0], [100, 100, 0],
    [0, 100, 0], [0, 0, 100], [50, 0, 50]]

for i in range(42):
    pwm.start(90)
    pwm.ChangeFrequency(scale[twimkile[i]-1])
    setColor(keys[twimkile[i]-1])
    time.sleep(.5)
    pwm.stop()
    time.sleep(.1)

pwm.stop()
GPIO.cleanup()
