#!/usr/bin/env python3

import re


s1 = 'username@websitename.com'
s2 = '''
5
its@gmail.com1
mike13445@yahoomail9.server
rase23@ha_ch.com
daniyal@gmail.coma
thatisit@thatisit
'''

# m = re.match(r'^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s1)
# m = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s1)
# print(m)


def fun(s):
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
    return bool(a)


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
