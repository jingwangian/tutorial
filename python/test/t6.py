#!/usr/bin/env python3


import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = (a0, a1, a2)
    B = (b0, b1, b2)

    point_a = 0
    point_b = 0
    for x, y in zip(A, B):
        if x > y:
            point_a += 1
        elif x < y:
            point_b += 1
    return point_a, point_b


x1 = 10**20


print(list(range(5)))
print(list(range(-1, -(5 + 1), -1)))
