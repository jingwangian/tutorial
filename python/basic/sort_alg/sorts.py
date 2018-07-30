#!/usr/bin/env python3


def bubble_sort(q):
    lastIndex = len(q) - 1
    swaps = 0
    swaped = False

    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        print("i = ", i)
        for j in range(0, lastIndex):
            a, b = q[j], q[j + 1]
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                swaps += 1
                swaped = True

            print(q, "{} --{}, swap = {}".format(a, b, 'True' if a > b else 'False'))

        if swaped:
            swaped = False
        else:
            break
    return swaps


def consecutive_minimum_swaps(arr):
    arr_len = len(arr)
    swaps = 0

    i = 0
    print(arr, 'swaps = {}'.format(swaps))
    for i in range(0, arr_len - 1):
        if arr[i] == i + 1:
            continue

        t = i

        while(arr[t] != i + 1):
            t += 1

        arr[i], arr[t] = arr[t], arr[i]
        swaps += 1

        print(arr, 'swaps = {}'.format(swaps))

    return swaps


def non_consecutive_minimum_swaps(arr):
    arr_len = len(arr)
    swaps = 0

    i = 0
    print(arr, 'swaps = {}'.format(swaps))
    for i in range(0, arr_len - 1):
        a = arr[i]
        swap_index = i
        if arr[i] == i + 1:
            continue

        for j in range(i + 1, arr_len):
            if arr[j] < a:
                swap_index = j
                a = arr[j]

        if i != swap_index:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swaps += 1

        print(arr, 'swaps = {}'.format(swaps))

    return swaps
