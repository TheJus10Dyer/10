# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:23:21 2022

@author: Justin
"""
#HW 1- introduction of Python
#Student name: Justin Dyer
#Student J number: J00655685


#try 1
b=2
print(b)
b=b*2.0
print(b)


#try 2
string1 = 'press return to exit'
print(string1[0] + string1[2])
string2 = 'the program'
print(string1 + ' ' + string2)
print(string1[0:12])
string3 = '0123456789'
print(string3[6:8])
s = 'Python is an easy programming language'
print(s.split())
print(s.split()[0], s.split()[3], s.split()[1])


#try 3
rec=('Smith', 'John', [6,23,1968])
lastName, firstName, birthDate = rec
print('First Name: ' + firstName)
print('Last Name: ' + lastName)
print(birthDate[2])
print(birthDate[0] + birthDate[1] + birthDate[2])
print(rec[0:2])
print(rec[0:3])


#try 4
a= [1.0, 2.0, 3.0]
a.append(4.0)
print(a)
a.insert(0, 0.0)
print(a)
print(len(a))
a[2:4] = [1.2, 'Cat', 1.3, 1.4, 1.5]
print(a)
print(len(a))


#try 5
a= [1.0, 2.0, 3.0]
b = a
b[0] = 5.0
print(a)

c=a[:]
c[0]=10.0
print(a)


#try 6
a=[[1, 2, 3], \
   [4, 5, 6], \
   [7, 8, 9]]
print(a)
print(a[0])
print(a[1][2])


#try 7
s='Hello '
t='to you'
a=[1, 2, 3]
print(3*s)
print(3*a)
print(a +[4, 5])
print(s+t)


#try 8
[a, b, c] = [2, 1.99, '2']
print(a>b)
print(a == c)
print((a > b) and (a != c))
print((a > b) or (a == b))


#try 9
def sign_of_number(a):
    if a < 0.0:
        sign = 'negative'
    elif a > 0.0:
        sign = 'positive'
    else:
        sign = 'zero'
    return sign

b=1.5
print('b is ' + sign_of_number(b))


#try 10
nMax = 5
n = 1
a = []
while n < nMax:
    a.append(1.0/n)
    n = n + 1
    print('block end n = ', n)
print(a)


nMax = 5
a=[]
for n in range(1, nMax):
    a.append(1.0/n)
    print('n =', n)
print(a)


list = ['Jack', 'Jill', 'Tim', 'Dave']
name = eval(input('Type a name: '))
for i in range(len(list)):
    if list[i] == name:
        print(name, 'is number', i+1, 'on the list')
        break
else:
    print(name, 'is not on the list')


x = []
for i in range(1, 100):
    if i%7 != 0: continue
    x.append(i)
print('these numbers are divisible by 7: ', x)


print('END of HW 1')


    