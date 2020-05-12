import math

import board
import busio
import Adafruit_PCA9685

from utils.vector import *
from utils.Compass import Compass
from utils.Vibrations import Vibrations

class Belt:
    def __init__(self, sensor=None, vibrations=None, i2c=None, units=None, order=None):
        if i2c == None:
            self.i2c = busio.I2C(board.SCL, board.SDA)
        else:
            self.i2c = i2c
        if sensor is None:
            self.sensor = Compass(i2c=self.i2c)
        else:
            self.sensor = sensor
        
        if vibrations is None:
            self.vibrations = Vibrations(units=units, i2c=self.i2c, order=order)
        else:
            self.vibrations = vibrations

    def v1_mainloop(self):
        try:
            raw = self.sensor.sensor.get_gyro()
            fb = -raw[0]
            lr = -raw[2]
            if abs(lr) >30 or abs(fb) > 40:
                angleraw = angle_between((0, 1, 0), (lr, fb, 0))
                angle = angleraw
                if angleraw < 0:
                    angle = (180 - abs(angleraw)) + 180
                index = int(angle/24)
                if self.vibrations.on[index]:
                    return
                else:
                    for n, j in enumerate(self.vibrations.on):
                        if j:
                            self.vibrations.safe_pwm(self.vibrations.order[n], 0, 0)

                    test = min(int(math.sqrt((fb**2) + (lr**2))/150*3000), 3000)
                    self.vibrations.safe_pwm(self.vibrations.order[index], 0, test)

            else:
                for n, j in enumerate(self.vibrations.on):
                    if j:
                        self.vibrations.safe_pwm(self.vibrations.order[n], 0, 0)
        except Exception as e:
            print(e)
            self.vibrations.all_off()