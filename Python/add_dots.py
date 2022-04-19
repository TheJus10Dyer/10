# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:34:00 2022

@author: Justin
"""

def add_dots(x):
    count = 1
    for i in str(x):
        if count == 1:
            output = i + "."
        if count == len(str(x)):
            output = output + i
            break
        if count >1:
            output = output + i +"."
        count = count + 1
    if len(x) == 1:
        output = x
    return output

def remove_dots(x):
    output = x.replace(".", "")
    return output
print("ab")
        