#!/usr/bin/env python3

# s = raw_input()

s = 'BANANA'
ln = len(s)
vowels = 'AEIOU'

s.capitalize()

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s) - i)
    else:
        stusc += (len(s) - i)

if kevsc > stusc:
    print("Kevin", kevsc)
elif kevsc < stusc:
    print("Stuart", stusc)
else:
    print("Draw")
