#!/usr/bin/env python3

from sorts import bubble_sort, consecutive_minimum_swaps, non_consecutive_minimum_swaps


ret = consecutive_minimum_swaps([7, 3, 8, 4, 1, 5, 2, 6])
print(ret)

ret = non_consecutive_minimum_swaps([1, 3, 5, 4, 6, 9, 8])
print(ret)
# ret = bubble_sort([7, 1, 3, 2, 4, 5, 6])
# print(ret)
