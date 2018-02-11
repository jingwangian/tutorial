#!/usr/bin/env python

from collections import deque

'''
input is:

2
6
4 3 2 1 3 4
3
1 3 2
'''


def dq_pop_max(dq):
    try:
        if dq[0] >= dq[-1]:
            return dq.popleft()
        else:
            return dq.pop()
    except IndexError:
        return None


def check_stack_dq(dq):
    cur_value = pop_value = dq_pop_max(dq)
    while(pop_value):
        if cur_value >= pop_value:
            cur_value, pop_value = pop_value, dq_pop_max(dq)
        else:
            return 'No'
    return 'Yes'


testcases = int(input().strip())
dq_list = []
for i in range(testcases):
    num = int(input().strip())
    dq_list.append(deque([int(x) for x in input().strip().split(' ')]))

for dq in dq_list:
    print(check_stack_dq(dq))
