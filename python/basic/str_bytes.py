#!/usr/bin/env python3

"""
String and bytes study
"""

s1 = 'hello world\n'
# s2 = r'hello world\n'
s2 = '中华人民共和国'
b1 = b'hello world\n'
b2 = br'hello world\n'

# print(s1)
# print(s2)
# print(b1)
# print(b2)

# print(dir(b1))
print(s1)
print('{} has {} "l"'.format(b1, b1.count(b'l')))
print(b2[0])

print(b1.decode())
print(s1.encode())
print(s2)
print(s2.encode())

barray = bytearray(b1)
print(barray)
[print(x, end=',') for x in barray]
print('')
[print(x, end=',') for x in b1]
