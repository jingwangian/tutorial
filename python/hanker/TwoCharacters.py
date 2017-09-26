#!/usr/bin/env python3

# Two Characters
'''

'''

import sys
from itertools import combinations
from itertools import dropwhile
from itertools import groupby


def valid_list(s_list):
    l1 = [list(g) for k, g in groupby(s_list)]
    if len(max(l1, key=lambda x: len(x))) > 1:
        return False
    else:
        return True


def get_max_tstring_len(s):
    set_s = set(s)

    if len(set_s) < 2:
        return 0
    elif len(set_s) == 2:
        if valid_list(list(s)):
            return len(list(s))
        else:
            return 0
    else:
        comb_list = list(combinations(set_s, len(set_s) - 2))
        max_num = 0
        for comb in comb_list:
            fin_list = list(filter(lambda x: x not in comb, s))
            if valid_list(fin_list):
                if len(fin_list) > max_num:
                    max_num = len(fin_list)

        return max_num


n = 10
s = 'beabeefeab'
s = 'a'

result = get_max_tstring_len(s)
print(result)
