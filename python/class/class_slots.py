#!/usr/bin/env python3

"""
Test __slots__ vs __dict__
"""

import time
import timeit


class Foo(object):
    __slots__ = 'foo',
    t1 = 123


class Bar(object):
    t1 = 123


slotted = Foo()
not_slotted = Bar()

slotted.foo = 'abc'
not_slotted.foo = 'abc'
print(dir(slotted))
print(dir(not_slotted))

print(not_slotted.__dict__)


def get_set_delete_fn(obj):
    def get_set_delete():
        num = 10
        while(num > 0):
            obj.foo = 'foo'
            obj.foo
            del obj.foo
            num -= 1
    return get_set_delete


print('Start to test')

t1 = time.time()
get_set_delete_fn(slotted)()
print(time.time() - t1)

t1 = time.time()
get_set_delete_fn(not_slotted)()
print(time.time() - t1)


print('End test')
