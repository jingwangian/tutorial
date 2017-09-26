#!/usr/bin/env python3


import sys
from itertools import dropwhile

s = 'beabee-feab'

s = 'www.abc.xy'
k = 87

s = 'DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.'
k = 45
es = 'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.'

S = 'OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS'

num = 0
print(len(S))
print(int(len(S) / 3))
for i in range(int(len(S) / 3)):
    msg = S[i * 3:i * 3 + 3]
    if msg != 'SOS':
        num += 1
print(num)
