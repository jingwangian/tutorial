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

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2.shape  #---> #"""(2, 4)"""

arr2.dtype  # --->  #dtype('int64')

arr3 = np.zeros((2, 3, 2))
# arr3.dtype=np.int64
print(arr3)
"""
[[[0. 0.]
  [0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]
  [0. 0.]]]
"""

arr = np.arange(1,10)
arr2 = np.array(arr)
arr3 = arr[:]

arr2[:] = 100
arr3[:] = 10
print(arr)   #[10 10 10 10 10 10 10 10 10 10]
print(arr2)  #[100 100 100 100 100 100 100 100 100 100]

arr = np.arange(1,10)
arr.shape=(3,3)
print(arr)
print(arr[2], arr[:,1])
print(arr[1:3,1:3])
"""
[[5 6]
 [8 9]]
"""

print(arr[[True,False,True],1:])
print(arr[[True,False,True],[1,1,0]])