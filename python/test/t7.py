#!/usr/bin/env python3

from collections import defaultdict


def f1(n):
    return 10 if n > 10 else 1


print(f1(20))
print(f1(9))

d = defaultdict(int)

d['a'] -= 1

d['a'] -= 1

print(d['a'])
