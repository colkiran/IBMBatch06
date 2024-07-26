
fruits = [
    ('apple', 285),
    ('orange', 110),
    ('banana', 65),
    ('pine apple', 80),
    ('gauva', 120),
    ('grapes', 160),
    ('Mango', 220),
    ('watermelon', 70)
]

print(f"fruits :{fruits}")
print("-" * 60)

prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

expn_frts = [fruit for fruit in fruits if fruit[1] > 100]
print(f"Expensive Fruits :{expn_frts}")
print("-" * 60)

expn_frts = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
              for fruit in fruits if fruit[1] > 100]
print(f"Expensive Fruits :{expn_frts}")
print("-" * 60)

setence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{setence}")

words = [word for word in setence.split()]
print(f"words :{words}")
print("-" * 60)

words = [word for word in setence.split() if word != 'the']
print(f"words :{words}")
print("-" * 60)

words = [(word, len(word)) for word in setence.split() if word != 'the']
print(f"words :{words}")
print("-" * 60)

