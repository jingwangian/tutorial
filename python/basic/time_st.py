#!/usr/bin/env python3

'''
time study

CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', '_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__',
'altzone', 'asctime', 'clock', 'clock_getres', 'clock_gettime',
'clock_settime', 'ctime', 'daylight', 'get_clock_info', 'gmtime',
'localtime', 'mktime', 'monotonic', 'perf_counter', 'process_time',
'sleep', 'strftime', 'strptime', 'struct_time', 'time', 'timezone', 'tzname', 'tzset'
'''

import time

t1 = time.time()

time.sleep(1)

t2 = time.time()

d = t2 - t1

print(t2 > t1)

print(d)

time.strptime("30 Nov 00", "%d %b %y")

# print(dir(time))
