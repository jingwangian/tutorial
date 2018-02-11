#!/usr/bin/env python3


from collections import OrderedDict

n = int(input().strip())

od = OrderedDict()
for i in range(n):
    name, price = input().strip().rsplit(' ', maxsplit=1)
    price = int(price)
    try:
        od[name] = od[name] + price
    except KeyError:
        od[name] = price

[print('{} {}'.format(k, v)) for k, v in od.items()]
