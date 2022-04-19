# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:20:14 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

#data = np.loadtxt('TestData.txt')
#T = data[:,0]
#R = data[:,1]

x = np.linspace(-10,10,100)
y = 3*x
k = 168750 - 36078201*x + 60500000000*(x**2) - 159.3*(x**6)
plt.plot(x,k)
#plt.plot(73.76,129, marker="o", markerfacecolor = "red")
plt.grid()
plt.xlabel('Temeperature (Celcius)')
plt.ylabel('Resistance (Ohms) ')

plt.show()