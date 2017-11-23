#!/bin/python3

import sys


def gcd(a, b):
    if a == 0 or b == 0:
        return 0

    while a != 0:
        print('a={}, b={}'.format(a, b))
        a, b = b % a, a

    return b


# print(gcd(3, 7))
# print(gcd(4, 8))
print(gcd(48, 22))
print(gcd(48, 20))
print(gcd(48, 18))
print(gcd(48, 16))

print(gcd(48, 9))

print(gcd(48, 8))
# print(gcd(212, 68))

# print(gcd(1, 12))

# print(gcd(0, 12))
# print(gcd(12, 0))
