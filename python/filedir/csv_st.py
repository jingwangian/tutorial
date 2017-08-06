#!/usr/bin/env python3

'''
csv study

class:
    DictReader
    DictWriter

functions:
    csv.reader : return a object reader
    csv.writer : return a object writer

object: reader, writer,

Dialect ??

Dialect,DictReader,DictWriter,Error,
QUOTE_ALL,QUOTE_MINIMAL,QUOTE_NONE,QUOTE_NONNUMERIC
Sniffer,StringIO,
_Dialect,__all__,__builtins__,__cached__,__doc__,__file__
__loader__,__name__,__package__,__spec__,__version__,
excel,excel_tab,field_size_limit,get_dialect,list_dialects,re,reader,
register_dialect,unix_dialect,unregister_dialect,writer
'''

import csv


# Use the csv.reader to read the content in csv
with open('city.csv') as f:
    csv_data = csv.reader(f)

    # next(csv_data)
    [print('{}, {}, {}, {}'.format(x[0], x[1], x[2], x[3])) for x in csv_data]


# Use the DictReader to read the content in csv, each item is a dict, keys is the fieldname and value is the content
with open('city.csv') as f:
    csv_data = csv.DictReader(f)

    # next(csv_data)
    # [print('{}, {}, {}, {}'.format(x['id'], x['name'], x['short_name'], x['url_name'])) for x in csv_data]
    [print(k, end='\t') for k in csv_data.fieldnames]
    print(' ')
    # print(csv_data.fieldnames)
    # print(dir(csv_data))
    [print('{id}, {name}, {short_name}, "{url_name}"'.format(**x)) for x in csv_data]


# write (1,100,200) as a row into a.csv file
list1 = list(zip(range(1, 100), range(100, 200), range(200, 300)))
with open('a.csv', 'w') as f:
    writer = csv.writer(f)

    # Here write a field name
    writer.writerow(('id', 'number', 'price'))

    # start to write rows
    writer.writerows(list1)


# def printkey(obj):
#     def f(n):
#         return ',' if n % 8 > 0 else None
#     [print(x, end=f(i + 1)) for i, x in (enumerate(dir(obj)))]
#     print('')

# printkey(csv)
