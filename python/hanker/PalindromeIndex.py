#!/usr/bin/env python3

# Palindrome Index

import sys


def is_palindrome_string(s):
    rev_s = list(reversed(s))

    if rev_s == s:
        return True
    else:
        return False


def palindromeIndex(s):
    # Complete this function

    s1 = list(s)
    s2 = list(reversed(s1))

    for i in range(len(s1) - 1):
        if s1[i] != s2[i]:
            s3 = s1.copy()
            s3.pop(i)
            if is_palindrome_string(s3) == True:
                return i
            else:
                return len(s1) - i - 1

    return -1


s = 'quyjjdcgsvvsgcdjjyq'
s = 'hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh'
s = 'aaab'
s = 'baa'
s = 'aaa'
result = palindromeIndex(s)
print(result)


# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     result = palindromeIndex(s)
#     print(result)


'''
10
quyjjdcgsvvsgcdjjyq
hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh
fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf
bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb
fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf
mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm
tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt
lhrxvssvxrhl
prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp
kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk
'''
