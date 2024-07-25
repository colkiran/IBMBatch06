
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))
print("-" * 60)

t2 = (1, 2, 3, 4, 5, 'six', 7.3, 8+4j, True, False)
print(f"t2 :{t2}")
print(type(t2))
print("-" * 60)

t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))
print("-" * 60)

t4 = 10,
print(f"t4 :{t4}")
print(type(t4))
print("-" * 60)

t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))
print("-" * 60)

print("-" * 60)
# print(dir(t1))
t1 = (1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2)
print(f"t1 :{t1}")


print("-" * 60)
# count
print(f"count of '1' :{t1.count(1)}")
print(f"count of '2' :{t1.count(2)}")
print(f"count of '3' :{t1.count(3)}")
print(f"count of '5' :{t1.count(5)}")

print("-" * 60)
# index
print(f"First '3' :{t1.index(3)}")
print(f"Second '3' :{t1.index(3, t1.index(3)+1)}")

