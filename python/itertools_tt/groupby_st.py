#!/usr/bin/env python3

'''
groupby

Functions:
__class__,__delattr__,__dir__,__doc__,__eq__,__format__,__ge__,__getattribute__
__gt__,__hash__,__init__,__iter__,__le__,__lt__,__ne__,__new__
__next__,__reduce__,__reduce_ex__,__repr__,__setattr__,__setstate__,__sizeof__,__str__
__subclasshook__,

'''
import sys
import itertools as it
from itertools import groupby

[print(''.join(g)) for k, g in groupby('AAAABBBCCDAACCCBB')]


print([list(g) for k, g in groupby(['a', 'a', 'a', 'a', 'b', 'b', 'b'])])

ret_list = list(map(lambda x: set(x) if len(x) % 2 != 0 else [], [list(g) for k, g in groupby(['a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'b'])]))

print(list(zip([x for x in ret_list if x])))

# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]

# printkey(p)


def super_reduced_list(str_list):
    print('super_reduced_list is invoked with {}'.format(str_list))
    new_group_list = []

    if not str_list:
        return 'Empty String'

    group_list = [list(g) for k, g in groupby(str_list)]

    if(max([len(x) for x in group_list])) == 1:
        return str_list

    # for group in group_list:
    #     if len(group) % 2 > 0:
    #         new_group_list.extend(list(set(group)))

    [new_group_list.extend(list(set(group))) for group in group_list if len(group) % 2 > 0]

    return super_reduced_list(new_group_list)

    # return new_group_list


def super_reduced_list_w2(str_list):
    print('super_reduced_list_w2 is invoked with {}'.format(str_list))

    if not str_list:
        return 'Empty String'

    new_list = []
    len_str_list = len(str_list)
    reduces_number = 0

    i = 0
    while (i < len_str_list):
        if i == len_str_list - 1:
            new_list.append(str_list[i])
            i += 1
        elif str_list[i] == str_list[i + 1]:
            i += 2
            reduces_number += 1
        else:
            new_list.append(str_list[i])
            i += 1

    if reduces_number == 0:
        return new_list
    else:
        return super_reduced_list_w2(new_list)


def super_reduced_string(s):
    # Complete this function

    ret_list = super_reduced_list(list(s))

    print(ret_list)

    return ''.join(ret_list)


# s = raw_input().strip()
# s = 'BCAAAABBBCCBBBDAADCCCBAA'
# result = super_reduced_string(s)
# print(result)


s = 'AAAABBBCCDAACCCB'
s = 'BCAAAABBBCCBBBDAADCCCBAA'
# result = super_reduced_string(s)
# print(result)

result = super_reduced_list_w2(list(s))
print(result)
