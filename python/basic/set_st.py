#!/usr/bin/env python3

'''
Set study

set:
frozenset: imutable set, can be used hashvalue as dict key or value of the set

Methods:
__and__,__class__,__contains__,__delattr__,__dir__,__doc__,__eq__,__format__
__ge__,__getattribute__,__gt__,__hash__,__iand__,__init__,__ior__,__isub__
__iter__,__ixor__,__le__,__len__,__lt__,__ne__,__new__,__or__
__rand__,__reduce__,__reduce_ex__,__repr__,__ror__,__rsub__,__rxor__,__setattr__
__sizeof__,__str__,__sub__,__subclasshook__,__xor__,
add,clear,copy,difference,difference_update,discard,intersection,
intersection_update,isdisjoint,issubset,issuperset,pop,remove,symmetric_difference,
symmetric_difference_update,union,update,

isdisjoint: Return True if intersection is the empty set.
issubset: subset
issuperset: superset
intersection: common part in s1 and s2
symmetric_difference: s1^s2
remove(elem):
discard(elem)
pop(): Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
clear(): Remove all

'''


s1 = set([1, 2, 3, 4, 5])
s1_b = set([2, 1, 3, 4, 5])
s2 = set([2, 9, 8, 7, 4])
s4 = set()
fs1 = frozenset(s1)
fs2 = frozenset(s2)
print('fs1:', fs1)

# frozenset can be used value as dict key or value of set
s4.add(fs1)
s4.add(fs2)
print('s4:', s4)
print('s4 len:', len(s4))

# [s1.add(x) for x in [1, 2, 3, 4]]

print('s1:{}'.format(s1))
print('s1_b:{}'.format(s1_b))
print('s2:{}'.format(s2))


print('s1 == s1_b : {}'.format(s1 == s1_b))
print('s1 == fs1:', s1 == fs1)

d1 = dict()
d1[fs1] = 1

if fs1 in d1:
    print('fs1 in d1')


# Using difference
print('s1.difference(s2):', s1.difference(s2))
print('s2.difference(s1):', s2.difference(s1))

# symmetric_difference
print('s1.symmetric_difference(s2):', s1.symmetric_difference(s2))

# Using difference update
s3 = s1.copy()

print('s3:{}'.format(s3))
print('s3.issubset(s1)', s3.issubset(s1))
print('s3.issuperset(s1)', s3.issuperset(s1))
print('s3 > s1', s3 > s1)
s3.difference_update(s2)
print(s1, s3)

# Union
print('s1.union(s2)--->', s1.union(s2))

# Intersection
print('s1.intersection(s2)--->', s1.intersection(s2))


# Using Discard
s3.discard(3)
print(s3)


a = set('abracadabra')
b = set('alacazam')
c = set('xyz')

print('a - b : ', a - b)
print('b - a : ', b - a)
print('a & b : ', a & b)
print('a | b : ', a | b)
print('a ^ b : ', a ^ b)

print('a & c: ', a & c)

s1 = set('abcde')
s1.remove('b')
print(s1)
# def f(n):
#     return ',' if n % 8 > 0 else None
# # print(dir(d1))
# [print(x, end=f(i + 1)) for i, x in (enumerate(dir(set())))]
