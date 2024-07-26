
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("-" * 60)

print("Sachin :", players['sachin'])
print("-" * 60)

print("Sachin :", sum(players['sachin']))
print("-" * 60)

scores = {k :sum(v) for k, v in players.items()}
print(f'scores :{scores}')
print("-" * 60)

scores = [player for player in players.keys()]
print(f"scores :{scores}")
print("-" * 60)

scores = [runs for runs in players.values()]
print(f"scores :{scores}")
print("-" * 60)

test = [{x: (lambda par : "Mr." + par) ("Sachin {}".format(x))}
        for x in range(1, 6)]
print(f"test :{test}")
print("-" * 60)

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

scores = [scr for scr in players.values()]
print(f"scores :{scores}")
print("-" * 60)

scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")
print("-" * 60)

scores = {k: [scr for scr in score if scr > 200]
          for k, score in players.items()}
print(f"scores :{scores}")
