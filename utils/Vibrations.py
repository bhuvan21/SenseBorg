import board
import busio
import Adafruit_PCA9685

from time import sleep

class Vibrations:

    def __init__(self, units=None, i2c=None, order=[]):
        if i2c == None:
            self.i2c = busio.I2C(board.SCL, board.SDA)
        else:
            self.i2c = i2c
        
        self.pwm = Adafruit_PCA9685.PCA9685(i2c=self.i2c)
        
        if order == []:
            if units == None:
                self.units = 15
            else:
                self.units = units
            
            self.order = list(range(self.units))
        
        else:
            self.units = len(order)
            self.order = order

        self.on = list(range(self.units))
    
    def safe_pwm(self, a, b, c):
        try:
            self.pwm.set_pwm(a, b, c)
        except OSError:
            self.pwm.set_pwm(a,b,c)
        if abs(c - b) > 0:
            self.on[a] = True
        else:
            self.on[a] = False

    def test_motor(self, i, ordered=False, t=1):
        if ordered:
            i = self.order[i]
        self.safe_pwm(i, 0, 3000)
        sleep(t)
        self.safe_pwm(i, 0, 0)

    def circular(self, t=0.2):
        while True:
            try:
                for i in self.order:
                    self.test_motor(i, t)
            except:
                    
                for i in self.order:
                   self.safe_pwm(i, 0, 0)
                return

    def all_off(self):
        for j in self.order:
            self.safe_pwm(j, 0, 0)


    
