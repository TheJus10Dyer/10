# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:06:08 2022

@author: Justin
"""
#HW 2 - ME 328
#Student Name: Justin Dyer
#Student J #: J00655685




#Try 1
a = 5
b = -3.6
d = '4'
print(a + b)
print(int(b))
print(b)
print(complex(a,b))
c = complex(a,b)

print('c =',c)
print(float(d))

print(int(float(d)))



#Try 2
a = -3.6
b = 3
c = 1.0
print(abs(a))
print(max([a, b, c]))
mylist = [a, b, c]
print(min(mylist))



#Try 3
a = input('input a = ')
b = eval(a)
print('a is ', a, type(a), '\n b is ', b, type(b))


c1 = 4321
c2 = 1234.56789
print('{:6d}, {:06d}, {:7.4f}, {:5.4e}' .format(c1,c1,c2,c2))



#Try 4
myfile = open('mynewfile.txt', 'w+')

for n in range(1, 5, 1):
    string_n = 'n = ' + str(n) + '\n'
    myfile.write(string_n)
myfile.close()

myfile = open('mynewfile.txt', 'r+')

dataReadFromFile = myfile.readlines()
print('original file data:', dataReadFromFile)
myfile.write('new input says n = 1000\n')
myfile.seek(0)
dataReadFromFile = myfile.readlines()
print('updated file data:', dataReadFromFile)
myfile.close()


#Try 5
def derivative(f, x, h=0.0001):
    print('calling the function derivative(f,x,h)')
    dfdx = (f(x+h) -f(x-h))/(2.0*h)
    ddfdxx = (f(x+h) - 2.0*f(x) + f(x-h))/(h**2)
    return dfdx, ddfdxx

from math import atan
c1, c2 = derivative(atan, 0.5)
print('first derivative = ', c1, '\nsecond derivative = ', c2)

c = lambda x, y: x**2 +2.0*x*y + y**2
print(c(2,4))
import math
print(dir(math))
from numpy import array

a = array([[2,-1], [-1, 3.0]], float)
print('array a =', a)

import numpy as np

b = np.zeros((3,3), float)
print(b)

b[0] = [1, 2, 3]
b[1, 2] = a[1,1] + 5
b[2, 0:2] = [8, -3]
print(b)
print(b/10.0)
print(np.diagonal(b))

A=np.array([[1,2],[3,4]])
b=np.array([[5], [6]])

print('A = ', A)
print('b = ', b)
print('transpose of b = ', b.transpose())
print('A times b = ', np.dot(A,b))
print('A inverse = ', np.linalg.inv(A))
print(np.dot(A, np.linalg.inv(A)))
print(np.linalg.solve(A,b))

c = np.array([5,6])

print(np.linalg.solve(A, c))



#Try 6
import matplotlib.pyplot as plt
from numpy import arange, sin, cos

x = arange(0.0, 6.2, 0.2)
plt.plot(x, sin(x), 'o-', x, cos(x), '^-')

plt.legend(('sine', 'cosine'), loc = 0)
plt.xlabel('x')
plt.ylabel('sin(x), cos(x)')

plt.grid(True)

plt.savefig('testplot.png', format = 'png')
plt.show()

input('\nPress return to exit')



