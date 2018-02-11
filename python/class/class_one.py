#!/usr/bin/env python3

# @property


class C:
    def __init__(self):
        self._x = None

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


c = C()
print(c.x)
c.x = 100
print(c.x)
print("c.__dict__--->", c.__dict__)
del c.x
# Now no x in the c if print c.__dict__
print("c.__dict__--->", c.__dict__)
# attribute can be added dynamically
c.y = 200
print('c.y={}'.format(c.y))

# If set x attribute again, the _x will be used again
c.x = 300
print('c.x={}'.format(c.x))
print("c.__dict__--->", c.__dict__)

# Can't visit c._x directly
try:
    print('c.x={}'.c._x)
except AttributeError:
    print("Can't visit c._x directly")

# Now x come into the c again
print(c.__dict__)
print(c.__dict__.keys())
