#!/usr/bin/env python3

import sys


def is_pangram(s1):
    # Complete this function
    if set('pangram') <= set(s1):
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == "__main__":
    s1 = input().strip().lower()
    l1 = [x for x in set(s1) if len(x.strip()) > 0]
    if len(l1) == 26:
        print('pangram')
    else:
        print('not pangram')


We promptly judged antique ivory buckles for the next prize
We promptly judged antique ivory buckles for the prize
