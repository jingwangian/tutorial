#!/usr/bin/env python3

'''
Methods:
    add :
    clear: Remove all elements from the set.
    copy:
    difference: Return a new set with elements in the set that are not in the others.
    difference_update:
    discard:
    intersection: Return a new set with elements common to the set and all others.
    intersection_update: Update the set, keeping only elements found in it and all others.
    isdisjoint: Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.
    issubset:
    issuperset:
    pop: Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
    remove: Remove element elem from the set. Raises KeyError if elem is not contained in the set.
    symmetric_difference: Return a new set with elements in either the set or other but not both.
    symmetric_difference_update:
    union: Return a new set with elements from the set and all others.
    update:
'''

s1 = {'A', 'B', 'D', 'E', 'G', 'Z', 'X'}
s2 = {'C', 'E', 'X', 'F', 'B'}
s3 = {'G', 'D', 'B'}
s4 = {'C', 'P', 'M'}
print(s1)
print(s2)


print('intersection:', s1.intersection(s2))
print('intersection:', s1.intersection(s4))

# s1.intersection_update(s2)
# print('s1.intersection_update(s2)', s1, s2)

print('isdisjoint:', s1.isdisjoint(s2))
print('isdisjoint:', s1.isdisjoint(s4))

print('issubset', s3.issubset(s1))

print('difference', s1.difference(s2))
print('symmetric_difference', s1.symmetric_difference(s2))

s1.update(s2)
print('s1.update(s2):', s1, s2)

l1 = [x for x in 'abcdef']
l2 = [x for x in 'dgae']
print(set(l1).intersection(l2))
rt = set('abc').intersection('cbs')
print(type(rt))
