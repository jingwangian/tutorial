#!/bin/python3

import sys
import time
from get_divisor import print_divisor_list


def gcd(a, b):
    while a != 0:
        a, b = b % a, a

    return b


def maximumGcdList(A, B):
    """
    Return pair_list contains maximumGcd pair
    """
    max_gcd_value = 1
    pair_list = []

    for x in A:
        for y in B:
            print(x, y)

    return [(10, 10)]

    for x in A:
        if x < max_gcd_value:
            break
        for y in B:
            if y < max_gcd_value:
                break
            gcd_value = gcd(x, y)
            print('gcd_value({},{}) = {}'.format(x, y, gcd_value))
            if gcd_value == max_gcd_value:
                pair_list.append((x, y))
            elif gcd_value > max_gcd_value:
                max_gcd_value = gcd_value
                pair_list.clear()
                pair_list.append((x, y))

    return pair_list


def maximumGcdAndSum(A, B):
    # Complete this function

    # max_a = max(A)
    # max_b = max(B)

    t1 = time.time()
    A = list(set(A))
    A.sort()
    A.reverse()
    print('A finished reverse cost {}'.format(time.time() - t1))

    print('A len = {}'.format(len(A)))

    t1 = time.time()
    B = list(set(B))
    B.sort()
    B.reverse()
    print('B finished reverse cost {}'.format(time.time() - t1))
    print('B len = {}'.format(len(B)))

    # print(A)
    # print(B)

    pair_list = maximumGcdList(A, B)

    max_pair = max(pair_list, key=lambda x: x[0] + x[1])

    return sum(max_pair)


def read_from_file(file_name):
    with open(file_name, 'r') as f:
        f.readline()
        A = list(map(int, f.readline().strip().split(' ')))
        B = list(map(int, f.readline().strip().split(' ')))

    return A, B


if __name__ == "__main__":
    # n = int(input().strip())
    # A = list(map(int, input().strip().split(' ')))
    # B = list(map(int, input().strip().split(' ')))

    # A = list(map(int, "4 8 4 4 4 4".split(' ')))
    # B = list(map(int, "4 12 4 4 4 4".split(' ')))

    A, B = read_from_file('input19.txt')
    res = maximumGcdAndSum(A, B)
    print(res)

    # t1 = time.time()
    # print_divisor_list(A)
    # print('print_divisor_list cost {}'.format(time.time() - t1))
