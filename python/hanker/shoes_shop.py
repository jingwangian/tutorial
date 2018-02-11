#!/usr/bin/env python3

from collections import Counter

s1='''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''

def canculate_money(shoes, customers):
	shoes = Counter(shoes)
	total_price = 0
	for x in customers:
		size = x[0]
		if shoes[size]>0:
			shoes[size] -=1
			total_price +=x[1]

	return total_price

X = input()
shoes = input().strip().split(' ')
N = int(input().strip())

customers = [input().strip().split(' ') for i in range(N)]

customers = [(x[0],int(x[1])) for x in customers]


total_price = canculate_money(shoes, customers)

print(total_price)

print(customers)
print(shoes)