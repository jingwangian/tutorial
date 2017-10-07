#!/usr/bin/env python3


import sys
import time

count = 0


def find_total_substring(s1, s2):
    '''
    Find the total number of s2 in s1.
    Example: s1='aaaab'  s2='aa', number = 3
    Explain: 1st time found is s1[0],s1[1]
             2nd time found is s1[1],s1[2]
             3rd time found is s1[2],s1[3]
    '''

    pos = s1.find(s2)
    if pos != -1:
        try:
            # print('pos is {}'.format(pos))
            return (find_total_substring(s1[pos + 1:], s2) + 1)
        except IndexError:
            return 1
    else:
        return 0


def find_total_substring_v2(s1, s2):
    '''
    Find the total number of s2 in s1.
    Example: s1='aaaab'  s2='aa', number = 3
    Explain: 1st time found is s1[0],s1[1]
             2nd time found is s1[1],s1[2]
             3rd time found is s1[2],s1[3]
    '''

    s1_len = len(s1)
    # s2_len = len(s2)

    total_value = 0
    pos = 0
    end_pos = s1_len - 1

    while (pos < end_pos):
        try:
            # print('pos is {},end_pos is {}'.format(pos, end_pos))
            ret = s1[pos:].find(s2)
        except IndexError:
            break

        if ret != -1:
            total_value += 1
            pos = pos + ret + 1
        else:
            break

    return total_value


def get_dna_value(gen_health_list, d):
    value = 0
    d1 = dict()
    for gen in gen_health_list:
        # if d1.setdefault(gen[0], int(-1)) != -1:
        #     number = d1[gen[0]]
        # else:
        #     # number = find_total_substring_v2(d, gen[0])
        #     number = 1
        #     d1[gen[0]] = number
        number = 2
        value += number * gen[1]

    return value

# n = int(input().strip())
# genes = input().strip().split(' ')
# health = list(map(int, input().strip().split(' ')))
# s = int(input().strip())
# for a0 in range(s):
#     first, last, d = input().strip().split(' ')
#     first, last, d = [int(first), int(last), str(d)]
    # your code goes here


def test_case2():
    with open('dna_input.txt') as f:
        n = f.readline()
        genes = f.readline().strip().split(' ')
        health = list(map(int, f.readline().strip().split(' ')))
        gen_health_list = list(zip(genes, health))
        value = 0
        max_value = 0
        min_value = sys.maxsize

        s = int(f.readline().strip())
        # for a0 in range(s):
        for a0 in range(100):
            first, last, d = f.readline().strip().split(' ')
            first, last, d = [int(first), int(last), str(d)]
            print('start to handle dna {}-{}-{}'.format(first, last, d))
            dna_value = get_dna_value(gen_health_list[first:last + 1], d)
            # dna_value=1
            max_value = max(max_value, dna_value)
            min_value = min(min_value, dna_value)

        print('max_value = {}'.format(max_value))
        print('min_value = {}'.format(min_value))


def test_case1():
    genes = 'a b c aa d b'.split(' ')
    health = [1, 2, 3, 4, 5, 6]
    gen_health_list = list(zip(genes, health))

    s_list = ['1 5 caaab',
              '0 4 xyz',
              '2 4 bcdybc']

    value = 0
    max_value = 0
    min_value = sys.maxsize

    for s in s_list:
        first, last, d = s.split(' ')
        first, last, d = [int(first), int(last), str(d)]
        dna_value = get_dna_value(gen_health_list[first:last + 1], d)
        max_value = max(max_value, dna_value)
        min_value = min(min_value, dna_value)

    print('max_value = {}'.format(max_value))
    print('min_value = {}'.format(min_value))


def main():
    t1 = time.time()
    test_case2()
    t2 = time.time()

    print('finished task using {} seconds'.format(t2 - t1))


if __name__ == '__main__':
    main()
