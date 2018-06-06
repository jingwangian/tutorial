#!/usr/bin/env python3


'''
input:
4
a a c d
2
'''
import os

from collections import OrderedDict

statinfo = os.stat('t2.py')

print(statinfo)
print(statinfo.st_mode)


statinfo = os.stat('t3.py')

print(statinfo)
print(statinfo.st_mode)


stat_result_1 = os.stat_result(range(1, 11))
print(stat_result_1.st_mode)


s1 = "st_mode=33277, st_ino=1181272, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000,st_size=645, st_atime=1526254738, st_mtime=1525084270, st_ctime=1525084270"
s2 = "st_mode=33277, st_ino=1181273, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=775, st_atime=1526254738, st_mtime=1520981849, st_ctime=1520981849"


# [print(x.strip().split('=')[1], end=',') for x in s1.split(",")]
# print()
# [print(x.strip().split('=')[1], end=',') for x in s2.split(",")]
# print()

# print([x.strip().split('=')[1] for x in s1.split(",")])

stat_result_1 = os.stat_result([x.strip().split('=')[1] for x in s1.split(",")])

print(stat_result_1)


dirinfo = os.stat('/db/github')
print(dirinfo)
