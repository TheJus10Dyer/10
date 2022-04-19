# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:40:17 2022

@author: Justin
"""
import numpy as np
def is_anagram(x,y):
    if sorted(x) == sorted(y):
        lis = True
    else:
        lis = False   
    return lis

print(is_anagram('acb', "abc"))