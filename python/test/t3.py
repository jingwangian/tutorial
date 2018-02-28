#!/usr/bin/env python3


import sys

class Student:
    # name = 'abc'
    def __init__(self,name):
        self._name = name
    def __repr__(self):
        return repr(self.name)

    def __str__(self):
        return str(self.name)

    @property
    def name(self):
        print('getter is invoked')
        return self._name

    @name.setter
    def name(self,value):
        print('setter is invoked')
        self._name = value

    @name.deleter
    def name(self):
        print('deleter is invoked')
        del self._name

s1 = Student('wang\njing')

print(s1)
print(repr(s1))
x1 = str(s1)
x2 = repr(s1)

print(list(x1))
print(list(x2))

del s1.name

s1.name='wang\nlin'
print(s1)

st1 = set([1,2,3,12,3,5,5,6,7])
print(st1)

st2 = set('hello world')
print(st2)
