
d1 = dict()
print(f'd1 :{d1}')
print(type(d1))
print("-" * 60)

d2 = {'name': 'sachin', 'age':32, 'runs': 85, 'opppn': "Aus"}
print(f"d2 :{d2}")
print(type(d2))
print("-" * 60)

d3 = dict([('name', 'rahul'), ('age', 29), ('runs', 60), ('oppn', 'pak')])
print(f"d3 :{d3}")
print(type(d3))
print("-" * 60)

d4 = dict(name="Messi", age=37, goals=550, club="Inter Miami")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
# create

player = {'name': 'Sachin', 'age': 32, 'runs': 145, 'oppn': 'WI'}
print(f"player :{player}")
print("-" * 60)

# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modify, add new key, value
print(f"player: {player}")

# modify
player['name'] = "Tendulkar"
player['age'] = 35

# add
player['venue'] = 'Sabina Park'
player['country'] = "India"

print(f"player :{player}")

print("-" * 60)
# delete
print(f"player :{player}")
del player['runs']
del player['age']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
