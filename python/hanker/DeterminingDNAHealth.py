#!/usr/bin/env python3


import sys


count = 0


def find_total_substring(s1, s2):
    '''
    Find the total number of s2 in s1.
    Example: s1='aaaab'  s2='aa', number = 3
    Explain: 1st time found is s1[0],s1[1]
             2nd time found is s1[1],s1[2]
             3rd time found is s1[2],s1[3]
    '''

    pos = s1.find(s2)
    if pos != -1:
        try:
            print('pos is {}'.format(pos))
            return (find_total_substring(s1[pos + 1:], s2) + 1)
        except IndexError:
            return 1
    else:
        return 0


# n = int(input().strip())
# genes = input().strip().split(' ')
# health = list(map(int, input().strip().split(' ')))
# s = int(input().strip())
# for a0 in range(s):
#     first, last, d = input().strip().split(' ')
#     first, last, d = [int(first), int(last), str(d)]
    # your code goes here

gen_health_list = list(zip(genes, health))

value = 0
max_value = 0
min_value = 0
for gen in gen_health_list[first, last + 1]:
    number = find_total_substring(d, gen[0])
    value += number * gen[1]


s1 = 'baaaaaadsaaaxbaa'
s2 = 'aa'

result = find_total_substring(s1, s2)
print(result)
