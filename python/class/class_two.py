#!/usr/bin/env python3

# @property


class C:
    value1 = 100
    value2 = 200

    def __init__(self):
        self._x = None
        self.ivalue = 100

    @property
    def x(self):
        """ Get x value"""
        print('Get x value')
        return self._x

    @x.setter
    def x(self, new_value):
        """Set the x value"""
        print('Set x value')
        self._x = new_value

    @x.deleter
    def x(self):
        print('Del x attribute')
        del self._x

    def __str__(self):
        return 'totalvalue is {}'.format(self.value1 + self.value2)


c1 = C()
c2 = C()

# Here value1 and value2 are class value
print(c1.value1, c1.value2)
print(c2.value1, c2.value2)
print(c1)
print(c2)
print(c1.__dict__)

# Here value1 and value2 will be instance value
c1.value1 = 1000
c1.value2 = 2000
print(c1.value1, c1.value2)
print(c1.__dict__)
print(c2.value1, c2.value2)
print(c1)
print(c2)
