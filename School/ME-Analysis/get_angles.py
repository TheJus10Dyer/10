# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 08:09:57 2022

@author: Justin
"""
import math


def get_angles(x,y,z):
    yaw = math.atan2(x, math.sqrt((y**2)+(z**2)))*180/math.pi
    pitch = math.atan2(y, math.sqrt((x**2)+(z**2)))*180/math.pi
    return yaw,pitch

yaw,pitch = get_angles(float(input('x acceleration = ')), float(input('y acceleration = ')),float(input('z acceleration = ')))

print(yaw,pitch)