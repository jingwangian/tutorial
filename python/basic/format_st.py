#!/usr/bin/env python3

"""
format study
"""

li = [12, 45, 78, 784, 2, 69, 1254, 4785, 984]

[print(x) for x in (map('the number is {}'.format, li))]

print('-' * 40)

[print('the number is {}'.format(x)) for x in li]


from datetime import datetime, timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=0, hours=1, minutes=0)

# creat a list
gen = [once_upon_a_time + x * delta for x in range(20)]
print(type(gen))
print(gen)

# creat a generator
gen_1 = (once_upon_a_time + x * delta for x in range(20))
print(type(gen_1))
print(gen_1)

[print(x) for x in gen_1]
# print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))


s1 = (1, 2, 3, 4)
print(type(s1))

s2 = (x * 2 for x in (1, 2, 3, 4))
print(type(s2))
