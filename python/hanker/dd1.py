#!/usr/bin/env python3

# Diagonal Difference
'''
Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, . The next  lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

Constraints

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

'''

import sys
from functools import reduce


def diagonal_difference(n, a):
    sum1 = 0
    sum2 = 0
    sum1 = reduce(lambda x, y: x + y, [a[i][i] for i in range(n)])

    sum2 = reduce(lambda x, y: x + y, [a[i][-1 - i] for i in range(n)])

    return abs(sum1 - sum2)


# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)

n = 3
a = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]

print([a[i][i] for i in range(n)])
print([a[i][-1 - i] for i in range(n)])
print(diagonal_difference(3, a))
