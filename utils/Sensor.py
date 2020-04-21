import board
import busio
import adafruit_lsm9ds1
import time as clock
import math
import threading
import queue

class Sensor:

    MAG_LIMITS = ((-32000, 32000), (-25000, 25000), (-20000, 25000))
    ACCEL_LPF = 0.2
    MAG_LPF = 0.2
    GYRO_LPF = 0.2

    def __init__(self, raw=False, processed=False, i2c=None):
        if i2c == None:
            self.i2c = busio.I2C(board.SCL, board.SDA)
        else:
            self.i2c = i2c
        self.sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
        self.queue = queue.Queue()

        self.old_accel = [0, 0, 0]
        self.old_mag = [0, 0, 0]
        self.old_gyro = [0, 0, 0]

        self.raw = raw
        self.processed = processed

        self.thread = threading.Thread(None, self.mainloop)
        self.thread.setDaemon(True)
        self.thread.start()

    def get_all(self):
        result = None
        while result == None:
            try:
                result = self.queue.get()
            except queue.Empty:
                pass
        return result

    def get_gyro(self):
        return list(self.sensor.gyro)
    
    def get_acceleration(self):
        return list(self.sensor.acceleration)
    
    def get_magnometer(self):
        return list(self.sensor.magnetic)
    
    def get_gyro_raw(self):
        return self.sensor.read_gyro_raw()
    
    def get_accel_raw(self):
        return self.sensor.read_accel_raw()
    
    def get_mag_raw(self):
        return self.sensor.read_mag_raw()
    
    def mainloop(self):
        while 1:
            if self.raw:
                raw_accel = self.get_accel_raw()
                raw_mag = self.get_mag_raw()
                raw_gyro = self.get_gyro_raw()
                
                mag = [0, 0, 0]
                mag[0]  = (raw_mag[0] - self.MAG_LIMITS[0][0]) / (self.MAG_LIMITS[0][1] - self.MAG_LIMITS[0][0]) * 2 - 1.07
                mag[1]  = (raw_mag[1] - self.MAG_LIMITS[1][0]) / (self.MAG_LIMITS[1][1] - self.MAG_LIMITS[1][0]) * 2 - 1.0
                mag[2]  = (raw_mag[2] - self.MAG_LIMITS[2][0]) / (self.MAG_LIMITS[2][1] - self.MAG_LIMITS[2][0]) * 2 - 0.8

                accel = raw_accel
                gyro = raw_gyro
            
            if self.processed:
                proc_accel = self.get_acceleration()
                proc_mag = self.get_magnometer()
                proc_gyro = self.get_gyro()
                

            if self.old_accel != [0, 0, 0] and self.raw:
                mag = [(x*self.MAG_LPF)+ (self.old_mag[mag.index(x)]*(1-self.MAG_LPF)) for x in mag]
                accel = [(x*self.ACCEL_LPF)+ (self.old_accel[accel.index(x)]*(1-self.ACCEL_LPF)) for x in accel]
                gyro = [(x*self.GYRO_LPF)+ (self.old_gyro[gyro.index(x)]*(1-self.GYRO_LPF)) for x in gyro]
            
            try:
                if self.old_accel != [0, 0, 0]:
                    self.queue.get(block=False)
            except queue.Empty:
                pass
            
            final = []
            if self.raw:
                final += [accel, mag, gyro]
            if self.processed:
                final += [proc_accel, proc_mag, proc_gyro]

            self.queue.put(final)

            self.old_accel = accel
            self.old_mag = mag
            self.old_gyro = gyro
    