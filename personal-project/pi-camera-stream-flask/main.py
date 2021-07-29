# Modified by smartbuilds.io
# Date: 27.09.20
# Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
from gpiozero import Button
import time
from threading import Thread
import asyncio
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led_blue = 2
led_red = 3
motion = 21
buzz = 20
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
pwm = GPIO.PWM(buzz, 1)
GPIO.output(2, 1)
GPIO.output(3, 0)
btn = 26
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.

# App Globals (do not edit)
app = Flask(__name__)

mode = 'living'

manualTurnOff = False


def mtochange():
    global manualTurnOff
    time.sleep(60)
    manualTurnOff = False


def motion_check(_mode):
    global mode, manualTurnOff
    if GPIO.input(btn) == False:
        manualTurnOff = True
        mtochange()
    elif _mode == 'patrol' and not manualTurnOff:
        if GPIO.input(motion) == GPIO.HIGH:
            pwm.start(90)
            pwm.ChangeFrequency(9999)
            time.sleep(.5)
            pwm.stop()
    

    time.sleep(.5)
    motion_check(mode)


@app.route('/')
def index():
    global mode
    mode = request.args.get('mode') or 'living'
    thread = Thread(target=motion_check, args=(mode,))
    thread.daemon = True

    threadStarted = False
    if mode == 'living':
        GPIO.output(led_red, 0)
        GPIO.output(led_blue, 1)
    elif mode == 'patrol':
        GPIO.output(led_blue, 0)
        GPIO.output(led_red, 1)
        if not threadStarted:
            thread.start()
            threadStarted = True

    return render_template('index.html')  # you can customze index.html here


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
