# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:56:25 2022

@author: Justin
"""

##PROJ4 SOLUTION
import math
import numpy as np
import matplotlib.pyplot as plt

import project_4_functions as f
print('Project 4. Liebmann (Gauss-Siedel) Method for solving PDE.\n')

dx=float(input('input dx : ')) 
dy=dx
flag_Part_B = input('is this for Part B question (Y/N)? :')
es= 0.01
max_iter=1000
relax_factor= 1.5

kp=0.49
L=40
W=40

qy_buttom = -5.0

m=int(math.floor(L/dx))
n=int(math.floor(W/dy))


T= np.zeros((m+1, n+1), dtype = float)
ea = np.zeros((m+1, n+1), dtype = float)
e = 1.0
count = 0

for nj  in range(0, n+1, 1):
    T[0][nj] = 100.0;
    
if flag_Part_B != 'Y' or flag_Part_B != 'y':
    for mi in range(0, m+1,1):
        T[mi][0]= 0.0
        
for mi in range(0, m+1, 1):
    T[mi][n] = 150.0;
    
while (e > es and count < max_iter):
    e=0
    
    for i in range(1, m, 1):
        if flag_Part_B =='Y' or flag_Part_B == 'y':
            for mi in range(1, m, 1):
                T[mi][0]= 0.25*(T[mi+1][0]+T[mi-1][0]+2*T[mi][0+1]-2*dy*(-qy_buttom/kp))
                
        for j in range(1, n, 1):
            [T_new_i_j,es_i_j] = f.LiebmannM(T, relax_factor, i, j);
            T[i][j]=T_new_i_j;
            ea[i][j]=es_i_j;
            e=e+es_i_j;
            
    count = count + 1;
    iteration = count
    e = e/((m)*(n))
    print('e = ', e)
    
x = np.linspace(0, L, m+1)
y = np.linspace(0, W, n+1)
fig1 = plt.figure(1)
fig1.set_figheight(5.0)
fig1.set_figwidth(5.0)
plt.xlim(-10, L+10)
plt.ylim(-10, W+10)
[X, Y] = np.meshgrid(x,y) 
plt.contour(X.transpose(), Y.transpose(), T, 40)
[qx,qy] = f.heatFlux(T, kp, dx, dy);
plt.quiver(X.transpose(), Y.transpose(),qx,qy)

fig1.show()
plotFileName = 'contours_and_flux_plot' + '.jpg'
plt.savefig(plotFileName, format = 'jpg')
