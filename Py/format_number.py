# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:29:37 2022

@author: Justin
"""

def format_number(x):
    if x < 0:
        raise TypeError("Parameter must be positive.")
    if type(x) is not int:
        raise TypeError("Parameter must be an integer.")
    count = 0
    output = 'sum'
    for i in str(x):
        if count == 0:
            output = i
        length = len(str(x)) - count
        if ((length)%3) == 0:
            if count > 0:
                output = output + ","
        if count > 0:
            output = output + i
        count = count + 1
    return output
print(format_number(100))