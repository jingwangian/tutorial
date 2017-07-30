#!/usr/bin/env python3

'''
List study

Methods:
__class__,__contains__,__delattr__,__delitem__,__dir__,__doc__,__eq__,__format__
__ge__,__getattribute__,__getitem__,__gt__,__hash__,__init__,__iter__,__le__
__len__,__lt__,__ne__,__new__,__reduce__,__reduce_ex__,__repr__,__setattr__
__setitem__,__sizeof__,__str__,__subclasshook__,
clear,copy,fromkeys,get,items,keys,pop,popitem,setdefault,update,values,

clear: Remove all items from the dictionary.
copy: Return a shallow copy of the dictionary.
get(key,default): Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
items: Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.
len(d): Return the number of items in the dictionary d.
key in d : Return True if d has a key key, else False.
del d[key]: Remove d[key] from d. Raises a KeyError if key is not in the map.
iter(d): Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).
get(key[, default]): Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
pop(key[, default]): If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.
popitem(): Remove and return an arbitrary (key, value) pair from the dictionary.  If the dictionary is empty, calling popitem() raises a KeyError.
setdefault(key[, default]): If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

update([other]):  Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None. d.update(red=1, blue=2).

values(): Return a new view of the dictionary’s values.
'''

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# Using items
print(a.items())
print(tuple(a.items()))
print(list(a.items()))

# Using iter
print([x for x in iter(a)])

# Using get and return default value
print(a.get('bb', 'none'))
print(a.setdefault('four', 100))
print(a)

# def f(n):
#     return ',' if n % 8 > 0 else None
# # print(dir(d1))
# [print(x, end=f(i + 1)) for i, x in (enumerate(dir(d1)))]


print('zip:', list(zip('abcd', '1234', 'xyz')))

x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))
print(list(zip(zip(x, y), ('a', 'b'))))
f = dict((zip(zip(x, y), ('a', 'b'))))
print(f)
f1 = dict([((1, 4), 'a'), ('b', (2, 5))])
print(f1)
print(sorted([((1, 4), 'a'), ((2, 5), 'b')]))
