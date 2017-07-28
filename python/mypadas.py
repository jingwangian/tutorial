#!/usr/bin/env python3

import pandas as pd
from pandas import Series, DataFrame

obj = Series([4, 7, -5, 3])

print(obj)
print(obj[0])
# print(dir(obj))
print(obj.values)
print(type(obj.values))
print(obj.values[1])
print(obj.index)

# create a series with index
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2.values)
print(obj2.index)
print(obj2['b'])
