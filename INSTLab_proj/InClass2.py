# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 10, num=100)
T = 60*(1-np.exp(-5*t))+30

plt.xlim([0,10])
plt.ylim([80,95])

plt.title('T(t) = 60(1 - e^(-5t))+30')
plt.xlabel ('Time (sec)')
plt.ylabel ('Temperature (F)')
plt.grid()

plt.plot(t,T)

plt.show()
