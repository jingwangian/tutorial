#!/usr/bin/env python3


import csv
<<<<<<< HEAD
import datetime
# [print(x) for x in s1_list]

# print(' '.join(map(lambda x: '0x{}'.format(x), s1.split())))

file_name = '/media/sf_hostshare/1/a.csv'
new_file_name = '/media/sf_hostshare/1/a_new.csv'

str_tmp = r'''SET PATH = C: \fep\fsepv95client64\lib
C: \fep\fsepv95client64\bin
C: \fep\fsepv95client64\include
%PATH%
SET PGHOST = 10.44.37.33
SET PGUSER = wangj
SET PGCLIENTENCODING = UTF8
test File: uvarchar.pgc
test function: test_{}_{}'''
=======

>>>>>>> ccba8f3086287825e562227c5e27efb92fe677da

# with open(file_name) as f:
#     csv_data = csv.reader(f)

#     [print(x[0]) for x in csv_data]


# with open(new_file_name, 'w') as nf:
#     csv_writer = csv.writer(nf)

#     [csv_writer.writerow([str_tmp.format('var', x)]) for x in range(1, 13)]
#     [csv_writer.writerow([str_tmp.format('array', x)]) for x in range(1, 13)]
#     [csv_writer.writerow([str_tmp.format('pvar', x)]) for x in range(1, 13)]

# print("finish write rows into {}".format(new_file_name))


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11],
]

# print([[item[i] for item in matrix] for i in range(0, 4)])

print(list(zip(*matrix)))

d1 = dict(name='wangj')
d1[(1, 2)] = 30

d1[(2, 1)] = 40

d1[(1, 2, 5)] = 30
print(d1)

a = set('abracadabra')
b = set('alacazam')

print("a-b")
print(a - b)

print("b-a")
print(b - a)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(sorted(set(basket)))

print(list(reversed(sorted(set(basket)))))

print(dir(slice(1, 10)))
<<<<<<< HEAD
print(slice(1, 10))

import os
p1 = os.getcwd()
print(p1)
print(os.path.abspath(p1))

file1 = '../v3/results/flight_1_5._xt'

file2 = '../v3/results/flight_1_5'
file3 = '../v3/results/flight_1_5/'

print(os.path.split(file1))
print(os.path.split(file2))
print(os.path.split(file3))

print(os.path.splitext(file1))
print(os.path.splitext(file2))
print(os.path.splitext(file3))

finalname = '{}.txt'.format(os.path.splitext(file1)[0])
print(finalname)
print(finalname[-4:])
=======
l1 = slice(1, 10)
print(l1)

a = [1, 2, 3, 4, 5]
sliceObj = slice(1, 3)
a[sliceObj]
>>>>>>> ccba8f3086287825e562227c5e27efb92fe677da
