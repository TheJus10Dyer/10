# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:42:37 2022

@author: Justin
"""
x = "HelLO"
def capital_indexes(x):
    count = 0
    output = list()
    for i in str(x):
        if (i.isupper()) == True:
            output.append(count)
            count = count + 1
        else:
            count = count + 1
            pass
    return output
print(capital_indexes("HeLlO"))
