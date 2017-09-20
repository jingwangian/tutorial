#!/usr/bin/env python3

"""
This tutorial will introduce the *args and **kwargs usage in function.

"""


def fun1(p1, p2=None, *args, **kwargs):
    print('Enter fun1')
    print("p1-->{}; p2-->{};args-->{}; kwargs-->{}".format(p1, p2, args, kwargs))
    print('')


def fun2(args):
    print('Enter fun2')
    print("args-->{}".format(args))
    print('')


def print_db(version, db):
    print(print_db.__name__)
    print('db:{} -- version:{}'.format(db, version))

list1 = ['apple', 'banana']
dict1 = {'db': 'postgresql', 'version': 9.6}

print(list1)
print(*list1)
print(dict1)
# print((**dict1))

fun1('hello')
# ---> p1-->hello; p2-->None;args-->(); kwargs-->{}

fun1(*'hello')
# ---> p1-->h; p2-->e;args-->('l', 'l', 'o'); kwargs-->{}

fun1('hello', [1, 2, 3])
# ---> p1-->hello; p2-->[1, 2, 3];args-->(); kwargs-->{}

fun1('hello', *[1, 2, 3])
# ---> p1-->hello; p2-->1;args-->(2, 3); kwargs-->{}

fun1(*'hello', [1, 2, 3])
# ---> p1-->hello; p2-->[1, 2, 3];args-->(); kwargs-->{}

fun1(*'hello', *[1, 2, 3])
# ---> p1-->hello; p2-->[1, 2, 3];args-->(); kwargs-->{}


fun1('hello', [1, 2, 3], 'apple', 'banana', {'db': 'postgresql', 'version': 9.6})
# ---> p1-->hello; p2-->[1, 2, 3];args-->('apple', 'banana', {'db': 'postgresql', 'version': 9.6}); kwargs-->{}

fun1('hello', *[1, 2, 3], 'apple', 'banana', dict1)

fun1('hello', [1, 2, 3], 'apple', 'banana', dict1)
# ---> p1-->hello; p2-->[1, 2, 3];args-->('apple', 'banana', {'db': 'postgresql', 'version': 9.6}); kwargs-->{}

fun1('hello', [1, 2, 3], 'apple', 'banana', **dict1)
# ---> p1-->hello; p2-->[1, 2, 3];args-->('apple', 'banana'); kwargs-->{'db': 'postgresql', 'version': 9.6}

fun1('hello', [1, 2, 3], 'apple', 'banana', dict1, **dict1)
# ---> p1-->hello; p2-->[1, 2, 3];args-->('apple', 'banana', {'db': 'postgresql', 'version': 9.6}); kwargs-->{'db': 'postgresql', 'version': 9.6}

fun1('hello', [1, 2, 3], list1, dict1, **dict1)
# ---> p1-->hello; p2-->[1, 2, 3];args-->(['apple', 'banana'], {'db': 'postgresql', 'version': 9.6}); kwargs-->{'db': 'postgresql', 'version': 9.6}

fun1('hello', *[1, 2, 3], list1, dict1)
# ---> p1-->hello; p2-->1;args-->(2, 3, ['apple', 'banana'], {'version': 9.6, 'db': 'postgresql'}); kwargs-->{}

fun1('hello', *[1, 2, 3][1:3], list1, dict1)
# ---> p1-->hello; p2-->2;args-->(3, ['apple', 'banana'], {'version': 9.6, 'db': 'postgresql'}); kwargs-->{}

fun1('hello', (1, 2, 3), list1, dict1)
# ---> p1-->hello; p2-->(1, 2, 3);args-->(['apple', 'banana'], {'version': 9.6, 'db': 'postgresql'}); kwargs-->{}

fun1('hello', *(1, 2, 3), list1, dict1)
# ---> p1-->hello; p2-->1;args-->(2, 3, ['apple', 'banana'], {'db': 'postgresql', 'version': 9.6}); kwargs-->{}

fun1('hello', *(1, 2, 3)[1:3], list1, dict1)
# ---> p1-->hello; p2-->2;args-->(3, ['apple', 'banana'], {'version': 9.6, 'db': 'postgresql'}); kwargs-->{}


fun1('hello', [1, 2, 3], *list1, dict1, **dict1)
# ---> p1-->hello; p2-->[1, 2, 3];args-->('apple', 'banana', {'db': 'postgresql', 'version': 9.6}); kwargs-->{'db': 'postgresql', 'version': 9.6}

print_db(**dict1)
# ---> db:postgresql -- version:9.6

# fun2(list1)
# args-->['apple', 'banana']

# fun2(*list1)
'''Traceback (most recent call last):
  File "/db2/github/tutorial/python/basic/fun_st.py", line 64, in <module>
    fun2(*list1)
TypeError: fun2() takes 1 positional argument but 2 were given'''
