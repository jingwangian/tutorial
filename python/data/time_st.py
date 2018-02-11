#!/usr/bin/env python3

import time

t1 = time.time()
local_t1 = time.localtime(t1)
gm_t1 = time.gmtime(t1)

time.sleep(1)

t2 = time.time()
local_t2 = time.localtime(t2)
gm_t2 = time.gmtime(t2)

print(t1)
tx = t2 - t1
print(tx, type(tx))

print('t2 - t1:', int(t2 - t1))
print('local_t1:', local_t1)
print('local_t2:', local_t2)

print('gm_t1:', gm_t1)
print('gm_t2:', gm_t2)

print("time.timezone / 3600 --->", time.timezone / 3600)
print("time.tzname--->", time.tzname)

print("time.ctime() = {}".format(time.ctime()))
print("time.gmtime() = {}".format(time.gmtime()))
print("time.localtime() = {}".format(time.localtime()))

print(time.altzone / 3600)

print(time.localtime().tm_year)
# print(dir(time.localtime()))
