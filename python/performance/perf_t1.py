#!/usr/bin/env python3

'''
Python performance study

'''

import time
from timeit import timeit

# MILLION_ELEMENTS = range(1, 10000000)

# how_many = 0

# t1 = time.time()

# for e in MILLION_ELEMENTS:
#     how_many += 1

# print(how_many)   #time: 1.6632080078125

# # print(len(MILLION_ELEMENTS))    #time: 3.3855438232421875e-05
# print('time: {}'.format(time.time() - t1))

t1 = timeit('"-".join(str(n) for n in range(100))', number=100)
print(t1)


def add_string_with_plus(iters):
    s = ""
    for i in range(iters):
        s += "xyz"
    assert len(s) == 3 * iters


def add_string_with_format(iters):
    fs = "{}" * iters
    s = fs.format(*(["xyz"] * iters))
    assert len(s) == 3 * iters


def add_string_with_join(iters):
    l = []
    for i in range(iters):
        l.append("xyz")
    s = "".join(l)
    assert len(s) == 3 * iters


def convert_list_to_string(l, iters):
    s = "".join(l)
    assert len(s) == 3 * iters


print('timeit(add_string_with_plus(10000))')
# # print(timeit(add_string_with_plus(10000)))
# timeit(add_string_with_plus(10000))
