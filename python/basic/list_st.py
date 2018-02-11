#!/usr/bin/env python3

'''
List study

Methods:
__add__,__class__,__contains__,__delattr__,__delitem__,__dir__,__doc__,__eq__
__format__,__ge__,__getattribute__,__getitem__,__gt__,__hash__,__iadd__,__imul__
__init__,__iter__,__le__,__len__,__lt__,__mul__,__ne__,__new__
__reduce__,__reduce_ex__,__repr__,__reversed__,__rmul__,__setattr__,__setitem__,__sizeof__
__str__,__subclasshook__,
append,clear,copy,count,extend,index,insert,pop,remove,reverse,sort

append: append to end
clear : remove all
copy: make a new list, shadow copy
count(object): Get the number of item in the list

extend: l1 + l2 ---> l1

index(value): return first index of value, not found raise ValueError
insert(index,object): insert object before index
pop(index): Remove and return the object at index
Remove(object): Remove first found value
sort: sorted(list) --> list
'''

l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd', 'c', 'd', 'c', 'b', 'd', 'd']

# Using count
print(l1.count('d'))  # --->0
print(l2.count('d'))  # --->4


# slice
print('l1[::2]:', l1[::2])
#-->l1[::2]: [1, 3, 5]

# del
print("l3 = l1.copy()")
l3 = l1.copy()
del l3[::2]
print('l3:', l3)
print('l1:', l1)
# *
print('l3 * 2---->', l3 * 2)

# pop
l3.pop(1)
print('l3.pop([1, 2, 3]):', l3)


# Using copy
l3 = l1.copy()
l1.append(7)
print('l1.append(7) --> ', l1)
print('l3 -->', l3)

# Using extend
l1.extend(l2)
print('l1.extend(l2)--->', l1)

# Using index, return ValueError if value is not in list
try:
    print(l1.index(1))
    print(l1.index(100))
except ValueError as e:
    print(e)

# Using insert
l1.insert(2, '20')
l1.insert(2, '20')
l1.insert(2, '20')
l1.insert(-1, '200')
print(l1)

# Using pop
print(l1.pop(-2))

# Using Remove
try:
    l1.remove('20')
    l1.remove('20')
    l1.remove('20')
    l1.remove('21')
except ValueError as e:
    print(e)
print("After rmove: {}".format(l1))

l1 = [1, 2, 3, 4, 5, 6]
l2 = ['a', 'b', 'c', 'd', 'c', 'd', 'c', 'b', 'd', 'd']
print("l1+l2={}".format(l1 + l2))
l3 = l1 + l2
[l3.remove(x) for x in l2]
print(l3)

# Using count to caculate  every number of alphabits and print it
print("# Using count to caculate  every number of alphabits and print it")
s1 = 'hello world china like topic book windows storys'
keys = set([x for x in s1])
print([(k, s1.count(k)) for k in sorted(keys)])


# def f(n):
#     return ',' if n % 8 > 0 else None
# print(dir(l1))
# [print(x, end=f(i + 1)) for i, x in (enumerate(dir(l1)))]


a = [1, 2, 3, 4, 5]
sliceObj = slice(1, 3)
print("slice(1, 3)-->", slice(1, 3))
print("a[sliceObj]--->", a[sliceObj])
