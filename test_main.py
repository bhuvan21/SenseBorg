import math
import busio
import board
import numpy as np
from time import sleep

from Belt import Belt
from utils.graphing import ConfigurableGraph

order = [2, 11, 0, 14, 3, 7, 4, 9, 6, 8, 5, 10, 13, 1, 12]
belt = Belt(order = order)




#y = ConfigurableGraph(x_gyro, (-360, 360))
print("epic")

while True:
   belt.v1_mainloop()
#y.circular(0.2)
#y.test(2, 5)