#!/usr/bin/env python3

'''
permutations study

Functions:
__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__,__getattribute__
__gt__,__hash__,__init__,__iter__,__le__,__lt__,__ne__,__new__
__next__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setstate__,__sizeof__,__str__
__subclasshook__,
'''
import itertools as it

obj = it.permutations('ABCD', 2)

[print(list(it.permutations('ABCD', x))) for x in range(1, 4 + 1)]

'''
[('A',), ('B',), ('C',), ('D',)]

[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]

[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'B'), ('A', 'C', 'D'), ('A', 'D', 'B'), ('A', 'D', 'C'), ('B', 'A', 'C'), ('B', 'A', 'D'), ('B', 'C', 'A'), ('B', 'C', 'D'), ('B', 'D', 'A'), ('B', 'D', 'C'), ('C', 'A', 'B'), ('C', 'A', 'D'), ('C', 'B', 'A'), ('C', 'B', 'D'), ('C', 'D', 'A'), ('C', 'D', 'B'), ('D', 'A', 'B'), ('D', 'A', 'C'), ('D', 'B', 'A'), ('D', 'B', 'C'), ('D', 'C', 'A'), ('D', 'C', 'B')]
'''

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(obj)
