#!/bin/python3

import sys


s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_num = 0
orange_num = 0

for pos in apple:
    if (a + pos) in range(s, t + 1):
        apple_num += 1

for pos in orange:
    if (b + pos) in range(s, t + 1):
        orange_num += 1

print(apple_num)
print(orange_num)
