#!/usr/bin/env python

'''
Dict subclass for counting hashable items.  Sometimes called a bag
or multiset.  Elements are stored as dictionary keys and their counts
are stored as dictionary values.

A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

print Counter(myList).keys()
[1, 2, 3, 4, 5]

print Counter(myList).values()
[3, 4, 4, 2, 1]

'''

from collections import Counter

c = Counter('abcdeabcdabcaba')  # count elements from a string

c1=c.most_common(3)                # three most common elements
print(c1)
# ---> [('a', 5), ('b', 4), ('c', 3)]
print(sorted(c))                       # list all unique elements
# ---> ['a', 'b', 'c', 'd', 'e']

print(c.items())  #--->dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 3), ('x', 1)])

c2=''.join(sorted(c.elements()))   # list elements with repetitions
print(c2)
# ---> 'aaaaabbbbcccdde'

c3=sum(c.values())                 # total of all counts
print(c3)
# ---> 15

print(c['a'])                          # count of letter 'a'
# ---> 5
for elem in 'shazam':           # update counts from an iterable
	c[elem] += 1                # by adding 1 to each element's count
print(c['a'])                          # now there are seven 'a'
# ---> 7

del c['b']                      # remove all 'b'
print(c['b'])                   # now there are zero 'b'
# ---> 0

d = Counter('simsalabim')       # make another counter
c.update(d)                     # add in the second counter
print(c['a'])                   # now there are nine 'a'
# ---> 9

c.clear()                       # empty the counter
print(c)
# ---> Counter()

'''
Note:  If a count is set to zero or reduced to zero, it will remain
in the counter until the entry is deleted or the counter is cleared:
'''

c = Counter('aaabbc')
c['b'] -= 2                     # reduce the count of 'b' by two
c4=c.most_common()                 # 'b' is still in, but its count is zero
print(c4)
# ---> [('a', 3), ('c', 1), ('b', 0)]


c1 = Counter([1,2,3,4,5,6,1,2,3])
print(c1)


c = Counter(['eggs', 'ham'])
print(c['ham'])  #--->1
del c['ham']
print(c)  # ---> Counter({'eggs': 1})
print(c['ham']) #--->0


c = Counter(a=4, b=2, c=0, d=-2, f=20)
d = Counter(a=1, b=2, c=3, d=4, e=16)
e = Counter(a=2, k=-1,hsd=2)
c.subtract(d)
print(c)  #--->Counter({'f': 20, 'a': 3, 'b': 0, 'c': -3, 'd': -6, 'e': -16})
c1=c+e
print(c1)  #--->Counter({'f': 20, 'a': 3, 'b': 0, 'c': -3, 'd': -6, 'e': -16})
e=c+d
print(sorted(c)) #--->['a', 'b', 'c', 'd', 'e', 'f']
print(c.keys())  #--->dict_keys(['a', 'b', 'c', 'd', 'f', 'e'])
print(c.values()) #--->dict_values([3, 0, -3, -6, 20, -16])
print(c.items()) #--->dict_items([('a', 3), ('b', 0), ('c', -3), ('d', -6), ('f', 20), ('e', -16)])
c['b']=2
del(c['f'])
print(list(c.elements())) #--->['a', 'a', 'a', 'b', 'b']


c = Counter(a=2, b=-4,c=1,d=-2)
c1=+c
print(c1)
c1['x']+=100
print(c1)

c1['y']='abc'
print(c1)
# Counter({'a': 2})
# Counter({'b': 4})