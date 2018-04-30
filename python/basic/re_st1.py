#!/usr/bin/env python3

import re

ref_url = 'endpoint://endpoint-1/account01/incoming/UPSERT-98234.tsv.gpg'

# pattern = 'endpoint://(\w)'

m = re.search(r"endpoint://(.*?)/(.*)$", ref_url)

print(ref_url)

print(m.groups())
# print(m.groups()[0],m.groups()[1])

l1 = None
for l in l1:
    print(l)

