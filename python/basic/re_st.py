#!/usr/bin/env python3

'''
Identifies:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  any character, except for a newline
\b the whitespace around words
\. a period

Modifiers:
{1,3} a range 1 - 3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of a string
^ Match the beginning of a string
| either or \d{1-3} | \w{5-6}
[] a set. ex: [1-9A-Za-z]
{x} expecting "x" amount

White Space Characters:

\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Method:
match() : only match from the begging of the string
search(): scan through the string and match any position
findall(): Find all substrings matched by RE,return a list
finditer(): same as findall but return a iterator.

DONT FORGET!:
. + * ? [] $ ^ () {} | \



'''
import re


exampleString = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
"""

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)


#*? +? ??
m = re.search(r'a.*b', 'a1ba1234b')
print(m.group())


# Using *? so no greedy
m = re.search(r'a.*?b', 'a1ba1234b')
print(m.group())

m = re.search('a{3,5}', 'aaaaa',)
print(m.group())

m = re.search('a{3,5}?', 'aaaaa',)
print(m.group())

ret = re.findall(r'aa', 'aaababacabbaacaaada')
print(ret)

m = re.search(r'Oscar.*(?P<word>[0-9]{3})', exampleString)
if m is not None:
    print('Oscar is {}'.format(m.group('word')))
else:
    print('Not found')


p = re.compile('a[bcd]*b', re.VERBOSE)
m = p.match('abbcbd')
print(m.group(0))
