import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

BTN_RED = 17
BTN_BLUE = 22
BTN_YELLOW = 26

GPIO.setup(BTN_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

led_red = [False, 21]  # Off
led_blue = [False, 20]
led_yellow = [False, 16]
try:
    while True:
        btn_state_red = GPIO.input(BTN_RED)
        btn_state_blue = GPIO.input(BTN_BLUE)
        btn_state_yellow = GPIO.input(BTN_YELLOW)

        # if btn_state_red == True and btn_state_blue == True:
        #     print('PURPLE')
        if btn_state_red == False:
            print("RED")
            print(led_red[0])
            if led_red[0]:
                GPIO.output(led_red[1], 0)
                led_red[0] = False
            else:
                GPIO.output(led_red[1], 1)
                led_red[0] = True
        elif btn_state_blue == False:
            print("BLUE")
            if led_blue[0]:
                GPIO.output(led_blue[1], 0)
                led_blue[0] = False
            else:
                GPIO.output(led_blue[1], 1)
                led_blue[0] = True
        elif btn_state_yellow == False:
            print("YELLOW")
            if led_yellow[0]:
                GPIO.output(led_yellow[1], 0)
                led_yellow[0] = False
            else:
                GPIO.output(led_yellow[1], 1)
                led_yellow[0] = True
        time.sleep(0.25)
except KeyboardInterrupt:
    GPIO.output(led_red[1], 0)
    GPIO.output(led_blue[1], 0)
    GPIO.output(led_yellow[1], 0)
    GPIO.cleanup()
