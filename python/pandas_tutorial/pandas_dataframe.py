#!/usr/bin/env python3

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as pl


# Every a value being a list as a column
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

# print(frame)
""" will print as a table
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
"""

# You can specify the sequence of the columns
frame = DataFrame(data, columns=['year', 'state', 'pop'])
# Print all values as a table
print(frame)

# Print one column
print(frame['year'])

# Only print indicate column and rows
print(frame['year'][1:3])

s1 = frame['year']
s1.plot()
frame.plot()
