#!/usr/bin/env python3


import sys
import time


def stringConstruction(s):
    # Complete this function

    return len(set(s))


s = 'abcdxabcxf'
s = 'abab'
result = stringConstruction(s)
print(result)

# if __name__ == "__main__":
#     q = int(input().strip())
#     for a0 in range(q):
#         s = input().strip()
#         result = stringConstruction(s)
#         print(result)
