#!/usr/bin/env python3


def func1():
    l1 = [1, 2, 3, 4, 5, 6]

    yield l1


def double_inputs():
    print("double_inputs start")
    x = 1
    while True:
        print("before yield *2, x={}".format(x))
        x = yield x * 2
        print("after yield *2 , x={}".format(x))


gen = double_inputs()

print("run next")
print(next(gen))

print("run send")
print(gen.send(10))

print("run send")
print(gen.send(30))

# print("run next")
# print(next(gen))
