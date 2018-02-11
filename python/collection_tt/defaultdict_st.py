#!/usr/bin/env python3


'''
Object : defaultdict

defaultdict:  No need key is there or not


'''

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# Create a dict with value type being list
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


s = [('red', 1), ('blue', 2), ('yellow', 12), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4), ('yellow', 2, 3, 5)]
d = defaultdict(list)
for x in s:
    k = x[0]
    v = (x[1:])
    d[k].extend(v)
print(d.items())
