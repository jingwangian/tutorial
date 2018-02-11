#!/usr/bin/env python3

import sys


def getTotalX(a, b):
    # Complete this function
    max_a = max(a)
    min_b = min(b)

    total = 0
    if max_a > min_b:
        return 0
    else:
        for n in range(max_a, min_b + 1):
            # print([n % x for x in a])
            # print([x % x for x in b])
            if max([n % x for x in a]) == 0 and max([x % n for x in b]) == 0:
                total += 1

        return total


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
