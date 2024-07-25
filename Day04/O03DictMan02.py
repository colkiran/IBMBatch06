
print("get".center(60, "-"))
player = {'name': 'Cristiano Ronaldo', 'age': 38, 'goals': 600, 'country': 'portuguese'}
print(f"player :{player}")

print(f"Name  :{player.get('name', 'Invalid Key, Please enter a valid key')}")
print(f"Goals :{player.get('goal', 'Invalid Key, Please enter a valid key')}")

print("keys".center(60, "-"))
player = {'name': 'Cristiano Ronaldo', 'age': 38, 'goals': 600, 'country': 'portuguese', 'ballandor': 5, 'club': 'Al-Nassr FC'}
print(f"player :{player}")

print("-" * 60)
kys = player.keys()
print(f"keys :{kys}")

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60,"-"))
player = {'name': 'Lionel Messi', 'age': 37, 'goals': 500, 'country': 'Argentina', 'ballandor': 8, 'club': 'Inter Miami'}
print(f"player :{player}")

print("-" * 60)
vals = player.values()
print(f"Values :{vals}")

print("items".center(60, "-"))
player = {'name': 'Lionel Messi', 'age': 37, 'goals': 500, 'country': 'Argentina', 'ballandor': 8, 'club': 'Inter Miami'}
print(f"player :{player}")

print("-" * 60)
for k, v in player.items():
    print(k, "=>", v)
print("-" * 60)
emp = {
    'emp1' :{'Name': 'Mark', 'age': 30, 'desig': 'TL', 'dept': 'MKT', 'loc': 'Mumbai', 'salary': '85000'},
    'emp2' :{'Name': 'Richard', 'age': 40, 'desig': 'MGR', 'dept': 'Finance', 'loc': 'Chennai', 'salary': 165000},
    'emp3' :{'Name': 'Gracy', 'age': 30, 'desig': 'SE', 'dept': 'IT', 'loc': 'Hyderabad', 'salary': 120000}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)
print(f"emp2 :{emp['emp2']}")
print("-" * 60)
print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)


