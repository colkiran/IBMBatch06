
values = list(range(10, 40, 10))
print(f"values :{values}")

# upack the list
a, b, c = values
print(a, b, c, sep=", ")

values = list(range(10, 101, 10))
print(f"values :{values}")
# any variable prefixed with a *, it can store more than one value
a, b, *c = values
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]
print(f"l1 :{l1}")
print(f"l2 :{l2}")

l3 = [l1, l2]
print(f"l3 :{l3}")
print(len(l3))
print("-" * 60)

l4 = [*l1, *l2]         # unpack
print(f"l4 :{l4}")
print(len(l4))

print("-" * 60)
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()
print("-" * 60)

for letter in enumerate(letters):
    print(letter, " ",  end=" ")
print()

print("-" * 60)

for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)

for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 60)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")
print("-" * 60)

for ind, lst in enumerate(mylist):
    print(ind, lst)
print("-" * 60)

for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
print("-" * 60)
l1= []
print(dir(l1))
