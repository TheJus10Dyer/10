# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:45:27 2022

@author: Justin
"""

def only_ints(x,y):
    if type(x) is int:
        output = False
        if type(y) is int:
            output = True
    else:
        output = False
    return output

print(only_ints("a", 1))