# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:53:37 2022

@author: Justin
"""

def mid(x):
    length = len(x)
    midpoint = 0.5*length
    count = 0.5
    for i in str(x):
        if count == midpoint:
            output = str(i)
            pass
        count = count + 1
    if length%2 ==0:
        output = ""
    return output