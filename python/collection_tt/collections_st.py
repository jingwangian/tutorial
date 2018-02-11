#!/usr/bin/env python3


'''
Module : Collections

Main sub-modules
defaultdict, OrderedDict, counter, deque, namedtuple, enum.Enum

defaultdict:  No need key is there or not

namedtuple()    factory function for creating tuple subclasses with named fields
deque   list-like container with fast appends and pops on either end
ChainMap    dict-like class for creating a single view of multiple mappings
Counter     dict subclass for counting hashable objects
OrderedDict     dict subclass that remembers the order entries were added
defaultdict     dict subclass that calls a factory function to supply missing values
UserDict    wrapper around dictionary objects for easier dict subclassing
UserList    wrapper around list objects for easier list subclassing
UserString  wrapper around string objects for easier string subclassing

'''

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = defaultdict(list)

[d[k].append(v) for k, v in s]

print(d.items())

# defaultdict is used to counting
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())

# Setting the default_factory to set makes the defaultdict useful for building a dictionary of sets:
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
[d[k].add(v) for k, v in s]
print(d.items())


s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4), ('yellow', 2, 3, 5)]
d1 = dict()
for x in s:
    k = x[0]
    v = (x[1:])
    if k in d1.keys()
