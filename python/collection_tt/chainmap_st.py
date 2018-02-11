#!/usr/bin/env python3


'''
Object : ChainMap

'''
import builtins

from collections import ChainMap

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

combined = ChainMap([1, 2, 3], ['a', 'b', 'c', 'd'], [333, 444, 555, 666, 777, 888])

print("combined--->", combined)
print(type(combined))
print(dir(combined))
# print(list(combined).sort(key=lambda x: (x)))

[print(x, end=' ') for x in combined]


# print(dir('a'))
# print(vars(builtins))

# print(help(vars))
