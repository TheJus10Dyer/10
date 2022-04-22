# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:55:46 2022

@author: Justin
"""
##PROJ4 FUNCTIONS
import math
import numpy as np


def LiebmannM(T_old, relax_factor, i,j):
    T_new_i_j = (T_old[i+1][j] + T_old[i-1][j] + T_old[i][j+1] + T_old[i][j-1])/4.0
    T_new_i_j = relax_factor*T_new_i_j + (1-relax_factor)*T_old[i][j]
    if T_new_i_j != 0:
        es_i_j = abs((T_new_i_j-T_old[i][j])/T_new_i_j)
    elif T_old[i][j] !=0:
        es_i_j = abs((T_new_i_j-T_old[i][j])/T_old[i][j])
    else:
        es_i_j = 1.0;
        
    return T_new_i_j,es_i_j

def heatFlux(T, kp, dx, dy):
    m = len(T)
    m=m-1
    n = len(T[0])
    n=n-1
    
    qx = np.zeros((m+1,n+1), dtype = float)
    qy = np.zeros((m+1,n+1), dtype = float)
    
    for i in range(1, m, 1):
        for j in range(1, n, 1):
            qx[i][j] = -kp*( T[i+1][j] - T[i-1][j] )/(2*dx)
            qy[i][j] = -kp*( T[i][j+1] - T[i][j-1] )/(2*dy)
            
    i = 0
    for j in range(1, n, 1):
        T_0_j = 4*T[i,j]-(T[i+1][j]+T[i][j+1]+T[i][j-1]);
        qx[i][j] = -kp*(T[i+1][j]-T_0_j)/(2*dx);
        qy[i][j] = -kp*(T[i][j+1]-T[i][j-1])/(2*dy);
    
    i = m;
    for j in range(1, n, 1):
        T_mplus2_j = 4*T[i][j]-(T[i-1][j]+T[i][j+1]+T[i][j-1]);
        qx[i][j] = -kp*(T_mplus2_j-T[i-1][j])/(2*dx);
        qy[i][j] = -kp*(T[i][j+1]-T[i][j-1])/(2*dy);

    j = 0
    for i in range(1, m, 1):
        T_i_0 = 4*T[i][j]-(T[i+1][j]+T[i-1][j]+T[i][j+1]);
        qx[i][j] = -kp*(T[i+1][j]-T[i-1][j])/(2*dx);
        qy[i][j] = -kp*(T[i][j+1]-T_i_0)/(2*dy);
    
    j = n
    for i in range(1, m, 1):
        T_i_nplus2 = 4*T[i][j]-(T[i+1][j]+T[i-1][j]+T[i][j-1]);
        qx[i][j] = -kp*(T[i+1][j]-T[i-1][j])/(2*dx);
        qy[i][j] = -kp*(T_i_nplus2-T[i][j-1])/(2*dy);
    
    return qx,qy

def y_exact_solution(t):
    t2=0.0866025*t
    y_exact_solution = math.exp(-0.05*t)*(0.2*math.cos(t2)+0.11547*math.sin(t2));
    return y_exact_solution

def derivs(y,z,t,m,c,k):
    dy_over_dt = z
    dz_over_dt = -c/m*z-k/m*y
    return dy_over_dt, dz_over_dt

def explicit_euler(y,z,t,h,m,c,k):
    dy_over_dt,dz_over_dt = derivs(y,z,t,h,m,c,k)
    y_iplus1 = y+dy_over_dt*h
    z_iplus1 = z+dz_over_dt*h
    return y_iplus1, z_iplus1

def midpoint(y,z,t,h,m,c,k):
    dy_over_dt,dz_over_dt = derivs(y,z,t,m,c,k)
    y_mid=y+dy_over_dt*0.5*h
    z_mid=z+dz_over_dt*0.5*h
    dy_over_dt,dz_over_dt = derivs(y_mid,z_mid,t,m,c,k)
    y_iplus1=y+dy_over_dt*h
    z_iplus1=z+dz_over_dt*h
    return y_iplus1, z_iplus1

def RK4(y,z,t,h,m,c,k):
    y_iplus1 = 0
    z_iplus1 = 0
    dy_over_dt=0
    dz_over_dt=0
    
    dy_over_dt, dz_over_dt = derivs(y,z,t,h,m,c,k)
    k1y=dy_over_dt
    k1z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derivs(y+k1y*h/2, z+k1z*h/2, t+h/2, m,c,k)
    k2y=dy_over_dt
    k2z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derivs(y+k2y*h/2, z+k2z*h/2, t+h/2, m,c,k)
    k3y=dy_over_dt
    k3z=dz_over_dt
    
    dy_over_dt, dz_over_dt = derivs(y+k3y*h, z+k3z*h, t+h, m,c,k)
    k4y=dy_over_dt
    k4z=dz_over_dt
    
    y_iplus1 = y+(k1y+2*k2y+2*k3y+k4y)*h/6;
    z_iplus1 = z+(k1z+2*k2z+2*k3z+k4z)*h/6;
    
    return y_iplus1, z_iplus1