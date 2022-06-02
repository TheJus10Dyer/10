# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:07:49 2022

@author: 500308
"""

import numpy as np
from matplotlib import pyplot as plt
import time


fig, ax = plt.subplots()
#y = np.linspace()
for i in range(0,1000,1):
    print('Loading Data...')
    x = np.loadtxt('longlat.txt')
    print('Plotting',x,',',i)
    ax.plot(x,i,'b*')
    print('Updating Figure...')
    plt.savefig('here.jpg')
    #ax.clear()
    time.sleep(5)


time.sleep(2)