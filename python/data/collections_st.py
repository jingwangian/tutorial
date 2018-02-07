#!/usr/bin/env python3

'''
collections study:

Object:
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

import os.path
from collections import Counter
from collections import deque
from collections import OrderedDict

c = Counter(a=3, b=1, c=20, f=100)
d = Counter(a=1, b=2, c=10)
e = Counter(a=10, b=20, c=30)
print(c + d + e)                       # add two counters together:  c[x] + d[x]
f = Counter({'a': 4, 'b': 3})
print(f['a'])
print(c - d)                       # subtract (keeping only positive counts)
Counter({'a': 2})
print("c & d --->", c & d)                       # intersection:  min(c[x], d[x])

print("c & d & e --->", c & d & e)

Counter({'a': 1, 'b': 1})
print("c | d | e --->", c | d | e)                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})

print(c['a'])


d = deque('cdefabx')
d.append('y')
d.appendleft('a')
print(d)
[print(e, end='-') for e in d]
print('')


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


d1 = OrderedDict([('c', 1), ('d', 2), ('a', 10)])
print(d1)
[print(x, d1[x]) for x in d1]
# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
# printkey(os.path)
