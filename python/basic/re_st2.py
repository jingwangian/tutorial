#!/usr/bin/env python3
import re
import itertools


passwd='fdsa1fd*sd+-f2'

ret = re.findall(r'[3-9]+', passwd)

print(ret)


ret = re.findall(r'[!@#$%^&*()-+]+', passwd)

print(ret)


def valid_list(s_list):
    l1 = [list(g) for k, g in groupby(s_list)]
    if len(max(l1, key=lambda x: len(x))) > 1:
        return False
    else:
        return True

s='abfasfsadfwfwega233534'
comb='23w5dfs4ge'

fin_list = list(filter(lambda x: x not in comb, s))
print(fin_list)
