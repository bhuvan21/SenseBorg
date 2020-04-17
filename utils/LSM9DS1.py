import board
import busio
import adafruit_lsm9ds1
import time as clock
import math

class LSM9DS1:
    def __init__(self, i2c=None):
        if i2c == None:
            self.i2c = busio.I2C(board.SCL, board.SDA)
        else:
            self.i2c = i2c
        self.sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
        self.dt = None
        self.alpha = 0
        self.beta = 0
        self.gamma = 0
        self.bias = 0.98

    def get_gyro(self):
        return list(self.sensor.gyro)
    
    def get_acceleration(self):
        return list(self.sensor.acceleration)
    
    def get_magnometer(self):
        return list(self.sensor.magnetic)
    
    def get_gravity(self):
        acc = self.get_acceleration()
        gyro = self.get_gyro()
        c = clock.time()
        if self.dt is None:
            self.dt = 0
        else:
            self.dt = c - self.dt

        norm = (acc[0]**2 + acc[1]**2 + acc[2]**2) ** (1/2)
        scale = math.pi/2

        self.alpha = self.alpha + gyro[2]*self.dt 
        self.beta = self.bias * (self.beta + gyro[0]*self.dt) + (1.0-self.bias)*(acc[0]*scale/norm)
        self.gamma = self.bias * (self.gamma + gyro[1]*self.dt) + (1.0-self.bias) * (acc[1] * -scale / norm)

        print(self.alpha, self.beta, self.gamma)

        if self.dt == 0:
            self.dt = c