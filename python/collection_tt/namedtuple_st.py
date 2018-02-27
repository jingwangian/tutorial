#!/usr/bin/env python3

'''Object : namedtuple

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_asdict', '_fields', '_make', '_replace', '_source', 'count', 'index', 'x', 'y']

'''

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)

print(p[0], p[1])  # -->>11 22
print(p.x, p.y)  # -->> 11 22
print(p)  # -->>Point(x=11, y=22)
print(len(p))  # -->>2
print(p._fields)  # -->>('x', 'y')

[print(x, end=';') for x in p]  # -->>11;22;
print()

np = p._replace(x=33)
print(np)  # -->>p._replace(x=33)

d1 = p._asdict()
print(d1)  # -->>OrderedDict([('x', 11), ('y', 22)])

print(p._source)
'''
class Point(tuple):
    'Point(x, y)'

    __slots__ = ()

    _fields = ('x', 'y')

    def __new__(_cls, x, y):
        'Create new instance of Point(x, y)'
        return _tuple.__new__(_cls, (x, y))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Point object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 2:
            raise TypeError('Expected 2 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Point object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')
'''

print(np.__doc__)  # -->>Point(x, y)

l1 = [100, 200]
p1 = Point(*l1)
print(p1)  # -->>Point(x=100, y=200)

l1 = [100, 200]
p2 = Point._make(l1)
print(p2)  # -->>Point(x=100, y=200)

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

record1 = ['wangj', '30', 'software engineer', 'fast', 'C']
e1 = EmployeeRecord._make(record1)
[print(x) for x in e1]

import csv

# for emp in map(EmployeeRecord._make)
