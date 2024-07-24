
print("append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
# l1 :[1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11, 12, 13]]
# print - 10, 11, 12
print(l1[8][1:4])
print(l1[-1][1:4])

print("extend".center(60, "-"))
l1 = [6, 7, 8, 9, 10]
print(f"l1 :{l1}")

l1.extend([11, 12, 13, 14, 15])
print(f"l1 :{l1}")

l1.extend([16])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")

l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)

print(f"l2 :{l2}")

print("remove".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.remove(1)
l1.remove(3)
l1.remove(5)

print(f"l1 :{l1}")

# l1.remove(1)
l1 = [1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1,1, 1, 1, 2,2 ,2, 2,2,2,2,2,2,2,2]

# for i in l1:
#     if i == 2:
#         l1.remove(2)

while 2 in l1:
    l1.remove(2)

print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

# pop will work on idexes
res = l1.pop(3)
print(res)

res = l1.pop(7)
print(res)

res = l1.pop(-2)
print(res)

print(f"l1 :{l1}")
res = l1.pop()
print(res)

print(f"l1 :{l1}")
# l1.pop(10)

print("clear".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")