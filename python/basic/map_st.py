#!/usr/bin/env python3

'''
map,reduce,filter study:

'''

from functools import reduce

l1 = [1, 2, 3, 4, 5, 6, 7]

[print(t, end=' ') for t in map(lambda x: x * 2, l1)]

print('')

[print(t, end=' ') for t in filter(lambda x: x >= 5, l1)]
print('')

print('reduce result for list:', l1)
print(reduce(lambda x, y: x + y, l1))
print(reduce(lambda x, y: '{}_{}'.format(x, y), l1))
# print(help(reduce))

b = bytearray([1, 2, 3, 4])
print(b)
[print(oct(x)) for x in b]

y = l1[0]


total = 0
for x in l1:
    total = x + total
    print(total, end=' ')
    print(total)


s1 = set('abdefafd')
s2 = set('fdsfaf')
s3 = set('dxgefk')

fs = s1&s2&s3
print(fs)

