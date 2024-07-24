
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)

l2 = [1, 2, 3, 4, 5.2, 6.9, 7.4, 8.0, 9 + 2j, 10 -2j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD
# create
cities = ['bangalore', 'chennai', 'hyderabad', 'trivandrum', 'delhi']
print(f"cities :{cities}")

print("-" * 60)
# read
print(f"cities[0] :{cities[0]}")
print(f"cities[2] :{cities[2]}")

# iterate
for city in cities:
    print(city, end=" ")
print()

for i in range(0, len(cities)):
    print(cities[i], end=" ")
print()

print("-" * 60)
# update - modify the name or add a new value to the list

# modify
print(f"cities :{cities}")
cities[1] = "madras"
cities[3] = 'mumbai'

print(f"cities :{cities}")

# add new values
cities[4] = "Kolkota"
cities[3] = "pune"
print(f"cities :{cities}")

print("-" * 60)
# delete
del cities[4]
del cities[3]

print(f"cities :{cities}")

