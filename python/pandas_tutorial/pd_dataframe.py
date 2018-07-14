#!/usr/bin/env python3
import numpy as np
import pandas as pd

def print_info(msg):
    print("*"*40)
    print("command: {}".format(msg))
    print(eval(msg))
    print('')

index = ['one', 'two', 'three', 'four','five', 'six']

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data, index=index, columns=['year', 'state', 'pop','debt'])

print_info("frame")

print_info("frame.loc['three']")

arr1 = frame.loc['three']

print(arr1.values, type(arr1), arr1.index)

# print_info("frame['year']")

arr2 = frame['year']
print(arr2.shape, arr2.index, type(arr2), arr2['two'])

frame2 = frame.transpose()

print_info("frame")
print_info("frame2")

print(frame2.four[1:3])

frame2.index.name = 'row'; frame2.columns.name = 'column'
print_info("frame2.index")