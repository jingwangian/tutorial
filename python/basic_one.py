#!/usr/bin/env python3


# Div/Divd/mod
list1 = [(7, 4), (18, 3), (19, 2), (21, 8)]
print([x / y for x, y in list1])
print([x // y for x, y in list1])
print([x % y for x, y in list1])

# Easy swap
i = 10
k = 20
i, k = k, i
print(i, k)

# One line condition
max_num = i if i > k else k


# One line expression
# [ expression for value in iterable if condition ]
list1 = [x for x in range(1, 11)]
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x >= 5])

list2 = [('a', 4), ('b', 3), ('c', 2), ('d', 8)]
# Now we create a dict based on list2
dict1 = {k: v for k, v in list2}
print('dict1 is {}'.format(dict1))
# Filter function : filter(fn,iterable)


def fn1(x):
    return x >= 5
print(list(filter(lambda x: x >= 5, range(1, 11))))
print(list(filter(fn1, range(1, 11))))
print([x * x for x in filter(fn1, range(1, 11))])

# Map function : map(fn,iterable)
print(list(map(lambda x: x * x if x >= 5 else 0, list1)))


# Pack and unpacke
a, b, c, d = range(7, 11)
print(a, b, c, d)
a, b, c, d = [1, 2, 3, 4, 5, 6][1:5]
print(a, b, c, d)
