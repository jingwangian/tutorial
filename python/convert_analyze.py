#!/usr/bin/env python3

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import re
# import datetime
from datetime import timedelta
from datetime import datetime

file_name = 'main_2017-07-27.log'

time_lines = []

t1 = None
pre_d1 = None
with open(file_name) as f:
    for line in f:
        if line.find('aws s3 cp s3') != -1:
            item_list = line.strip().split(' ')
            # print(item_list[1:3])
            time_str = '{} {}'.format(*item_list[1:3])
            # time_str = '{0} {1}'.format(*(1, 2))
            # print(line.strip())
            # print(time_str)
            if pre_d1 is None:
                time_lines.append(0)
                d1 = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S,%f")
                pre_d1 = d1
            else:
                d1 = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S,%f")
                t1 = d1 - pre_d1
                pre_d1 = d1
                print(t1.seconds)
                time_lines.append(t1.seconds)

print(len(time_lines))

plt.plot(time_lines)
plt.xlabel('Nth zip file')
plt.ylabel('convert time(seconds)')
plt.show()
