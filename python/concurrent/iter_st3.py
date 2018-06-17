#!/usr/bin/env python3


def func1():
    l1 = [1, 2, 3, 4, 5, 6]
    for n in l1:
        print("before yield n")
        yield n
        print("after yield n")


def double_inputs():
    print("double_inputs start")
    x = 1
    while True:
        print("before yield *2, x={}".format(x))
        x = yield from func1()
        print("after yield *2 , x={}".format(x))


gen = double_inputs()

print("run next")
print(next(gen))

print("run send 10")
print(gen.send(10))

print("run send 30")
print(gen.send(30))

# print("run next")
# print(next(gen))
