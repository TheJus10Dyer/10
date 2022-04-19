import board
from adafruit_circuitplayground import cp
import time
from array import array
import analogio
import digitalio
import math

def derivative(x1,x2,t1,t2):
    x = (x2-x1)/(t2-t1)
    return x

def plus(x,y):
    x = x+y
    return x

def minus(x,y):
    x = x-y
    return x

def times(x,y):
    x = x*y
    return x

def divide(x,y):
    x = x/y
    return x

def exp(x,y):
    x = x**y
    return x


while True:
    x = float(input('x = '))
    enter = str(input('Function: '))
    if enter is 'help' or 'Help':
        print('List of functions: +, -, *, /, ^y')

    y = float(input('y = '))
    if enter is '+':
        out = plus(x,y)
    if enter is '-':
        out = minus(x,y)
    if enter is '*':
        out = times(x,y)
    if enter is '/':
        out = divide(x,y)
    if enter is '^y':
        enter = '^'
        out = exp(x,y)
    if enter is 'dx':
        x1 = float(input('x1 = '))
        x2 = float(input('x2 = '))
        t1 = float(input('t1 = '))
        t2 = float(input('t2 = '))
        out = derivative(x1, x2, t1, t2)
    else:
        out = 'No Function'

    print(x,enter,y,' = ',out)
