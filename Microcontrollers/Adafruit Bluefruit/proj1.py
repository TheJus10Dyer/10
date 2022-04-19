# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:39:22 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn-poster')

t = np.linspace(0, 100, num=100)
m = 68.1
c = 12.5
g = 9.8
v = (g*m/c)*(1 - np.exp(-(c/m)*t))


plt.xlabel ('Time (sec)')
plt.ylabel ('Velocity (V)')
plt.grid()

plt.plot(t,v)

plt.show()
