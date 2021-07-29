import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26

scale = [262, 294, 330, 349, 391, 440, 493, 523]

GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)
pwm.start(90)


def sol():
    pwm.ChangeFrequency(391)
    time.sleep(0.5)


def la():
    pwm.ChangeFrequency(440)
    time.sleep(.5)


def mi():
    pwm.ChangeFrequency(330)
    time.sleep(.5)


def re():
    pwm.ChangeFrequency(294)
    time.sleep(.5)


def do():
    pwm.ChangeFrequency(262)
    time.sleep(.5)


def sol2():
    for i in range(2):
        sol()
        pwm.stop()
        time.sleep(.25)
        pwm.start(90)


def la2():
    for i in range(2):
        la()
        pwm.stop()
        time.sleep(.25)
        pwm.start(90)


def mi2():
    for i in range(2):
        mi()
        pwm.stop()
        time.sleep(.25)
        pwm.start(90)


sol2()
la2()
sol2()
mi()
pwm.stop()
time.sleep(.5)
pwm.start(90)
sol2()
mi2()
re()
pwm.stop()
time.sleep(.5)
pwm.start(90)
sol2()
la2()
sol2()
mi()
pwm.stop()
time.sleep(.5)
pwm.start(90)
sol()
mi()
re()
mi()
do()


pwm.stop()
GPIO.cleanup()
