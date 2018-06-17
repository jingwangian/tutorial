#!/usr/bin/env python3


def log(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


def double_inputs():
    print("double_inputs start")
    while True:
        print("before x=yield")
        x = yield
        print("before yield *2 ")
        yield x * 2
        print("after yield *2 ")


def double_inputs_2():
    print("double_inputs start")
    while True:
        print("double_inputs_2: before yield *2 ")
        x = yield x * 2
        print("double_inputs_2: after yield *2 ")


gen = double_inputs()

print("run next")
print(next(gen))

print("run send")
print(gen.send(10))

print("run next")
print(next(gen))
