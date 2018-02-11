#!/usr/bin/env python

from collections import deque

'''
input is:

6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''

n = int(input().strip())
dq = deque()

for i in range(n):
    items = input().strip().split(' ')
    if len(items) == 2:
        action, num = items
    else:
        action = items[0]

    # num = int(num)
    if action == 'append':
        dq.append(num)
    elif action == 'appendleft':
        dq.appendleft(num)
    elif action == 'pop':
        dq.pop()
    elif action == 'popleft':
        dq.popleft()

[print(x, end=' ') for x in dq]
