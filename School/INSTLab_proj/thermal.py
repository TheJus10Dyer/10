# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:56:40 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('thermalconduct.txt')
time = data[:,0]-2939.29
T = data[:,1]

T0 = 24
TMAX = 60.5
DELT = TMAX - T0

Ts = 700
sigma = 4/Ts
print('time constant = ',sigma)

time_fit = np.linspace(0,Ts,1000)
Tfit = T0 + DELT*np.exp(-sigma*time_fit)


plt.plot(time,T,'b*', label = 'Data')
plt.plot(time_fit,Tfit,'r-', label = 'Fitted Equation')
plt.xlim([0,700])
plt.xlabel('Time (sec)')
plt.ylabel('Temperature (C)')
plt.grid()
plt.show()
