#!/usr/bin/env python3
import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])

print(obj)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

obj3 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'e'])

print(obj2)
print(obj2.index)
print(obj2*2)

print('b' in obj2)

print(4 in obj2.values)

print("obj2+obj3")
print(obj2+obj3)


sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj4 = pd.Series(sdata)
print(obj4[['Texas','Utah']].keys())

print(obj4.sort_values(ascending=True))

print(obj4)
