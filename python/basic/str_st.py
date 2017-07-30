#!/usr/bin/env python3

'''
str study

Methods:
__add__,__class__,__contains__,__delattr__,__dir__,__doc__,__eq__,__format__
__ge__,__getattribute__,__getitem__,__getnewargs__,__gt__,__hash__,__init__,__iter__
__le__,__len__,__lt__,__mod__,__mul__,__ne__,__new__,__reduce__
__reduce_ex__,__repr__,__rmod__,__rmul__,__setattr__,__sizeof__,__str__,__subclasshook__
capitalize,casefold,center,count,encode,endswith,expandtabs,find
format,format_map,index,isalnum,isalpha,isdecimal,isdigit,isidentifier
islower,isnumeric,isprintable,isspace,istitle,isupper,join,ljust
lower,lstrip,maketrans,partition,replace,rfind,rindex,rjust
rpartition,rsplit,rstrip,split,splitlines,startswith,strip,swapcase
title,translate,upper,zfill,

capitalize(): Return a copy of the string with its first character capitalized and the rest lowercased.
casefold(): Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
center(width,fillchar):Return centered in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
count(sub[, start[, end]]): Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

expandtabs(tabsize=8): Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size

index(sub) : Like find but rasise ValueError if not found

isalnum():
isalpha():
isdecimal():
isnumeric():
isprintable():
isspace():
istitle():
isupper():
join(iter):

lower():
upper():

lstrip():
strip(chars): Remove char if in chars and continue remove next. if not find in chars then stop.


replace():Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

rfind(sub[, start[, end]]):Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end].
rindex(sub[, start[, end]]):

ljust():Return the string left justified in a string of length width.
rjust(width[, fillchar]):

partition():
rpartition(sep):

swapcase(): uppercase swap with lowercase

rsplit(sep=None, maxsplit=-1):
split(sep=None, maxsplit=-1):
splitlines()

maketrans():
translate(table)


zfill(width):Return a copy of the string left filled with ASCII '0' digits to make a string of length width. A leading sign prefix ('+'/'-') is handled by inserting the padding after the sign character rather than before. The original string is returned if width is less than or equal to len(s).
'''

s1 = 'hello world china people, lllleedd'
s2 = 'WHAT YOU ARE REALLY MEANT TO DO'
s3 = '中国中国美丽的祖国'

print(s1.capitalize())
print(s2.casefold())

# center
print(s1.center(len(s1) + 3, 'y'))
print('count of ll in s1:', s1.count('ll'))

print('中'.encode(encoding="utf-16", errors="strict"))
print('中'.encode(encoding="utf-8", errors="strict"))
print('s3:', s3)
sb1 = s3.encode(encoding="utf-16", errors="strict")
sb2 = s3.encode(encoding="utf-8", errors="strict")
print(sb1)
print(sb2)

# expandtabs
print('12345678' * 4)
print('01\t012\n\t0123\t01234'.expandtabs())
print('01\t012\t0123\t01234'.expandtabs(4))

# Using Format
d1 = dict(name='Guido', country='German')
print(d1)
print('{name} was born in {country}'.format(**d1))
print('{name} was born in {country}'.format_map(d1))

print('www.exam.ple.com'.strip('cmowz.'))

# swapcase
print('abcdABCDKKll'.swapcase())
# title
print(s1.title())

# translate
mpt = str.maketrans('abcd', 'ABCD')
print(mpt)
print(s1.translate(mpt))

# partition
print(s1.partition('china'))
#--->('hello world ', 'china', ' people, lllleedd')

print('abcdabcd'.find('cd'))
print('abcdabcd'.rfind('cd'))

# just and rjust
print('abcd'.rjust(10, '-'))
#--->------abcd
print('abcd'.ljust(10, '*'))
#--->abcd******

# split
print('abcdabcdefcdxxcd'.split('cd'))
print('abcdabcdefcdxxcd'.split('cd', maxsplit=1))
print('abcdabcdefcdxxcd'.rsplit('cd', maxsplit=1))

"""
If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
"""
print('   1   2   3   \n 4 \t5  \r 6'.split())
print('   1   2   3   \n 4 \t5  \r 6'.split())
print('   1   2   3   \n 4 \t5  \r 6\r\n'.splitlines())
print('   1   2   3   \n 4 \t5  \r 6\r\n'.splitlines(True))

print('Two lines\n'.split())
print('Two lines\n'.split('\n'))
print('Two lines\n'.splitlines())


# startswith
print("hello world".startswith('hell'))

# upper and lower
print('s1.upper():', s1.upper())
print('s2.lower():', s2.lower())


#isalnum, isalpha, isdigit
def isis(s5):
    print('"{}":\t\t{}\t{}\t{}\t{}'.format(s5, s5.isalnum(), s5.isdigit(), s5.isalpha(), s5.isnumeric()))

print('str   \t\tisalnum\tisdigit\tisalpha\tisnumeric')
s5 = '111'
isis(s5)
s5 = '11AB'
isis(s5)
s5 = '0xab'
isis(s5)
s5 = '111t'
isis(s5)
s5 = 'abcd'
isis(s5)

# join
print('--'.join(str(x) for x in [1, 2, 3, 4]))

# print(sb1.decode(encoding="utf-8"))

# def f(n):
#     return ',' if n % 8 > 0 else None
# # print(dir(d1))
# [print(x, end=f(i + 1)) for i, x in (enumerate(dir('s1')))]
