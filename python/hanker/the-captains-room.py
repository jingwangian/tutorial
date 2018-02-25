#!/usr/bin/env python3

from collections import Counter

num = 5
l1 = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split()

c1 = Counter(l1)

[print(k) for k, v in c1.items() if v != 5]

# num = int(input().strip())
# l1 = map(int, input().strip().split())

d1 = dict()

for x in l1:
    d1[x] = d1.get(x, 0) + 1

print(d1)
