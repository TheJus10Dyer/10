# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:48:48 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('CPB_Datalog_NXP9DOF_test.txt')
t = data[:,0]
t -= t[0]
gx = data[:,1]
gy = data[:,2]
gz = data[:,3]
mx = data[:,4]
my = data[:,5]
mz = data[:,6]
ax = data[:,7]
ay = data[:,8]
az = data[:,9]
T = data[:,10]

plt.figure()
plt.plot(t,T, label = 'Temp')
plt.title('Thermistor')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (C)')
plt.legend()
plt.grid()

plt.figure()
plt.plot(t,gx,'r-',label= 'gx')
plt.plot(t,gy,'g-',label= 'gy')
plt.plot(t,gz,'b-',label= 'gz')
plt.title('Gyroscope')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velo (rad/s)')
plt.legend()
plt.grid()

plt.figure()
plt.plot(t,mx,'r-',label= 'mx')
plt.plot(t,my,'g-',label= 'my')
plt.plot(t,mz,'b-',label= 'mz')
plt.title('Magnetometer')
plt.xlabel('Time (s)')
plt.ylabel('MagField (uTesla)')
plt.legend()
plt.grid()

plt.figure()
plt.plot(t,ax,'r-',label= 'ax')
plt.plot(t,ay,'g-',label= 'ay')
plt.plot(t,az,'b-',label= 'az')
plt.title('Accelerometer')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.legend()
plt.grid()


