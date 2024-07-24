
print("index".center(60, "-"))

l1 = [1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2,3, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2 ,2, 2, 2, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")
print("-" * 60)

print("first '3' :", l1.index(3))
print("second '3' :", l1.index(3, l1.index(3)+1))

print("count".center(60, "-"))
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")
