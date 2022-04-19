# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:53:30 2022

@author: Justin
"""

import numpy as np
import matplotlib.pyplot as plt

Vin = 1.28
Vup = 5
Vlow = 0
bits = np.array([4,8,16,32])
error_hand = np.array([2.34375,0.703125,0.0015625,0])

print('Input voltage = ', Vin)
print('Voltage range = ', Vlow,'-',Vup,'V')

digitalout = []
for i in [4,8,16,32]:
    out = np.trunc((Vin-Vlow)/((Vup-Vlow)/(2**i)))
    digitalout.append(out)
    print('Digital Output of', i, 'bit: ', out)
    

count = 0
Vreversed = []
for i in [4,8,16,32]:
    if count == 0:
        count = 0
    Vrev = (digitalout[count]*((Vup-Vlow)/2**i))+Vlow
    count = count + 1
    Vreversed.append(Vrev)
    print('Digital signal converted to voltage of',i,'bit: ', Vrev, 'V')

error = []
count = 0
for i in Vreversed:
    e = ((Vin-i)/Vin)*100
    error.append(e)
    print('Error of ',bits[count], 'bit: ', e,'%')
    count = count+1


plt.plot(bits,error_hand,'r-', label= 'Hand Computed')
plt.plot(bits,error,'b-',label= 'Python Computed')
plt.xlabel('N (number of bits)')
plt.ylabel('%error from actual value')
plt.title('Error as function of bits')
plt.legend()
plt.grid()
plt.show()