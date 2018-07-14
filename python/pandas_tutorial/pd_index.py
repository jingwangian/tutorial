#!/usr/bin/env python3
import numpy as np
import pandas as pd

def print_info(msg):
    print("*"*40)
    print("command: {}".format(msg))
    print(eval(msg))
    print('')


data = pd.DataFrame(np.arange(16).reshape((4,4)),
             index = ['Ohio', 'Colorado', 'Utah', 'New York'],
             columns=['one', 'two', 'three', 'four'])

print(data)

# print_info("data[2]")
print_info("data[2:4]")

print(data[['two','four']])

print_info("data['three'] > 5")

print_info("data.iloc[2:4, [3, 0, 1]]")
print_info("data.iloc[2:4, [3, 0, 1]].transpose()")

print_info("data.iloc[2]")

print_info("data.iloc[:,2]")

print_info("data.loc[:,['two','three']]")

data.iloc[1,2]= np.nan

print(data)
