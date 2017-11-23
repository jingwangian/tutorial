#!/usr/bin/env python3


import csv
import datetime
# [print(x) for x in s1_list]

# print(' '.join(map(lambda x: '0x{}'.format(x), s1.split())))

file_name = '/db/bitbucket/flightv3/node/src/script/route.csv'
new_file_name = '/db/bitbucket/flightv3/node/src/script/route_new.csv'


with open(file_name) as f, open(new_file_name, 'w') as nf:
    csv_data = csv.reader(f)
    csv_writer = csv.writer(nf)

    # [csv_writer.writerow([x[0], x[2], x[3]]) for x in csv_data]

    route_list = [[x[0], x[2], x[3]] for x in csv_data][1:]

    # print(route_list)

    route_list.sort(key=lambda x: int(x[0]))

    [print(x) for x in route_list]

    csv_writer.writerow(['id', 'from_city_id', 'to_city_id'])
    [csv_writer.writerow(x) for x in route_list]


# with open(new_file_name, 'w') as nf:
#     csv_writer = csv.writer(nf)

#     [csv_writer.writerow([str_tmp.format('var', x)]) for x in range(1, 13)]
#     [csv_writer.writerow([str_tmp.format('array', x)]) for x in range(1, 13)]
#     [csv_writer.writerow([str_tmp.format('pvar', x)]) for x in range(1, 13)]

# print("finish write rows into {}".format(new_file_name))
