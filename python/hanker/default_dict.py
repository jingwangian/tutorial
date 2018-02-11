#!/usr/bin/env python3

from collections import defaultdict

n, m = input().strip().split(' ')
n, m = int(n), int(m)

group_a = [input().strip() for i in range(n)]
group_b = [input().strip() for i in range(m)]

d = defaultdict(list)

index = 0
lna = len(group_a)
[d[group_a[index]].append(index + 1) for index in range(lna)]


for k in group_b:
    [print(x, end=' ') for x in d[k]]
    print('')
