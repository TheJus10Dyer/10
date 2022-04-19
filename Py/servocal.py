# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:38:46 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

degrees = np.array([0,3.3])
pulse = np.array([70,110])

coeff = np.polyfit(degrees, pulse, 1)
print(coeff)

degrees_fit = np.linspace(0, 3.3,1000)
pulse_fit = np.polyval(coeff, degrees_fit)


plt.plot(degrees_fit, pulse_fit, 'r-')
plt.plot(degrees,pulse, 'b*')
plt.xlabel('Degrees')
plt.ylabel('Pulse (ms)')
plt.title('Servo (Pulse vs Deg)')
plt.show()
