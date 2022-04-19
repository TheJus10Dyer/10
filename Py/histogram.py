# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 11:49:02 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('hist_3.txt')
time = data[:,0]
time -= time[0]
ambient = data[:,1]

mean = np.mean(ambient)
sd = np.std(ambient)
median = np.median(ambient)

print('Mean = ', mean,'\n', 'Median = ', median, '\n', 'Standard Deviation = ',sd)

mu = mean
s = sd

x = np.linspace(np.min(ambient), np.max(ambient), 100)
a = 1.0/(s*np.sqrt(2*np.pi))
b = (-(x-mu)**2)/(2*s**2)
pdf = (a*np.exp(b)/100)*471

plt.hist(ambient)
plt.xlabel('Voltage (V)')
plt.ylabel('Number of occurences')
plt.plot(x,pdf)
plt.show()