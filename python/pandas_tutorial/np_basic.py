#!/usr/bin/env python3
import numpy as np
import os

data1 = [6, 7.5, 8, 0, 1]

arr1 = np.array(data1)

l1 = list(arr1)

print(arr1)

print(l1)


x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print(x2)
v2 = x2[:1,:1]
v1 = x2[1,1]
print(v1,type(v1))
print(v2,type(v2),v2.ndim, v2.shape)
print(x2[:2,:2])

arr2 = arr1.astype(np.int64)
arr2.sort()

print(arr2.shape, arr2.ndim, arr2)