# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:03:11 2022

@author: Justin
"""


import math


def y_exact_solution (t) :
    t2=0.0866025*t
    y_exact_solution = math.exp(-0.05*t) * (0.2*math.cos(t2) + 0.11547*math.sin(t2));
    return y_exact_solution

def derives (y,z,t,m,c,k) :
    dy_over_dt = z
    dz_over_dt = -c/m*z-k/m*y
    return dy_over_dt, dz_over_dt

def explicit_euler(y,z,t,h,m,c,k) :
    dy_over_dt,dz_over_dt = derives(y,z,t,m,c,k)
    y_iplus1 = y+dy_over_dt*h
    z_iplus1 = z+dz_over_dt*h
    return y_iplus1, z_iplus1

def midpoint(y,z,t,h,m,c,k) :
    dy_over_dt,dz_over_dt = derives(y,z,t,m,c,k)
    y_mid=y+dy_over_dt*0.5*h
    z_mid=z+dz_over_dt*0.5*h
    dy_over_dt,dz_over_dt = derives(y_mid,z_mid,t,m,c,k)
    y_iplus1=y+dy_over_dt*h
    z_iplus1=z+dz_over_dt*h
    return y_iplus1, z_iplus1

def RK4(y,z,t,h,m,c,k) :
    y_iplus1 = 0
    z_iplus1 = 0
    dy_over_dt=0
    dz_over_dt=0
    
    dy_over_dt, dz_over_dt = derives(y,z,t,m,c,k)
    k1y=dy_over_dt
    k1z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derives(y+k1y*h/2,z+k1z*h/2,t+h/2,m,c,k)
    k2y=dy_over_dt
    k2z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derives(y+k2y*h/2,z+k2z*h/2,t+h/2,m,c,k)
    k3y=dy_over_dt
    k3z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derives(y+k3y*h, z+k3z*h,t+h,m,c,k)
    k4y=dy_over_dt
    k4z=dz_over_dt
    
    y_iplus1 = y+(k1y+2*k2y+2*k3y+k4y)*h/6;
    z_iplus1 = z+(k1z+2*k2z+2*k3z+k4z)*h/6;
    
    return y_iplus1, z_iplus1
