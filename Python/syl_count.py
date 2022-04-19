# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:30:33 2022

@author: Justin
"""

def count(x):
    count = 1
    for i in str(x):
        if i == "-":
            count = count + 1
    return count
print(count("ho-tel"))