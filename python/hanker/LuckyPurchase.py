#!/bin/python3

import sys
import re

if __name__ == "__main__":
    n = int(input().strip())
    valid_laptops = set()
    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), int(value)]

        m = re.search(r'^[4,7]+$', str(value))
        if m is None:
            continue

        count4 = str(value).count('4')
        count7 = str(value).count('7')

        if count4 == count7:
            valid_laptops.add((name, value))

    if len(valid_laptops) == 0:
        print(-1)
    else:
        print(min(valid_laptops, key=lambda x: x[1])[0])
