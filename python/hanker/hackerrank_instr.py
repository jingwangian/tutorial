#!/usr/bin/env python3

# hankerrank

'''
We say that a string, , contains the word hackerrank if a subsequence of the characters in spell the word hackerrank. For example, haacckkerrannkk does contain hackerrank, but haacckkerannk does not (the characters all appear in the same order, but it's missing a second r).

More formally, let be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If is true, then contains hackerrank.

You must answer queries, where each query consists of a string, . For each query, print YES on a new line if contains hackerrank; otherwise, print NO instead.

Input Format

The first line contains an integer denoting (the number of queries).
Each line of the subsequent lines contains a single string denoting .

Constraints

Output Format

For each query, print YES on a new line if contains hackerrank; otherwise, print NO instead.

Sample Input 0

2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO

Explanation 0

We perform the following queries:


    The characters of hackerrank are bolded in the string above. Because the string contains all the characters in hackerrank in the same exact order as they appear in hackerrank, we print YES on a new line.
    does not contain the last three characters of hackerrank, so we print NO on a new line.
'''


import sys

# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
# your code goes here


hancker_str = 'hackerrank'


def hackerrank_in_str(s):
    '''
    Check 'hackerrank' is in S or not
    Return True if it is in s
    '''
    for i in range(len(hancker_str)):
        pos = s.find(hancker_str[i])
        if pos >= 0:
            s = s[pos + 1:]
        else:
            return False

    return True


ret = hackerrank_in_str('haccckkerrraankers')
print(ret)

ret = hackerrank_in_str('hackeeerxxaank')
print(ret)
