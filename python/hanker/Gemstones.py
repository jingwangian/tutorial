#!/usr/bin/env python3

import sys


'''
Find the common characters in all items in the array
'''

def gemstones(arr):
    # Complete this function

    rocks_composition = [set(x) for x in arr]

    print(rocks_composition)

    s1 = rocks_composition[0]

    for i in range(1, len(rocks_composition)):
        s1 = s1 & rocks_composition[i]

    return len(s1)


arr = [
    'abcdde',
    'baccd',
    'eeabg'
]

result = gemstones(arr)
print(result)
