#!/usr/bin/env python3

'''
groupby

Functions:
__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__,__getattribute__
__gt__,__hash__,__init__,__iter__,__le__,__lt__,__ne__,__new__
__next__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setstate__,__sizeof__,__str__
__subclasshook__,

'''
import sys
import itertools as it
from itertools import groupby

iter1 = iter(range(1, 11))
t1 = it.tee(iter1)

print(list(t1))

[print(x) for x in t1[0]]

[print(x) for x in t1[1]]
