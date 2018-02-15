#!/usr/bin/env python3


'''
input:
4 
a a c d
2
'''
from itertools import combinations as cb
from functools import reduce

cbnum=[1,2,3,4,5,1,2,3,4]

total_appears = 0
for x in cbnum:
	if x==1:
		total_appears +=1

print(sum(map(lambda x: 1 if x==1 else 0,cbnum)))


l1=list(enumerate('aabc',1))

print(l1)

print(total_appears)
