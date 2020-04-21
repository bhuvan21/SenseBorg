from Compass import Compass
import busio
import board
i2c = busio.I2C(board.SCL, board.SDA)
x = Compass(i2c)
while 1:
    print([int(y*57.2958) for y in x.sensor.get_all()][1])