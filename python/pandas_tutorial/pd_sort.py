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

data2 = data.reindex(['New York', 'Colorado', 'Ohio', 'Utah'])

print(data2)

print_info("data2.sort_index()")

print_info("data2.sort_index(axis=1)")
print_info("data2.sort_index(axis=1, ascending=False)")

data2 = data.sort_values(by="three")
print(data2.values)

print(data2.iloc[0,1])

# [print(list(x), type(x)) for x in data.values]
