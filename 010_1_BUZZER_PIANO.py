import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_buzzer = 26

scale = [262, 294, 330, 349, 391, 440, 493, 523]

GPIO.setup(pin_buzzer, GPIO.OUT)

pwm = GPIO.PWM(pin_buzzer, 1)
pwm.start(50)

# for cnt in range(3):
#     pwm.ChangeFrequency(262)
#     time.sleep(1)
#     pwm.ChangeFrequency(294)
#     time.sleep(1)
#     pwm.ChangeFrequency(330)
#     time.sleep(1)
while True:
    class _Getch:
        """Gets a single character from standard input.  Does not echo to the
    screen."""

        def __init__(self):
            self.impl = _GetchUnix()

        def __call__(self): return self.impl()

    class _GetchUnix:
        def __init__(self):
            import tty
            import sys

        def __call__(self):
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    a = _Getch().__call__()

    pwm.ChangeFrequency(int(scale[int(a)-1]))

pwm.stop()
GPIO.cleanup()
