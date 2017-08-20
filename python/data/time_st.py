#!/usr/bin/env python3

import time

t1 = time.time()
local_t1 = time.localtime(t1)
gm_t1 = time.gmtime(t1)

time.sleep(1)

t2 = time.time()
local_t2 = time.localtime(t2)
gm_t2 = time.gmtime(t2)

print(t2 - t1)
print(local_t1)
print(local_t2)

print(gm_t1)
print(gm_t2)

print(time.timezone/3600)
print(time.tzname)
