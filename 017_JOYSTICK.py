import spidev
import os
import time

swt_channel = 2  # SWITCH NU REU NEUN GEO JOYSTICK = 0
vrx_channel = 1  # VRX IS CONNECTED TO 1
vry_channel = 0  # VRY IS CONNECTED TO 2

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

    print(f"vrx = {vrx_pos} , vry = {vry_pos}, swt = {swt_val}")
    time.sleep(0.5)
