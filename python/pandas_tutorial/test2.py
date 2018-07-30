#!/usr/bin/env python3

from itertools import combinations

s1 = 'abcde'

l1 = combinations(s1, len(s1) - 2)

print(list(l1))

s2 = 'abababbabab'


def valid_string(s):
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            print(i, s[i],s[i+1])
            return False

    return True

print(valid_string(s2))
print(valid_string('ababababa'))
