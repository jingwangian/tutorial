#!/usr/bin/env python3


import sys


def theLoveLetterMystery(s):
    # Complete this function
    s1 = [ord(x) for x in s]
    s2 = list(reversed(s1))

    count = 0
    half_len = len(s1) // 2

    for i in range(half_len):
        if s1[i] != s2[i]:
            count += abs(s1[i] - s2[i])

    return count


# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     result = theLoveLetterMystery(s)
#     print(result)


array = [
    'abc',
    'abcba',
    'abcd',
    'cba',
]

for s in array:
    result = theLoveLetterMystery(s)
    print(result)
