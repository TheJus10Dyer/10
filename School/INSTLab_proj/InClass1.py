# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:28:03 2022

@author: Justin
"""



import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':14})

x = np.linspace(0,5.0,100)

y = 200*np.cos(2.0*x+0.5)



plt.plot(x,y,'g-',linewidth=2)
plt.grid()
plt.xlabel('Cool')
plt.ylabel('Bananas')
plt.title('Fruits')


plt.show()
