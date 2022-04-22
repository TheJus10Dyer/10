"""
Created on Mon Feb 22 15:34:21 2022

ME 328 Project 2
by Justin Dyer
J00655685

"""

x = []
y = []
z = []
A = []

numOfDataPointsRead = 0

inputfile = open('cross-section-input.txt', 'r')

for line in inputfile:
    numOfDataPointsRead += 1
    x.append(eval(line.split(',' or '')[0]))
    y.append(eval(line.split(',' or '')[1]))
    z.append(eval(line.split(',' or '')[2]))
    A.append(eval(line.split(',' or '')[3]))

inputfile.close()

print('numOfDataPointsRead = ', numOfDataPointsRead)
print('x = ',x)
print('y = ',y)
print('z = ',z)
print('A = ',A)

h = x[1]-x[0]
print('h = ',h)

V = A[0]
xCB = x[0]*A[0]
yCB = y[0]*A[0]
zCB = z[0]*A[0]

for i in range(1,(numOfDataPointsRead),1):
    c = 2.0
    if i == numOfDataPointsRead - 1:
        c = 1.0
    V = V + c*A[i]
    xCB = xCB + c*x[i]*A[i]
    yCB = yCB + c*y[i]*A[i]
    zCB = zCB + c*z[i]*A[i]

V = V * h *0.5
xCB = xCB * h * 0.5
yCB = yCB * h * 0.5
zCB = zCB * h * 0.5
xCB = xCB/V
yCB = yCB/V
zCB = zCB/V

print('x_CB = ', xCB)
print('y_CB = ', yCB)
print('z_CB = ', zCB)
print('V = ', V)

outputfile = open('buoyancy-summary.txt', 'w')
outputfile.write('{:10.4f}, {:10.4f}, {:10.4f}, {:10.4f}' .format(xCB, yCB, zCB, V))
outputfile.close()