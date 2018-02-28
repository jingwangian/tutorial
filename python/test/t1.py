#!/usr/bin/env python3


'''
input:
4
a a c d
2
'''
import re

file_name = '/db2/github/p.txt'

with open(file_name) as rf:
	# [print(line) for line in rf]

	rt_list = re.findall(r'\w+print\w+?\(',rf.read())

s1 = set(rt_list)

l1 = list(enumerate('aabc', 1))

print(l1)

print(total_appears)
