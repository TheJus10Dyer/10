"""
Created on Tue Apr 19 14:06:17 2022

@author: Justin
"""

##Instrumentation Assesment 2 Problem 2

##Import needed modules
import numpy as np
import matplotlib.pyplot as plt

#Load data
data = np.loadtxt('INSTtest2problem2data.txt')

#Assign variables to data
MAGX = data[:,0]
MAGY = data[:,1]
MAGZ = data[:,2]

#Define function to answer part 2
def get_solution(x,y):
    print('Mean of ',y, 'data = ',np.mean(x))
    print('Standard Deviation of ',y, 'data = ',np.std(x))
    
#Get solution to part 2
get_solution(MAGX, 'x - axis')
get_solution(MAGY, 'y - axis')
get_solution(MAGZ, 'z - axis')

#Satisfy part 1 by plotting histograms
#X-axis Histogram
plt.figure()
plt.hist(MAGX)
plt.title('Magnetometer x-axis Histogram')
plt.xlabel('Value')
plt.ylabel('Number of Occurances')
plt.grid()

#Y-axis Histogram
plt.figure()
plt.hist(MAGY)
plt.title('Magnetometer y-axis Histogram')
plt.xlabel('Value')
plt.ylabel('Number of Occurances')
plt.grid()

#Z-axis Histogram
plt.figure()
plt.hist(MAGZ)
plt.title('Magnetometer z-axis Histogram')
plt.xlabel('Value')
plt.ylabel('Number of Occurances')
plt.grid()

#Show plots
plt.show()