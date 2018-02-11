#!/usr/bin/env python3

import sys
from functools import reduce


def is_beauty(num, s, s_len):
    bs = ''
    for m in range(num, num + s_len):
        bs = bs + str(m)

        if bs == s:
            return True

        if len(bs) > len(s):
            return False

    return False


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here

    s_len = len(s)
    found = False
    for n in range(1, int(s_len / 2) + 1):
        num = int(s[0:n])
        # print('{}---{}'.format(n, num))
        # x1 = [m for m in range(num, num + s_len)]
        # beauti_s = reduce(lambda x, y: str(x) + str(y), x1)

        if is_beauty(num, s, s_len) == True:
            print('YES {}'.format(num))
            found = True
            break

    if found == False:
        print('NO')
