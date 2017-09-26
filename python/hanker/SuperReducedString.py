#!/usr/bin/env python3
# Super Reduced String
'''
Steve has a string, , consisting of lowercase English alphabetic letters. In one operation, he can delete any pair of adjacent letters with same value. For example, string "aabcc" would become either "aab" or "bcc" after operation.

Steve wants to reduce as much as possible. To do this, he will repeat the above operation as many times as it can be performed. Help Steve out by finding and printing 's non-reducible form!

Note: If the final string is empty, print Empty String .

Input Format

A single string, .

Constraints

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd

Sample Output 0

abd

Sample Case 0

Steve can perform the following sequence of operations to get the final string:

    aaabccddd → abccddd
    abccddd → abddd
    abddd → abd

Thus, we print abd.

Sample Input 1

baab

Sample Output 1

Empty String

Explanation 1

Steve can perform the following sequence of operations to get the final string:

    baab → bb
    bb → Empty String

Thus, we print Empty String.

Sample Input 2

aa

Sample Output 2

Empty String

Explanation 2

Steve can perform the following sequence of operations to get the final string:

    aa → Empty String

Thus, we print Empty String.
'''


def super_reduced_list(str_list):
    print('super_reduced_list is invoked with {}'.format(str_list))
    new_group_list = []

    if not str_list:
        return 'Empty String'

    group_list = [list(g) for k, g in groupby(str_list)]

    if(max([len(x) for x in group_list])) == 1:
        return str_list

    # for group in group_list:
    #     if len(group) % 2 > 0:
    #         new_group_list.extend(list(set(group)))

    [new_group_list.extend(list(set(group))) for group in group_list if len(group) % 2 > 0]

    return super_reduced_list(new_group_list)

    # return new_group_list


def super_reduced_string(s):
    # Complete this function

    ret_list = super_reduced_list(list(s))

    print(ret_list)

    return ''.join(ret_list)



# s = raw_input().strip()
s = 'BCAAAABBBCCBBBDAADCCCBAA'
result = super_reduced_string(s)
print(result)
