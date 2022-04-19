# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:49:52 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('PotentioData.txt')

time = data[:,1]
time -= time[0]

D = data[:,0]

voltage = 5*D/2.0**16

plt.plot(time, voltage)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Voltage (V)')
plt.show()