#!/usr/bin/env python3

'''
Combinatoric generators:
product, permutations, combinations, combinations_with_replacement()

permutations(iterable, r=None)  -- r-length tuples, all possible orderings, no repeated elements
'''

import itertools as it

for x in it.count(10):
    print(x)
    if x > 20:
        break

for t in it.compress('abcdefg', [1, 0, 1, 1, 1]):
    print(t)

for t in it.compress(['a1', 'a2', 'a3'], [1, 0, 1, 1, 1]):
    print(t)

for t in it.compress({'b1': 1, 'b2': 2, 'b3': 3}, [1, 0, 1, 1, 1]):
    print(t)

# print(list(it.product('ABCD', '1234')))
# print(list(it.product('ABCD', '1234', 'abcd')))

# product('ABCD', repeat=3) == product('ABCD', 'ABCD', 'ABCD')


# print(list(it.product('ABCDE', repeat=3)))

'''
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D')]
'''
# print(list(it.permutations('ABDEa', 3)))

print(list(it.product([1, 2, 3, 4], repeat=2)))
print(list(it.permutations([1, 2, 3, 4], 2)))


# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
# print(list(it.combinations('ABCDE', 2)))
