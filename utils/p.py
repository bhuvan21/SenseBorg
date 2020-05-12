from Compass import Compass
import busio
import board
import numpy as np
import math
from graphing import ConfigurableGraph
i2c = busio.I2C(board.SCL, board.SDA)
x = Compass(i2c)
'''
while 1:
    print([int(y) for y in x.get_maj()][0])
'''
def a():
    return x.sensor.get_gyro()[0]
#y = ConfigurableGraph(a, (-360, 360))

import Adafruit_PCA9685
from time import sleep
pwm = Adafruit_PCA9685.PCA9685()

def safe_pwm(a, b, c):
    try:
        pwm.set_pwm(a, b, c)
    except OSError:
        pwm.set_pwm(a,b,c)

def test(i, t):
    pwm.set_pwm(i, 0, 3000)
    sleep(t)
    pwm.set_pwm(i, 0, 0)
    
order = [2, 11, 0, 14, 3, 7, 4, 9, 6, 8, 5, 10, 13, 1, 12]

def circular(t):
    global order
    while True:
        try:
            for i in order:
                test(i, t)
        except:
                
            for i in order:
                pwm.set_pwm(i, 0, 0)
            return

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    sf = 1
    if v2_u[0] > 0:
        sf = -1
    return sf*np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))


try:
    on = [0 for i in range(15)]
    while True:
        raw = x.sensor.get_gyro()
        fb = -raw[0]
        lr = -raw[2]
        if abs(lr) >30 or abs(fb) > 40:
            angleraw = angle_between((0, 1, 0), (lr, fb, 0))
            angle = angleraw
            if angleraw < 0:
                angle = (180 - abs(angleraw)) + 180
            index = int(angle/24)
            if on[index]:
                continue
            else:
                for n, j in enumerate(on):
                    if j:
                        pwm.set_pwm(order[n], 0, 0)
                        print(n, "off")
                        on[n] = 0
                print(index, "on")
                test = min(int(math.sqrt((fb**2) + (lr**2))/150*3000), 3000)
                print(test)
                pwm.set_pwm(order[index], 0, test)
                on[index] = 1
        else:
            for n, j in enumerate(on):
                if j:
                    print(n, "off")
                    pwm.set_pwm(order[n], 0, 0)
                    on[n] = 0
except Exception as e:
    print(e)
    for j in order:
        pwm.set_pwm(j, 0, 0)

#circular(0.2)
#test(2, 5)