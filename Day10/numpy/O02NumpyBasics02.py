import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(f"arr[0] :{arr[0]}")
print(f"arr[3] :{arr[3]}")
print(f"arr[-1] :{arr[-1]}")

num = 0
for i in range(0, len(arr)):
    num += arr[i]

print(f"Sum of all numbers :{num}")

print(f"{arr[2]} + {arr[3]} = {arr[2] + arr[3]}")

