#!/usr/bin/env python3

"""
This tutorial will introduce the *args and **kwargs usage in function.

"""


def fun1(p1, p2=None, *args, **kwargs):
    print('Enter fun1')
    print("p1-->{}; p2-->{}".format(p1, p2))
    print("print args:")
    [print(x) for x in args]

    print("print kwargs:")
    [print(x, y) for x, y in kwargs.items()]
    print('')


def fun2(**kwargs):
    try:
        print('student :', kwargs['student'])
        print('teachers :', kwargs['teachers'])

    except KeyError as e:
        print('{} is not there'.format(e))

    if 'assistant' in kwargs:
        print('assistant : {}'.format(kwargs['assistant']))


def fun3(**kwargs):
    try:
        print('student :', kwargs.get('student'))
        print('teachers :', kwargs.get('teachers'))
        print('assistant :', kwargs.get('assistant'))

    except KeyError as e:
        print('{} is not there'.format(e))


def print_db(version, db):
    print(print_db.__name__)
    print('db:{} -- version:{}'.format(db, version))


list1 = ['apple', 'banana']
dict1 = {'db': 'postgresql', 'version': 9.6}

print(list1)
print(*list1)
print(dict1)
# print((**dict1))
print('db : {db} -- version : {version}'.format(**dict1))

fun1('hello', 100, *list1, **dict1)

fun2(student=200, teachers=10)
fun2(student=100, teachers=20, assistant=5)
fun2(student=100, assistant=5)

print('*' * 20, 'fun3', '*' * 20)
fun3(student=200, teachers=10)
fun3(student=100, teachers=20, assistant=5)
fun3(student=100, assistant=5)
