# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt
#from matplotlib.animation import FuncAnimation

data = np.loadtxt('test.txt')
x = data[:,1]
y = data[:,0]

fig, ax = plt.subplots()

#aaa = "LONG,LAT"
aaalong = -88.089443
aaalat = 30.526738

aablong = -88.089977
aablat = 30.526768

aaclong = -88.090373
aaclat = 30.527313

aadlong = -88.089855
aadlat = 30.527877

aaelong = -88.089477
aaelat = 30.528374



plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
im = plt.imread("sat.jpg")
im2 = plt.imread("akerlogo.PNG")
im3 = plt.imread("nsew.PNG")
plt.xlim(-88.094431,-88.087216)
plt.ylim(30.526135,30.529811)
im = ax.imshow(im, extent=[-88.094431,-88.087216, 30.526135,30.529811])
im2 = ax.imshow(im2, extent=[-88.093639, -88.091869, 30.529221, 30.529443])
im3 = ax.imshow(im3, extent=[-88.088019, -88.087493, 30.526259, 30.526885])
plt.plot(aaalong,aaalat,'r,',marker =r'$CSL1$',markersize = 25,label = 'CSL1')
plt.plot(aablong,aablat,'r,',marker =r'$CSL2$',markersize = 25,label = 'CSL2')
plt.plot(aaclong,aaclat,'r,',marker =r'$CSL3$',markersize = 25,label = 'CSL3')
plt.plot(aadlong,aadlat,'r,',marker =r'$CSL4$',markersize = 25,label = 'CSL4')
plt.plot(aaelong,aaelat,'r,',marker =r'$CSL5$',markersize = 25,label = 'CSL5')
plt.axis('on')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
fig.set_facecolor('grey')
plt.show()
plt.savefig('maps.jpeg')