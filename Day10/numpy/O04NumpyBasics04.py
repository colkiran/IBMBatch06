import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr[1:5])
print(arr[1:5:2])

# alternate elements from the array
print(f"arr[::2] :{arr[::2]}")

print("two dimension".center(60,"-"))
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr1 :\n{arr1}")
print('-' * 60)

print(f"arr1[1, 1:4] :{arr1[1, 1:4]}")
print('-' * 60)

print(f"arr1[0:2, 2] :{arr1[0:2, 2]}")

print(f"arr1[0:2, 1:4] :{arr1[0:2, 1:4]}")
