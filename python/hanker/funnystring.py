#!/usr/bin/env python3

import sys

'''
Suppose you have a String,S , of length N that is indexed from 0 to N-1 . You also have some String,R , that is the reverse of String S. S is funny if the condition |S[i]-S[i-1]|==|R[i]-R[i-1]|is true for every character from 1 to N-1 .

Note: For some String S, denotes the ASCII value of the ith 0-indexed character in S. The absolute value of an integer,x , is written as |x|.

Input Format

The first line contains an integer, (the number of test cases).
Each line of the subsequent lines contain a string, .

Constraints

Output Format

For each String (where ), print whether it is or on a new line.

Sample Input

2
acxz
bcxz

Sample Output

Funny
Not Funny

Explanation

Test Case 0:



As each comparison is equal, we print .

Test Case 1:
, but
At this point, we stop evaluating (as ) and print .

'''
def funnyString(s):
    num_s = [ord(x) for x in s]
    num_rs = list(reversed(num_s))

    for i in range(1, len(num_s)):
        if abs(num_s[i] - num_s[i - 1]) != abs(num_rs[i] - num_rs[i - 1]):
            return 'Not Funny'

    return 'Funny'


# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     result = funnyString(s)
#     print(result)


s = 'acxz'

result = funnyString(s)
print(result)

print(funnyString('bcxz'))
