
print("copy".center(60, "-"))
emp1 = {'Name': 'Mark', 'age': 30, 'desig': 'TL',  'loc': 'Mumbai'}
print(f'emp1 before :{emp1}')

# copy the dictionary emp1 to emp2
emp2 = emp1     # shallow copy - copies the address along with the data
print(f"emp2 before :{emp2}")

emp2['dept'] = 'Finance'
emp2['salary'] = 150000

print("-" * 60)
print(f"emp2 after :{emp2}")

print("=" * 60)
print("=" * 60)
ply1 = {'name': 'virat', 'age' :34, 'runs': 86, 'oppn': 'NZL'}
print(f"player before :{ply1}")

# copy dictionary ply1 to ply2
ply2 = ply1.copy()
print(f"ply2 before {ply2}")

ply2['venue'] = "Auckland"
ply2['country'] = 'India'

print(f"ply2 after :{ply2}")
print(f'ply1 after :{ply1}')

print("=" * 60)
print("=" * 60)

ply1 = {'name': 'virat', 'age' :34, 'runs': {'aus': 65, 'pak': 105, 'sri': 38}, 'tournament': 'Asia Cup'}
print(f"player before :{ply1}")

# copy dictionary ply1 to ply2
ply2 = ply1.copy()
print(f"ply2 before :{ply2}")

ply2['runs']['afg'] = 85
ply2['runs']['bng'] = 120

print(f"ply2 after :{ply2}")
print(f"ply1 after :{ply1}")

print("=" * 60)
print("=" * 60)

ply1 = {'name': 'virat', 'age' :34, 'runs': {'aus': 65, 'pak': 105, 'sri': 38}, 'tournament': 'Asia Cup'}
print(f"ply1 before :{ply1}")

# copy dictionary ply1 to ply2
from copy import deepcopy
ply2 = deepcopy(ply1)       # deep copy
print(f"ply2 before :{ply2}")

ply2['runs']['afg'] = 85
ply2['runs']['bng'] = 120

print(f"ply2 after :{ply2}")
print(f"ply1 after :{ply1}")
