#!/usr/bin/env python3

# 2D Array - DS

'''
Context
Given a 2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Input Format

There are lines of input, where each line contains space-separated integers describing 2D Array ; every value in will be in the inclusive range of to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19

Explanation

contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4

'''
from functools import reduce


def get_hourglass_num(hg_array):
    total_num = 0

    for x in hg_array:
        total_num += sum(x)

    return total_num


def get_max_hourglasses(array):
    max_hourglass_num = -10000
    max_row = len(array)
    max_col = len(array[0])

    if max_row < 3 or max_col < 3:
        return get_hourglass_num(array)
    for row in range(0, max_row - 3 + 1):
        for col in range(0, max_col - 3 + 1):
            hourglass = [array[row][col:col + 3], array[row + 1][col + 1:col + 2], array[row + 2][col:col + 3]]
            num = get_hourglass_num(hourglass)
            print(num)
            max_hourglass_num = max(max_hourglass_num, num)

    return max_hourglass_num


array = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]

array = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5]
]
print(get_max_hourglasses(array))
