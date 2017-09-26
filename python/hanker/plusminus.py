#!/usr/bin/env python3

# Plus Minus

import sys


'''
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  “<” | “>” | “=” | “^”
sign            ::=  “+” | “-” | ” “
width           ::=  integer
grouping_option ::=  “_” | “,”
precision       ::=  integer
type            ::=  “b” | “c” | “d” | “e” | “E” | “f” | “F” | “g” | “G” | “n” | “o” | “s” | “x” | “X” | “%”
'''


'''
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeroes in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
'''
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

n = 6
arr = [int(x) for x in '-4 3 -9 0 4 1'.strip().split(' ')]

pn, nn, zn = 0, 0, 0

for x in arr:
    if x > 0:
        pn += 1
    elif x < 0:
        nn += 1
    else:
        zn += 1

total = pn + nn + zn

print('{:.6f}'.format(round(pn / total, 6)))
print('{:.6f}'.format(nn / total))
print('{:.6f}'.format(round(zn / total, 6)))
