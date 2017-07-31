#!/usr/bin/env python3

'''
max and min study

Functions:
__call__,__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__
__getattribute__,__gt__,__hash__,__init__,__le__,__lt__,__module__,__name__
__ne__,__new__,__qualname__,__reduce__,__reduce_ex__,__repr__,__self__,__setattr__
__sizeof__,__str__,__subclasshook__,__text_signature__,
'''


print([1, 2, 3] == [1, 3, 2])
print([1, 2, 3] == [1, 2, 3])
print((1, 2, 3) == (1, 3, 2))
print((1, 2, 3) == (1, 2, 3))
print({1, 2, 3} == {1, 3, 2})
print({1, 2, 3} == {1, 2, 3})

print(max([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(min([1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]))
print(max((1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5)))
print(min((1, 2, 3), (1, 2, 3, 4), (1, 2, 3, 4, 5)))
print(max({1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4, 5}))
print(min({1, 2, 3}, {1, 2, 3, 4}, {1, 2, 3, 4, 5}))

print(max([1, 2, 3, 4]))
print(max((1, 2, 3, 4, 5)))
print(max({1, 2, 3, 4, 5, 6}))


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(max)
# print(help(max))
