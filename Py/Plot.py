# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 09:40:59 2022

@author: Justin
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('MatSci.txt')

sa = data[:,0]
cycles = data[:,1]

plt.plot(cycles,sa)
plt.xlabel('Cycles to Failure')
plt.ylabel('Stress Amplitude (MPa)')
plt.title('S-N plot')
plt.grid()
plt.show()