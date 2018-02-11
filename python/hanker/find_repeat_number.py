#!/usr/bin/env python3

import re

'''
input:
..12345678910111213141516171820212223
'''
# s1=input().strip()

s1 = '..123456789101112131415166617182021222239999'
s1 = 'thethebcdbcdbcd'
m = re.search(r'([a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9])\1([a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9])\2', s1)
# print(m.group(1) if m else -1)
print(m.groups() if m else -1)
