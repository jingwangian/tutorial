#!/usr/bin/env python3


'''
input:
4 
a a c d
2
'''
from itertools import combinations as cb

N = int(input())
L = input().split()
K = int(input())

C = list(cb(L, K))
print(list(C))
F = filter(lambda c: 'a' in c, C)
print(list(F))
print("{0:.3}".format(len(list(F))/len(C)))


# pos_list = []

# N=int(input().strip())

# num = 1
# for x in input().strip().split():
# 	if x=='a':
# 		pos_list.append(num)
# 	num +=1


# set1 = set(pos_list)

# K = int(input().strip())

# cbnum = [set(x) for x in cb(range(1,N+1),K)]

# total_appears = 0

# for x in cbnum:
# 	if bool(set1 & x):
# 		total_appears +=1

# print(format(total_appears/len(cbnum),'.4f'))
