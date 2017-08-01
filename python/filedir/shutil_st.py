#!/usr/bin/env python3

'''
shutil study

Functions:

'''
import shutil
import os

dir = '/db2/github/tutorial/python'

[print('{:>05.2} G'.format(x / (1024 * 1024 * 1024))) for x in shutil.disk_usage(dir)]


def printkey(obj):
    def f(n):
        return ',' if n % 8 > 0 else None
    [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
    print('')

printkey(shutil)
