#!/usr/bin/env python

from collections import OrderedDict

n = int(input().strip())

od = OrderedDict()
for i in range(n):
    name = input().strip()
    try:
        od[name] = od[name] + 1
    except KeyError:
        od[name] = 1

print(len(od))
print(*list(od.values()), sep=' ')
