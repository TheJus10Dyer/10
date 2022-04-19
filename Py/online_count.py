# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:17:18 2022

@author: Justin
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(x):
    output = 0
    for key in x:
        if x[key] == "online":
            output = output + 1
        else:
            pass
    return output

print(online_count(statuses))