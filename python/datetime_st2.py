#!/usr/bin/env python3


'''
datetime

Sample Input

07:05:45PM
Sample Output

19:05:45
'''

import sys
import time


def timeConversion(s):
    # Complete this function
    t1 = time.strptime(s, '%I:%M:%S%p')

    return time.strftime('%H:%M:%S', t1)


# s = input().strip()
s = '07:05:45PM'

result = timeConversion(s)

print(result)
