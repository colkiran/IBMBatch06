
print("fromkeys".center(60, "-"))
cities = ['blr', 'che', 'hyd', 'del', 'mum', 'kol']
print(f"cities :{cities}")

# convert the list cities into a dictionary
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 23)
print(f"res :{res}")

print("setdefault".center(60, "-"))
emp1 = {'name': 'Mark', 'age': 30, 'desig': 'TL', 'loc': 'Mumbai'}
print(f"emp1 :{emp1}")

print("-" * 60)
emp1.setdefault('name', 'Mike' )
emp1.setdefault('desig', 'MGR')

emp1.setdefault('dept', 'Finance')
emp1.setdefault('salary', 135000)

print(f"emp1 :{emp1}")

print("pop".center(60, "-"))
emp = {'Name': 'Mark', 'age': 30, 'desig': 'TL', 'dept': 'MKT', 'loc': 'Mumbai', 'salary': '85000'}
print(f"emp :{emp}")

print("-" * 60)
res = emp.pop('desig')
print(f"res :{res}")

res = emp.pop('dept')
print(f"res :{res}")

# res = emp.pop()
# print(f"res :{res}")

print(f"emp :{emp}")

print("popitem".center(60, "-"))
emp = {'Name': 'Mark', 'age': 30, 'desig': 'TL', 'dept': 'MKT', 'loc': 'Mumbai', 'salary': '85000'}
print(f"emp :{emp}")

print("-" * 60)
res = emp.popitem()
print(f'res :{res}')

res = emp.popitem()
print(f'res :{res}')

print(f"emp :{emp}")

print("update".center(60, "-"))
emp1 = {'Name': 'Mark', 'age': 30, 'desig': 'TL',  'loc': 'Mumbai', 'salary': '85000'}
print(f"emp1 :{emp1}")

emp2 = {'Name': 'Richard', 'age': 40, 'desig': 'MGR', 'dept': 'Finance', 'loc': 'Chennai'}
print(f"emp2 :{emp2}")

# update emp1 with emp2 values
emp1.update(emp2)
print(f"emp1 :{emp1}")
