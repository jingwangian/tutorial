#!/usr/bin/env python3

import sys


def isValid(s):
    # Complete this function

    set_s = set(s)

# l1 contains all kinds of length for different characters
    l1 = [s.count(c) for c in set_s]
    print(l1)
    # [1,1,1,4,2,3]

# s1 contains different length [1,4]
    s1 = set(l1)
    if len(s1) > 2:
        return 'NO'
    elif len(s1) == 1:
        return 'YES'
    elif len(s1) == 2:
        # go to here only 2 item in s1 [1,1,4,4,4,1], [1,4,4,4], [2,5,5,5], [1,1,1,4] [1,4] [1]  []
        t1 = tuple(s1)

        # [1,4,4,4]
        if min(t1) == 1 and l1.count(1) == 1:
            return 'YES'

        # [1,1,4,4,4]  count0=2, count1=3
        count0 = l1.count(t1[0])
        count1 = l1.count(t1[1])

        if count0 > 1 and count1 > 1:
            return 'NO'

        # [1,1,1,4]
        # print('t1 is {}'.format(t1))
        # print(max(t1), min(t1))
        if max(t1) - min(t1) > 1:
            return 'NO'

    return 'YES'


# s = input().strip()
s = 'aabbcccDDDXX'
s = 'abcccc'
s = 'hfchdkkbfifgbgebfaahijchgeeeiagkadjfcbekbdaifchkjfejckbiiihegacfbchdihkgbkbddgaefhkdgccjejjaajgijdkd'
result = isValid(s)
print(result)
