import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT11
pin_dht = 18

while True:
    h, t = Adafruit_DHT.read_retry(sensor, pin_dht)
    if h is not None and t is not None:
        print('Temperature={0:0.1f}`C\nHumidity={1:0.1f}%'.format(t, h))
    else:
        print('READ ERROR')

    time.sleep(1)
