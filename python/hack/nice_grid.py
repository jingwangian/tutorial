#!/usr/bin/env python3

'''
Minimax problem
'''

# rows = 3
# input = [(10, 20, 30), (20, 10, 30), (10, 5, 35)]

# rows = 4
# input = [
#     (1, 1, 3, 4),
#     (5, 1, 1, 8),
#     (9, 10, 1, 1),
#     (1, 14, 15, 1)]

row_list = []
rows = int(input())

for i in range(0, rows):
    row_list.append(tuple([int(x) for x in input().split(' ')]))

# print(row_list)


def nice_grid(rows, row_list):
    output = []

    col_list = []
    for row in range(0, rows):
        col_list.append(tuple([x[row] for x in row_list]))

    max_ri = max([min(x) for x in row_list])
    min_ci = min([max(x) for x in col_list])

    num = 0
    min_num_list = []
    for col in range(0, rows):
        for x in col_list[col]:
            if x > max_ri:
                num += 1
        min_num_list.append(num)
        num = 0

    # print(max_ri)
    # print(min_ci)
    # print(col_list)
    # print(min_num_list)

    return min(min_num_list)

output = nice_grid(rows, row_list)
print(output)
