import math
import time

import board
import busio
import Adafruit_PCA9685

from utils.vector import *
from utils.Compass import Compass
from utils.Vibrations import Vibrations
from network import Sender

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
            self.vibrations = Vibrations(units=units, order=order)
        else:
            self.vibrations = vibrations
        
        self.sender = Sender()

    def v1_mainloop(self):
        a = time.time()
        try:
            if self.sensor.sensor.raw:
                all = self.sensor.sensor.get_all()
                t = time.time()
                cut = all[3:6]
                self.sender.queue.put(cut[0]+cut[2]+cut[1]+[t], block=False)
                
            raw = all[5]
            print("gyro", time.time() - t)
            fb = -raw[0]
            lr = -raw[2]
            if abs(lr) >30 or abs(fb) > 40:
                angleraw = angle_between((0, 1, 0), (lr, fb, 0))
                angle = angleraw
                if angleraw < 0:
                    angle = (180 - abs(angleraw)) + 180
                print(angle)
                index = int(angle/24)
                if self.vibrations.on[index]:
                    return
                else:
                    for n, j in enumerate(self.vibrations.on):
                        if j:
                            self.vibrations.safe_pwm(n, 0, 0)

                    test = min(int(math.sqrt((fb**2) + (lr**2))/150*3000), 3000)
                    self.vibrations.safe_pwm(index, 0, test)

            else:
                for n, j in enumerate(self.vibrations.on):
                    if j:
                        self.vibrations.safe_pwm(n, 0, 0)
        except Exception as e:
            print(e)
            self.vibrations.all_off()

        print(time.time()-a)