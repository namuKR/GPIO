from flask import *
import RPi.GPIO as GPIO
import time
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
pin_dht = 18

GPIO.setmode(GPIO.BCM)

LED_RED = 2
LED_BLUE = 3
LED_YELLOW = 4

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/led_button/')
def led_button():
    color = request.args.get('color')
    on_off = request.args.get('on_off')
    if color == 'red':
        if on_off == "on":
            GPIO.output(LED_RED, 1)
        else:
            GPIO.output(LED_RED, 0)
    elif color == 'blue':
        if on_off == "on":
            GPIO.output(LED_BLUE, 1)
        else:
            GPIO.output(LED_BLUE, 0)
    elif color == 'yellow':
        if on_off == "on":
            GPIO.output(LED_YELLOW, 1)
        else:
            GPIO.output(LED_YELLOW, 0)
    return render_template('home.html')


@app.route('/about')
def about():
    return 'This is the ABOUT page.'


@app.route('/led')
def _led():
    return """
    <select id="sel"><option id="r" value="r">RED</option><option id="b" value="b">BLUE</option><option id="y" value="y">YELLOW</option></select>
    <button id="on">ON</button>  <button id="off">OFF</button> <script>document.getElementById('on').onclick = function() {sel = document.getElementById('sel'); if (sel.value == 'r'){location.href += '/red/on'};if (sel.value == 'b'){location.href += '/blue/on'};if (sel.value == 'y'){location.href += '/yellow/on'}};document.getElementById('off').onclick = function() {sel = document.getElementById('sel'); if (sel.value == 'r'){location.href += '/red/off'};if (sel.value == 'b'){location.href += '/blue/off'};if (sel.value == 'y'){location.href += '/yellow/off'}}</script>
    """


@app.route('/led/<color>/<on_off>')
def led_path(color, on_off):
    if color.lower() == 'red':
        if on_off.lower() == 'on':
            GPIO.output(LED_RED, 1)
        elif on_off.lower() == 'off':
            GPIO.output(LED_RED, 0)
        else:
            return 'error'
    elif color.lower() == 'blue':
        if on_off.lower() == 'on':
            GPIO.output(LED_BLUE, 1)
        elif on_off.lower() == 'off':
            GPIO.output(LED_BLUE, 0)
        else:
            return 'error'
    elif color.lower() == 'yellow':
        if on_off.lower() == 'on':
            GPIO.output(LED_YELLOW, 1)
        elif on_off.lower() == 'off':
            GPIO.output(LED_YELLOW, 0)
        else:
            return 'error'

    return color + ' is ' + on_off


@app.route('/<username>')
def user(username):
    return render_template('back.html', user=username)


@app.route('/dht')
def dht11():
    h, t = Adafruit_DHT.read_retry(sensor, pin_dht)
    DHT = {'temp': t, 'humi': h}
    return render_template('dht11.html', **DHT)


@app.route('/door')
def door_control():
    pin_pir = 14
    pin_red = 2
    pin_blue = 3
    sound = 26
    door = 19
    GPIO.setup(pin_pir, GPIO.IN)
    GPIO.setup(pin_red, GPIO.OUT)
    GPIO.setup(pin_blue, GPIO.OUT)
    GPIO.setup(sound, GPIO.OUT)
    GPIO.setup(door, GPIO.OUT)
    pwm = GPIO.PWM(sound, 0.1)
    pwm.start(90)
    dr = GPIO.PWM(door, 50)
    scale = [1, 523, 660, 782, 523]
    scale2 = [1, 782, 782, 523]
    dr.start(0)
    open_close = request.args.get('open_close')
    if open_close == 'open':
        dr.start(0)
        dr.ChangeDutyCycle(5)
        for i in range(4):
            GPIO.output(pin_red, 1)
            GPIO.output(pin_blue, 1)
            pwm.start(90)
            pwm.ChangeFrequency(scale[i])
            time.sleep(0.45)
            pwm.stop()
            GPIO.output(pin_red, 0)
            GPIO.output(pin_blue, 0)
    elif open_close == "close":
        dr.start(0)
        dr.ChangeDutyCycle(10)
        for i in range(4):
            GPIO.output(pin_red, 1)
            GPIO.output(pin_blue, 1)
            pwm.start(90)
            pwm.ChangeFrequency(scale2[i])
            time.sleep(0.45)
            pwm.stop()
            time.sleep(0.05)
            GPIO.output(pin_red, 0)
            GPIO.output(pin_blue, 0)
    return render_template("home.html")


@app.route('/rgb_led')
def _rgb_led():
    try:
        _r = int(request.args.get('red_range'))
        _g = int(request.args.get('green_range'))
        _b = int(request.args.get('blue_range'))

        _leds = [2, 3, 4]
        p = []
        for i in range(3):
            p.append(GPIO.PWM(_leds[i], 2000))
            p[i].start(0)

        def setColor(list_):
            for i in range(3):
                list_[i] = list_[i]/3  # Ah My EYES!
                p[i].ChangeDutyCycle(list_[i])

        setColor([_r, _g, _b])
        return render_template('home.html')
    except Exception:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
