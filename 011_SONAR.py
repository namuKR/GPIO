import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26
pin_echo = 2
pin_trig = 3

red = 19

GPIO.setup(pin_buzzer, GPIO.OUT)
GPIO.setup(pin_echo, GPIO.IN)
GPIO.setup(pin_trig, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
pwm = GPIO.PWM(pin_buzzer, 700)


def get_dis():
    GPIO.output(pin_trig, 0)
    time.sleep(0.1)
    GPIO.output(pin_trig, 1)
    time.sleep(0.00001)
    GPIO.output(pin_trig, 0)

    while GPIO.input(pin_echo) == 0:
        pulse_start = time.time()

    while GPIO.input(pin_echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17000
    distance = round(distance, 2)
    print(str(distance) + 'cm')
    return distance


try:
    while True:
        distance = get_dis()
        if distance < 10:
            GPIO.output(red, GPIO.HIGH)
            pwm.start(90)
            pwm.ChangeFrequency(10000)
            time.sleep(0.1)
            pwm.stop()
            GPIO.output(red, GPIO.LOW)
        elif distance < 20:
            GPIO.output(red, GPIO.HIGH)
            pwm.start(90)
            pwm.ChangeFrequency(10000)
            time.sleep(0.4)
            pwm.stop()
            GPIO.output(red, GPIO.LOW)
        elif distance < 30:
            GPIO.output(red, GPIO.HIGH)
            pwm.start(90)
            pwm.ChangeFrequency(10000)
            time.sleep(1)
            pwm.stop()
            GPIO.output(red, GPIO.LOW)
        else:
            pwm.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
