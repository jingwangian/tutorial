#!/usr/bin/env python3

'''
Python performance study

Optimization includes:
1. speed
2. memory
3. disk space
4. disk I/O
5. network I/O
6. Power consumption

The methods inlcudes:
1. Try to use the built-in functions

2. Filter a List
    [x for x in MILLION_ELEMENTS if x%2]


3. permissions vs forgiveness
    class Foo(object):
        hello = 'world'

    foo = Foo()

    if hasattr(foo,'hello'):
        print(foo.hello)

    # 149ns

    try:
        print(foo.hello)
    except AttributeError:
        pass

    # 33ns

4. membership testing

5. Remove duplicates
    set(MILLION_ELEMENTS)

6. List sorting
    sorted(MILLION_ELEMENTS)  #476ms
    MILLION_ELEMENTS.sort()   #77.6ms

7. call function 1000 times and 1 function call 1000 operations

8. checking for True
    if var == True:
        35.8ns
    if var is True:
        28.7ns
    if var:
        20.6ns

    if len(list1) == 0:
        91.7ns
    if list1 = []:
        56.3ns

    if not list1:
        32.4ns

9. list or []
    list()  # 104ns
    [] #22.5ns

10. Lookup local scope is faster than other scopes (LEGA)
'''

import time

MILLION_ELEMENTS = range(1, 10000000)

how_many = 0

t1 = time.time()

for e in MILLION_ELEMENTS:
    how_many += 1

print(how_many)   #time: 1.6632080078125

# print(len(MILLION_ELEMENTS))    #time: 3.3855438232421875e-05
print('time: {}'.format(time.time() - t1))
