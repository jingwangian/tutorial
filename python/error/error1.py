#!/usr/bin/env python3

import os


def f1():
    try:
        w1 = "hello world"
        raise IOError('unknow error {}'.format(w1))
    except IOError as e:
        print("IOError error:", e)
    finally:
        if w1:
            print("w1 is ", w1)


def f2():
    try:
        t1 = 100
        print(t1.h1())
    except AttributeError as e:
        print("AttributeError error:", e)

    # try block will not create a block namespace, so t1 can be visited as following
    print("t1 == ", t1)

    t2 = None
    try:
        print(t2.h1())
    except AttributeError as e:
        print("AttributeError error:", e)


def f3():
    invalid_file = 'abxx/x1/t1.psg'
    os.remove(invalid_file)


def f4():
    filename = "/test/a1.txt"
    try:
        os.remove(filename)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    f4()
