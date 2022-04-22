# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 08:54:25 2022

@author: Justin
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import project_3_functions as f

print('Project 3. ODE of modeling a cylinder oscillating in still water.\n')

# input parameters from keyboard
c = float(input('Damping Coefficient c : '))# c=0.1
dt = float(input('Time Step Size (h) : '))
#dt = 0.1, 0.1(sec), 0.5 (sec) , 1(sec), 5(sec), 10(sec)
m = 1.0
k = 0.01

#Set t information
ti = 0.0 #Initial t
tf = 200.0 #Final t

# Initial Conditions @ t=ti
yi = 0.2
zi = 0.0

#Assign h = t_(i+1) - t_(i) = dt
h = dt

#Create vectors to store data for t(i) & y(i)
numberOfDataSets = math.floor((tf-ti)/dt) + 1
t = np.zeros(numberOfDataSets)

y_exact = np.zeros(numberOfDataSets)

y_ex = np.zeros(numberOfDataSets) #Explicit Euler results for y
z_ex = np.zeros(numberOfDataSets) #Explicit Euler results for z = dy/dt

y_mid = np.zeros(numberOfDataSets)
z_mid = np.zeros(numberOfDataSets)

y_rk4 = np.zeros(numberOfDataSets)
z_rk4 = np.zeros(numberOfDataSets)

#assign the initial values for all y(0) and z(0)
i = 0
t[i]=ti
y_exact[i]=yi
y_ex[i]=yi
z_ex[i]=zi
y_mid[i]=yi
z_mid[i]=zi
y_rk4[i]=yi
z_rk4[i]=zi

flag = 1 #declare flag to stop while loop to get y values from ti until tf with step h

while (flag):
#If t[i]+dt exceeds tf, h=tf-t
    if t[i]+dt > tf:
        h=tf-t
        
    t[i+1]=t[i]+h;
    
    #calculate the exact solution
    y_exact[i+1] = f.y_exact_solution(t[i+1])
    
    #Calculate the Explicit Euler Solution   
    y_ex[i+1], z_ex[i+1] = f.explicit_euler(y_ex[i], z_ex[i], t[i], h, m, c, k)
    
    #Calculate the midpoint solution   
    y_mid[i+1], z_mid[i+1] = f.midpoint(y_mid[i], z_mid[i], t[i], h, m, c, k);
    
    #Calculate the RK4 solution
    y_rk4[i+1], z_rk4[i+1] = f.RK4(y_rk4[i], z_rk4[i], t[i], h, m, c, k);
    
    i = i + 1
    print('@ x= {:10.7} : y_Exact Solution= {:10.7f} , y_Explicit Euler= {:10.7f} , y_MidPoint= {:10.7f}, y_RK4= {:10.7f} \n' .format(t[i], y_exact[i], y_ex[i], y_mid[i], y_rk4[i]));
    
    #If t eaches tf, stop the while loop
    if i >= numberOfDataSets -1:
        flag = 0
    
    #end of while loop

#plot y against t

fig1 = plt.figure(1)
plt.plot(t, y_exact, 'o-', t, y_ex, '-x', t, y_mid, '+g', t,y_rk4, '-.*k') #plot 4 curves pf y vs t
plt.legend(('y_Exact Solution for c=0.1 only', 'y_Explicit Euler Method', 'y_Mid Point', 'y_RK4'), loc = 0)
plottitle = 'Figure 1. y vs. t for ODE : c={:8.5f}kg/s& h={:8.5f}s' .format(c, h)
plt.title(plottitle)
plt.xlabel('t (sec)')
plt.ylabel('y (m)')
plotFileName = 'y-t c' + str(c) + 'h' + str(h) + '.jpg'
plt.savefig(plotFileName, format = 'jpg') #save plot in a jpg format file
plt.show() #show the plot on screen

# plot z against t
fig2 = plt.figure(2)
plt.plot(t, z_ex, '-x', t, z_mid, '+g', t,z_rk4, '-.*k') #plot 3 curves for z vs t
plt.legend(('z_Explicit Euler Method', 'z_Mid Point', 'z_RK4'), loc = 0)
plottitle = 'Figure 2. z vs. t for ODE with : c={:8.5f}kg/s & h={:8.5f}s' .format(c, h)
plt.title(plottitle)
plt.xlabel('t (sec)')
plt.ylabel('z (m/s)')
plotFileName = 'z-t c' + str(c) + 'h' + str(h) + '.jpg'
plt.savefig(plotFileName, format = 'jpg') # save plot in a jpg format file
plt.show() #show the plot on screen

del c, dt, h, m, k

del t, ti, tf, numberOfDataSets

del y_exact, y_ex, z_ex, y_mid, z_mid, y_rk4, z_rk4

del plottitle, plotFileName