import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26

scale = [262, 294, 330, 349, 391, 440, 493, 523]

GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)
pwm.start(50)

for cnt in range(3):
    pwm.ChangeFrequency(262)
    time.sleep(1)
    pwm.ChangeFrequency(294)
    time.sleep(1)
    pwm.ChangeFrequency(330)
    time.sleep(1)

pwm.stop()
GPIO.cleanup()
