#!/usr/bin/env python3

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    need_number = 0

    ret = re.findall(r'[0-9]+',password)
    if len(ret) == 0:
        need_number += 1

    if len(re.findall(r'[a-z]+',password))==0:
        need_number += 1

    if len(re.findall(r'[A-Z]+',password))==0:
        need_number += 1

    if len(re.findall(r'[!@#$%^&*()\-+]',password))==0:
        need_number += 1

    return max(6-len(password),need_number)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())

    # password = input()
    password = 'AUzs-nV'

    answer = minimumNumber(len(password), password)

    print(answer)

