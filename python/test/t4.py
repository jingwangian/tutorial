#!/usr/bin/env python3


def myzip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            print('it is {}'.format(it))
            elem = next(it, sentinel)
            print(elem)
            if elem is sentinel:
                return
            result.append(elem)
            print(result)
        yield tuple(result)


l1 = myzip(['a', 'b', 'c'], [1, 2, 3, 4])
print(list(l1))


l2 = [1, 2, 3, 4, 5]
while l2:
    print(l2.pop())
