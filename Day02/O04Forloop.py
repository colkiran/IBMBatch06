
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 21, 2):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(2, 21, 2):
    print(i, end=" ")
print()

print("-" * 60)
for i in range(10, 0, -1):
    print(i, end=" ")
print()

"""
# continue - skip the current iteration
# break - stops the iteration
# else - 
"""
print("-" * 60)

for i in range(1, 31):
    # if i > 20:
    #     break
    if i % 2 == 0:
        continue
    print(i, end= " ")
else:
    print("\n Completed generating numbers....")

