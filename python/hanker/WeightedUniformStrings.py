#!/usr/bin/env python3

# Weighted Uniform Strings

'''
A weighted string is a string of lowercase English letters where each letter has a weight in the inclusive range from to , defined below:

a=1,b=2,....z=26

We define the following terms:

    The weight of a string is the sum of the weights of all the string's characters. For example:

    apple = 1+16+16+12+5=50

    A uniform string is a string consisting of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not (i.e., they consist of more than one distinct character).

Given a string s , let U be the set of weights for all possible uniform substrings (contiguous) of string . You have to answer queries, where each query consists of a single integer, . For each query, print Yes on a new line if ; otherwise, print No instead.

Note: The symbol denotes that is an element of set .

Input Format

The first line contains a string denoting (the original string).
The second line contains an integer denoting (the number of queries).
Each line of the subsequent lines contains an integer denoting (the weight of a uniform subtring of that may or may not exist).

Constraints

    will only contain lowercase English letters.

Output Format

Print lines. For each query, print Yes on a new line if ; otherwise, print No instead.

Sample Input 0

abccddde
6
1
3
12
5
9
10

Sample Output 0

Yes
Yes
Yes
Yes
No
No

Explanation 0

The weights of every possible uniform substring in the string abccddde are shown below:

image

We print Yes on the first four lines because the first four queries match weights of uniform substrings of . We print No for the last two queries because there are no uniform substrings in that have those weights.

Note that while de is a substring of that would have a weight of , it is not a uniform substring.

Note that we are only dealing with contiguous substrings. So ccc is not a substring of the string ccxxc.
'''


import sys
from itertools import groupby


class WeightString():
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    d1 = dict([(x[1], x[0]) for x in enumerate(list(s1), start=1)])

    def __init__(self, s):
        self.s = s
        self.weights = self.get_weights_from_string(s)

    def has_weight(self, num):
        if num in self.weights:
            return 'Yes'
        else:
            return 'No'

    def get_weights_from_uni_string(self, s):
        weights = set()
        for i in range(len(s)):
            weights.add(self.d1[s[0]] * (i + 1))

        return weights

    def get_weights_from_string(self, s):
        substr_list = [list(g) for k, g in groupby(s)]
        weights = set()

        for substr in substr_list:
            weights |= self.get_weights_from_uni_string(substr)

        return weights

    def print_weights(self):
        print(self.weights)


x = 'abccddde'

ws = WeightString(x)

for i in range(1, 15):
    print(ws.has_weight(i))

ws.print_weights()
