#!/usr/bin/env python3


import sys
import re

s = 'saveChangesInTheEditor'

# cret = re.compile('[a-z]+|[A-Z][a-z]+')

# cret.search()

# m = re.findall(r"([a-z]+)|([A-Z][a-z]+) ", "saveChangesInTheEditor")
m = re.findall(r"([a-z]+|[A-Z][a-z]+)", "saveChangesInTheEditor")

if m:
    [print('{}.{}'.format(x[0], x[1])) for x in list(enumerate(m))]
