#!/usr/bin/python3

import sys


def gameOfThrones(s):
    # Complete this function
    # alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # alpha_seq_list = list(enumerate(alpha_list))

    # alpha_dict = {}
    # for t in alpha_seq_list:
    #     alpha_dict[t[1]] = t[0]

    # s_list = list(s)
    # rs_list = reversed(s_list)

    # sum_list = [alpha_dict[s_list[x]] + alpha_dict[s_list[x]] for x in range(len(s_list))]

    # sum_list_len = len(sum_list)
    # for n in range(sum_list_len // 2):
    #     if sum_list[n] != sum_list[-1 - n]:
    #         return 'NO'

    # return 'YES'

    s_list = list(s)
    # s_list.sorted()

    s_set = set(s_list)

    odd_count = 0
    for a in s_set:
        if s_list.count(a)%2==1:
            odd_count+=1

    if len(s_list)%2==1:
        if odd_count == 1:
            return 'YES'
        else:
            return 'NO'
    else:
        if odd_count ==0:
            return 'YES'
        else:
            return 'NO'


s = input().strip()
result = gameOfThrones(s)
print(result)
