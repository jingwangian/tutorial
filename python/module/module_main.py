#!/usr/bin/env python3


import os
import sys

print('main path: ', sys.path)
print(globals())
print(locals())

import module_a
import car
from car import Car


print(dir(car))


car1 = Car('civil', 'honda', 'hatch back', 5)
car2 = Car('accord euro', 'honda', 'hatch back', 5)

print(car1)
print(car2)
