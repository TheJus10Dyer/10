# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 07:28:14 2022

@author: Justin
"""

import time
from adafruit_circuitplayground import cp


cp.pixels.brightness = 0.3



def scale_range(value):

    return round(value / 310*9)

while True:
    if cp.switch is False:
        for i in range(10):
            peak = scale_range(cp.light)
            if i >= peak:
                cp.pixels[i] = (0, 0, 0)
            else:
                cp.pixels[i] = (0, 0, 0)
        cp.pixels.show()
        time.sleep(.1)
    if cp.switch is True:
        peak = scale_range(cp.light)
        time.sleep(.01)

        for i in range(10):
            if i >= peak:
                cp.pixels[i] = (100, 100, 100)
            else:
                cp.pixels[i] = (0, 0, 0)
        cp.pixels.show()

