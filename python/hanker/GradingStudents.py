#!/usr/bin/env python3


import sys


def solve(grades):
    # Complete this function
    for x in grades:
        if x >= 38 and x % 5 >= 3:
            x = x + 5 - (x % 5)

    return map(lambda x: x + 5 - (x % 5) if x >= 38 and x % 5 >= 3 else x, grades)


# n = int(input().strip())
# grades = []
# grades_i = 0
# for grades_i in range(n):
#    grades_t = int(input().strip())
#    grades.append(grades_t)

grades = [73, 67, 38, 33]
result = solve(grades)
print("\n".join(map(str, result)))
