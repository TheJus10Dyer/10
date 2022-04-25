# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:02:04 2022

@author: Justin
"""

class Person:
    def __init__(self,fname):
        self.firstname = fname
        
    def printname(self):
        print(self.firstname)

class Student(Person):
    pass

x = Student('Justin')
x.printname()

