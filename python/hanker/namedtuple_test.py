#!/usr/bin/env python3

import re
from collections import namedtuple
from functools import reduce

tup_list = []
n = int(input().strip())

student = namedtuple('student', input().strip())

for x in range(n):
    data_list = re.findall(r'\w+', input().strip())
    tup_list.append(student._make(data_list))

marks = [int(t.MARKS) for t in tup_list]
avgnum = sum(marks) / len(marks)
print('{:.2f}'.format(avgnum))
