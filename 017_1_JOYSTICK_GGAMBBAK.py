import spidev
import os
import time
import RPi.GPIO as _g

swt_channel = 2  # SWITCH NU REU NEUN GEO JOYSTICK = 0
vrx_channel = 1  # VRX IS CONNECTED TO 1
vry_channel = 0  # VRY IS CONNECTED TO 2
_g.setmode(_g.BCM)
leds = [2, 3, 4]

for l in leds:
    _g.setup(l, _g.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000  # million hz!


def readChannel(channel):
    val = spi.xfer2([1, (8+channel) << 4, 0])
    data = ((val[1] & 3) << 8) + val[2]
    return data


while True:
    vrx_pos = readChannel(vrx_channel)
    vry_pos = readChannel(vry_channel)
    swt_val = readChannel(swt_channel)

    if vrx_pos < 300:
        _g.output(leds[0], 1)
        time.sleep(.2)
        _g.output(leds[0], 0)

    if vrx_pos > 700:

        _g.output(leds[2], 1)

        time.sleep(.2)

        _g.output(leds[2], 0)

    if swt_val > 0:
        _g.output(leds[1], 1)
        time.sleep(.2)
        _g.output(leds[1], 0)

    print(vrx_pos, vry_pos, swt_val)

    time.sleep(0.5)
