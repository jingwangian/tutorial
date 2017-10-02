#!/usr/bin/env python3

'''
combinations study

Functions:
__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__,__getattribute__
__gt__,__hash__,__init__,__iter__,__le__,__lt__,__ne__,__new__
__next__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setstate__,__sizeof__,__str__
__subclasshook__,
'''
import itertools as it

obj = it.combinations('ABCD', 2)

[print(list(it.combinations('ABCD', x))) for x in range(1, 5)]
'''
[('A',), ('B',), ('C',), ('D',)]
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
[('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
[('A', 'B', 'C', 'D')]
'''

print(list(it.combinations('ABCDE', 4)))

print(list(it.combinations_with_replacement('ABCD', 2)))
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'), ('D', 'D')]


print(list(it.combinations((1, 2, 3, 4, 5), 3)))

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(obj)
