#!/usr/bin/env python3

'''
product study

Functions:
__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__,__getattribute__
__gt__,__hash__,__init__,__iter__,__le__,__lt__,__ne__,__new__
__next__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setstate__,__sizeof__,__str__
__subclasshook__,

'''
import itertools as it

p = it.product('ABCD', repeat=2)

# len = len(string)** repeat

[print(list(it.product('ABCD', repeat=x))) for x in range(1, 4)]
'''
[('A',), ('B',), ('C',), ('D',)]

[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]

[('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'A', 'D'), ('A', 'B', 'A'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'), ('A', 'C', 'D'), ('A', 'D', 'A'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('A', 'D', 'D'), ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'B', 'D'), ('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'B'), ('B', 'D', 'C'), ('B', 'D', 'D'), ('C', 'A', 'A'), ('C', 'A', 'B'), ('C', 'A', 'C'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'), ('C', 'B', 'D'), ('C', 'C', 'A'), ('C', 'C', 'B'), ('C', 'C', 'C'), ('C', 'C', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('C', 'D', 'C'), ('C', 'D', 'D'), ('D', 'A', 'A'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'A', 'D'), ('D', 'B', 'A'), ('D', 'B', 'B'), ('D', 'B', 'C'), ('D', 'B', 'D'), ('D', 'C', 'A'), ('D', 'C', 'B'), ('D', 'C', 'C'), ('D', 'C', 'D'), ('D', 'D', 'A'), ('D', 'D', 'B'), ('D', 'D', 'C'), ('D', 'D', 'D')]
'''

[print(len(list(it.product('ABCD', repeat=x)))) for x in range(1, 4)]

print(list(it.product('ABCD', '123', 'xyz', ['hk'])))

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(p)
