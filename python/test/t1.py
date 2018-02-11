#!/usr/bin/env python

from itertools import groupby, repeat

s1 = 'aaaabbbccddaaxxyyy'

s2 = groupby(s1)

l1 = [list(g) for k, g in s2]

# [print(len(list(g)), k) for k, g in s2]
# [print(k, list(g)) for k, g in s2]

print(id(s2))
print(id(l1))
print(l1)

l2 = [(len(x), x[0]) for x in l1]

print(l2)


print(list(repeat((1, 2, 3), 3)))
