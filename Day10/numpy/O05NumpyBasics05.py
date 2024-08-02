import numpy as np

arr = np.array([1, 2, 3, 4])
print(f"arr :\n{arr}")
print(arr.dtype)

print('-' * 60)
arr1 = np.array(['apple', 'orange', 'banana'])
print(f"arr1 :{arr1}")
print(arr1.dtype)

print('-' * 60)
arr2 = np.array([1, 2, 3, 4, 5], dtype="S")
print(arr2)
print(arr2.dtype)

print('-' * 60)
arr2 = np.array([1, 2, 3, 4, 5], dtype="i4")
print(arr2)
print(arr2.dtype)

print('-' * 60)
arr4 = np.array([1.2, 2.5, 3.8, 4.1, 5.7])
print(arr4)
print(arr4.dtype)

newarr = arr4.astype("i")
print(newarr)
print(newarr.dtype)
