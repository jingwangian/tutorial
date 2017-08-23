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

re.search --->_sre.SRE_Match
['end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']

(...)
    Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the \number special sequence, described below. To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(] [)].

(?=...)
    Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

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


print('?')
m = re.search(r'\w*(?=is 15)', exampleString)
print(m.group(0))


m = re.search(r'(aa)', 'x1aaababacabbaacaaada')
print(m.pos, m.string, m.start(), m.span())
print(m.groups())

# unamed group
print('''\n---re.search(r'^/articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', '/articles/2003/03/03/') --- ''')
m = re.search(r'^/articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', '/articles/2003/03/03/')
print(m.pos, m.string, m.start(), m.span())
print("m.groups()-->",m.groups())
print("m.groupdict()-->",m.groupdict())

# named group
print("""\n---re.search(r'^/articles/(?P<year>\d+)/(?P<month>\d+)/$', '/articles/2003/10/')--- """)
m = re.search(r'^/articles/(?P<year>\d+)/(?P<month>\d+)/$', '/articles/2003/10/')
print(m.pos, m.string, m.start(), m.span())
print(m.group('year'))
print("m.groups()-->",m.groups())
print("m.groupdict()-->",m.groupdict())
print(m.groupdict().items())
[print((k,m.group(k))) for k in m.groupdict()]

# groups
print('''\n---re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")---''')
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print('''len(m.groups())-->''',len(m.groups()))
print('''m.groups()-->''',m.groups())
[print('''m.group({})-->{}'''.format(x,m.group(x))) for x in range(0,len(m.groups())+1)]


print('''\n---re.match(r"(\w+) ", "Isaac Newton physicist abc")---''')
m = re.match(r"(\w+) ", "Isaac Newton, physicist abc")
print('''len(m.groups())-->''',len(m.groups()))
print('''m.groups()-->''',m.groups())
[print('''m.group({})-->{}'''.format(x,m.group(x))) for x in range(0,len(m.groups())+1)]


print('''\n---re.match("\w+", "Isaac Newton, physicist abc")---''')
m = re.match("\w+", "Isaac Newton, physicist abc")
print('''len(m.groups())-->''',len(m.groups()))
print('''m.groups()-->''',m.groups())
[print('''m.group({})-->{}'''.format(x,m.group(x))) for x in range(0,len(m.groups())+1)]
