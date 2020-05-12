import Adafruit_PCA9685
from time import sleep
pwm = Adafruit_PCA9685.PCA9685()

def test(i, t):
    pwm.set_pwm(i, 0, 3000)
    sleep(t)
    pwm.set_pwm(i, 0, 0)
    
order = [9, 7, 4, 0, 11, 2, 3, 14, 12, 13, 1, 10, 8, 5, 6]

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

