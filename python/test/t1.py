#!/usr/bin/env python3


'''
input:
4
a a c d
2
'''
import re

import string

CHARACTERS = list(string.ascii_letters) + [""]

print(CHARACTERS)
print(CHARACTERS.index('c'))

CHARACTERS.reverse()
