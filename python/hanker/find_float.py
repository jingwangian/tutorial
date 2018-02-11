#!/usr/bin/env python


from re import match, compile

#

s1 = '''9
+9%1
5.6
6%7
-6.7
-3**2
+1.3
+7**3
1.4
9**1'''

patt = compile('^[-+]?\d*\.\d+$')
for x in s1.splitlines():
    # print(bool(patt.match(input().strip())))
    print(x)
    print(bool(patt.match(x)))


# patt = compile('^[-+]?\d*.\d+$')
# for x in range(int(input())):
#     print(bool(patt.match(input().strip())))
