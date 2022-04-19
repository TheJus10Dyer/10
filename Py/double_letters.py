# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:54:50 2022

@author: Justin
"""

def double_letters(x):
    count = 0
    output = False
    for i in str(x):
        if count == 0:
            y = 0
            count = count + 1
        if i is not y:
            output = False
        else:
            output = True
            return output
        y = i
    return output
print(double_letters("hell"))            