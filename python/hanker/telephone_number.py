#!/usr/bin/env python

'''
3
8956324712
FACBGEGADB
85234789651
'''


import re
n = int(input().strip())
for i in range(n):
    m = re.match(r'^[7-9]\d{9}$', input().strip())
    print('YES') if m else print('NO')
