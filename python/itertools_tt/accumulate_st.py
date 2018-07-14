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
from itertools import accumulate


print(list(accumulate([1, 2, 3, 4, 5])))  # - - > 1 3 6 10 15

[print(x, end=' ') for x in accumulate([1, 2, 3, 4, 5])]
print(' ')

print(list(accumulate([1, 2, 3, 4, 5], lambda x, y: x + y + 100)))  # - - > 1 3 6 10 15
'''
1   1
1,2 x+y+100 = 1+2+100 = 103
1,2,3 103+3+100 = 206
'''

print(list(accumulate([100, 50, 30, 20, 10], lambda x, y: x - y)))  # - - > [100, 50, 20, 0, -10]

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(obj)
print('it.chain:')
print(list(it.chain(['a', 'b', 'c'], [1, 2, 3], ['c', 'd', 'e', 'f'])))


print(list(it.compress(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], [1, 2, 3, 0, -1, 'a', '', None])))
# ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i']
# [ 1,   2,   3,   0,   -1, 'a',  '', None]
# ['a', 'b', 'c',      'e', 'f']


print([(k, len(list(g))) for k, g in it.groupby('AAAABBBCCDAABBB')])
print([list(g) for k, g in it.groupby('AAAABBBCCDAABBB')])
