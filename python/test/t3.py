#!/usr/bin/env python3


import sys

s1='/a/b/c/d'

print(dir(s1))

s2=s1.partition('/')

s3='10020'
print(s3.isdigit())
print(s3.isnumeric())

print(s3.center(10,'-'))