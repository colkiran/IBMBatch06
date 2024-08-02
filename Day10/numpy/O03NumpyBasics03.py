
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("dimension :", arr.ndim)

print(f"arr :\n{arr}")
print(f"first row fourth element :{arr[0, 3]}")
print(f"second row third element :{arr[1, 2]}")

print("-" * 60)

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"arr1 :\n{arr1}")

print(f"arr1[0, 1, 2] :{arr1[0, 1, 2]}")
print(f"arr1[1, 0, 1] :{arr1[1, 0, 1]}")

