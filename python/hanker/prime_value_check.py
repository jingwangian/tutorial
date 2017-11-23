#!/usr/bin/env python3



def prime_value_check(num):
    """
    Useing the sqrt(num) time to finish the check
    Return: True --- prime value
            False --- not prime value
    """
    if num == 1:
        return False

    if num <= 3:
        return True

    n = 2
    while (n * n <= num):
        if num % n == 0:
            return False
        n += 1

    return True


T = int(input())

data_list = []
for i in range(T):
    data = int(input())
    data_list.append(data)

for data in data_list:
    if prime_value_check(data):
        print('Prime')
    else:
        print('Not prime')
