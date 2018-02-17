#!/usr/bin/env python3


def cube(x): return x**3


def fibonacci(n):
    # return a list of fibonacci numbers
    def fib(x): return x if x < 2 else fib(x - 1) + fib(x - 2)
    return list(map(fib, range(n)))


if __name__ == '__main__':
    # n = int(input())
    n = 5
    print(list(map(cube, fibonacci(n))))
