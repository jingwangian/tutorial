#!/usr/bin/env python3

'''
Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, , making it unreadable by his enemies. Given a string, , and a number, , encrypt  and print the resulting string.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Input Format

The first line contains an integer, , which is the length of the unencrypted string.
The second line contains the unencrypted string, .
The third line contains the integer encryption key, , which is the number of letters to rotate.

Constraints


 is a valid ASCII string and doesn't contain any spaces.

Output Format

For each test case, print the encoded string.

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Each unencrypted letter is replaced with the letter occurring  spaces after it when listed alphabetically. Think of the alphabet as being both case-sensitive and circular; if  rotates past the end of the alphabet, it loops back to the beginning (i.e.: the letter after  is , and the letter after  is ).

Selected Examples:
 (ASCII 109) becomes  (ASCII 111).
 (ASCII 105) becomes  (ASCII 107).
 remains the same, as symbols are not encoded.
 (ASCII 79) becomes  (ASCII 81).
 (ASCII 122) becomes  (ASCII 98); because  is the last letter of the alphabet,  (ASCII 97) is the next letter after it in lower-case rotation.
'''

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())


def convert_ascii(s, k):
    s = ord(s)
    k = k % 26
    if (s >= 97 and s <= 122):
        s = s + k
        # print(s, chr(s))
        if(s > 122):
            s = s - 122 + 97 - 1
        return chr(s)
    elif (s >= 65 and s <= 90):
        s = s + k
        if(s > 90):
            s = s - 90 + 65 - 1
        return chr(s)

    return chr(s)


s = 'www.abc.xy'
k = 87
ret = ''.join([convert_ascii(x, k) for x in s])
print(ret)

s = 'DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.'
k = 45
es = 'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.'
ret = ''.join([convert_ascii(x, k) for x in s])
print(ret)
