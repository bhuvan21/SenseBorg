import math
from utils.Sensor import Sensor

class Compass:
    def __init__(self, i2c=None):
        self.sensor = Sensor(raw=True, processed=True, maj=True, i2c=i2c)

    def get_heading(self, data=None):
        if data is None:
            raw = self.sensor.get_all()
        else:
            raw = data
        accel = raw[0]
        mag = raw[1]

        acc_x_norm = accel[0]/math.sqrt(accel[0]**2 + accel[1]**2 + accel[2]**2)
        acc_y_norm = accel[1]/math.sqrt(accel[0]**2 + accel[1]**2 + accel[2]**2)
        pitch = math.asin(acc_x_norm)
        roll = -math.asin(acc_y_norm/math.cos(pitch))

        mag_x_comp = mag[0] * math.cos(pitch) + mag[2] * math.sin(pitch)
        mag_y_comp = mag[0] * math.sin(roll) * math.sin(pitch) + mag[1] * math.cos(roll) + mag[2] * math.sin(roll) * math.cos(pitch)
        heading = 180 * math.atan2(mag_y_comp, mag_x_comp) / math.pi

        if heading < 0:
            heading += 360

        return int(heading)
    
    def get_maj(self):
        return [y*(57.2958) for y in self.sensor.get_all()[6]]
