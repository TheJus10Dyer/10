# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:15:16 2022

@author: Justin
"""

def list_xor(n,list1,list2):
    count = 0
    output = False
    for i in list1:
        if i == n:
            count = count + 1
            break
    for i in list2:
        if i == n:
            count = count + 1 
            break
    if count >= 2:
        output = False
    if count == 1:
        output = True
    if count == 0:
        output = False
    return output
print(list_xor(5, [5, 5, 5], [4, 4, 4]))