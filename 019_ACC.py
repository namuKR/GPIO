import time
import board
import busio
import adafruit_adxl34x as adxl

i2c = busio.I2C(board.SCL, board.SDA)

ac = adxl.ADXL345(i2c)
ac.enable_freefall_detection(threshold=10, time=25)
ac.enable_motion_detection(threshold=18)
ac.enable_tap_detection(tap_count=1, threshold=5, duration=40, latency=40)

while True:
    x, y, z = ac.acceleration
    print('x: {0:2f} y:{1:2f} z:{2:2f}'.format(x, y, z))
    time.sleep(.5)
