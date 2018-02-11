#!/usr/bin/env python3

import sys


def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x1 < x2:
        if v1 <= v2:
            return 'NO'
        else:
            return check_meet_availabe(x1, v1, x2, v2)
    elif x1 == x2:
        return 'YES'
    elif x2 < x1 and v2 <= v1:
        return 'NO'
    else:
        return check_meet_availabe(x2, v2, x1, v1)


def check_meet_availabe(x1, v1, x2, v2):
    '''
    assume x1<x2 and v1>v2
    '''
    num = 0
    while(1):
        x1 = x1 + v1
        x2 = x2 + v2
        if x1 == x2:
            return 'YES'
        elif x1 > x2:
            return 'NO'


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
