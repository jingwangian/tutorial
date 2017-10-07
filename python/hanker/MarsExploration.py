#!/usr/bin/env python3

# Birthday Cake Candles

'''
Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of Sami's SOS have been changed by radiation.

Input Format

There is one line of input: a single string, .

Note: As the original message is just SOS repeated times, 's length will be a multiple of .

Constraints

    will contain only uppercase English letters.

Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 0

SOSSPSSQSSOR

Sample Output 0

3

Sample Input 1

SOSSOT

Sample Output 1

1

Explanation

Sample 0

= SOSSPSSQSSOR, and signal length . Sami sent SOS messages (i.e.: ).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR

We print the number of changed letters, which is .

Sample 1

= SOSSOT, and signal length . Sami sent SOS messages (i.e.: ).

Expected Signal: SOSSOS
Received Signal: SOSSOT

We print the number of changed letters, which is .
'''


import sys


def get_error_characters(test_str):
    strlen = len(test_str)
    print(strlen)
    match_str = 'sos' * int(strlen / 3)
    print(len(match_str))
    num = 0
    for i in range(strlen):
        try:
            if test_str[i] != match_str[i]:
                num += 1
        except Exception as e:
            print(e, i)

    return num


test_str = 'sodsesosssossoasosaassxs'

ret = get_error_characters(test_str)

print(ret)
