import Adafruit_PCA9685
from time import sleep
pwm = Adafruit_PCA9685.PCA9685()

order = []
c = int(input("How many?"))
for i in range(c):
    for j in range(16):
        if j not in order:
            pwm.set_pwm(j, 0, 3000)
            print(j)
            sleep(1)
            pwm.set_pwm(j, 0, 0)
    curr = int(input("Which turned on?"))
    order.append(curr)
print(order)
