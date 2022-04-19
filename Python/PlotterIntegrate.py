# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 11:20:14 2022

@author: Justin
"""

#Import Modules and Data
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('AccelerometerData.txt')

#Interpret Data and Assign Variables
t = data[:,0]
y = data[:,2]

#Select data
y = y[t>40]
t = t[t>40]
y = y[t<70]
t = t[t<70]
t -= t[0]

#Filter Data
yf = 0*y
yf[0] = y[0]
s = 0.9
for i in range(0,len(y)-1):
    yf[i+1] = s*yf[i] + (1-s)*y[i]
    
#Adjust Phase Shift
tf = t-0.3


#Plot original and filtered data toi adjust filter
plt.plot(t,y, label='y')
plt.plot(tf,yf, label='yf')

plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Acceleration (m/s^2) ')
plt.legend()


#Integrate Acceleration
vel = 0*y
for i in range(0,len(y)-1):
    vel[i+1] = vel[i]+yf[i]*(tf[i+1]-tf[i])

#Convert m/s^2 to mph
vel = 2.23*vel

#Plot Velocity
plt.figure()
plt.plot(tf,vel)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (mph)')

plt.show()

#Integarate Velocity
vel = vel*1.477
pos = 0*vel
for i in range(0, len(vel)-1):
    pos[i+1] = pos[i]+vel[i]*(tf[i+1]-tf[i])
    
plt.figure()
plt.plot(tf,pos)
plt.grid()
plt.xlabel('Time (sec)')
plt.ylabel('Position (Feet)')