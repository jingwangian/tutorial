#!/usr/bin/env python3

'''
map,reduce,filter study:

'''

from functools import reduce

l1 = [1, 2, 3, 4, 5, 6, 7]

[print(t) for t in map(lambda x: x * 2, l1)]

[print(t) for t in filter(lambda x: x >= 5, l1)]


print('reduce')
print(reduce(lambda x, y: x + y, l1))
print(reduce(lambda x, y: '{}_{}'.format(x, y), l1))
print(help(reduce))

b = bytearray([1, 2, 3, 4])
print(b)
[print(oct(x)) for x in b]
[print(x) for x in b]
