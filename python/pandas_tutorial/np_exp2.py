#!/usr/bin/env python3
import numpy as np

"""
Function

"""
array_1 = np.random.randn(2, 3)

"""
array([[-0.2047,  0.4789, -0.5194],
[-0.5557, 1.9658, 1.3934]])
"""

arr1 = np.array([6, 7.5, -8, 0, 1,12])

arr2 = np.array([3,5,7,4,2,3])

arr3 = np.array([8,4,5,2,3,0])

max_arr = np.maximum(arr1,arr2)
print(max_arr)

print(arr1)
print(np.abs(arr1))

points = np.arange(-5, 5, 1)

print(points)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

a1 = arr.cumsum(axis=0)

a2 = arr.cumsum(axis=1)

print(a1)
print(a2)