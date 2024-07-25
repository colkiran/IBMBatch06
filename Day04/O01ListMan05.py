
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1     # shallow copy - copies the address along with the data
print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
print("=" * 60)

l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")

# copy the list l3 to l4
l4 = l3.copy()      # Deep copy - onlu the data gets copied
print(f"l4 before :{l4}")

l4.append(60)
l4.append(70)
l4.append(80)

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
print("=" * 60)

l5 = [1, 2, 3, [2, 4, 6, 8], 4, 5]
print(f"l5 before :{l5}")

# copy the list l5 to l6
l6 = l5.copy()      # deep copy
print(f"l6 before :{l6}")

l6[3].append(10)
l6[3].append(12)
l6[3].append(14)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
print("=" * 60)

l7 = [1, 2, ['aa', 'bb', 'cc'], 3, 4, 5]
print(f"l7 before :{l7}")

from copy import deepcopy
# copy the list l7 to l8
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[2].append('dd')
l8[2].append("ee")
l8[2].append('ff')

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(60, "-"))
l1 = [10, 8, 5, 1, 7, 3, 9, 1, 4, 2]
print(f"l1 :{l1}")

# sort the list l1
"""
1. sort - sort will sort the origal list

2. sorted - sorted will take a copy of the list and sort it 
"""

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"descending :{res_desc}")

print("-" * 60)
l1 = [10,'zebra', 'apple', 8, 'yellow', 'blue', 5, 'xray', 'green', 1, 'violet', 'maroon', 7, 'white', 'orange', 3, 'cat', 'dog', 9, 'egg', 'umbrella', 'queen',  4, 'king', 2, 190, 1765, 29, 275, 2523]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
# for i in range(0, len(res)):
#     if type(res[i]) == int:
#         print(i)
#         break

print(res[0:18] + sorted(res[17:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'bangalore', 'chennai', 'ooty', 'vishakapatnam', 'hyderabad', 'madurai', 'mumbai', 'delhi', 'kolkata']

print(f"cities :{cities}")
print("-" * 60)

res = sorted(cities, key=len)
print(f"res :{res}")


print("reverse".center(60, "-"))

l1 = [10, 8, 5, 1, 7, 3, 9, 1, 4, 2]
print(f"l1 :{l1}")

l1.reverse()
print(f"l1 :{l1}")




