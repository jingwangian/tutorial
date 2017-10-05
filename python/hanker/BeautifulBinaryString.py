#!/usr/bin/env python3

import sys


def minSteps(n, B):
    # Complete this function
    bstr = list(B)

    print(bstr)
    changed_steps = 0
    for i in range(2, len(bstr)):
        if bstr[i - 2] == '0' and bstr[i - 1] == '1' and bstr[i] == '0':
            bstr[i] = '1'
            changed_steps += 1

    return changed_steps


# n = int(input().strip())
# B = input().strip()

B = '0101010'
result = minSteps(1, B)
print(result)
