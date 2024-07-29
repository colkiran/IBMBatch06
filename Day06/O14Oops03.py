
class Player:

    def __init__(self):
        self.name = "Sachin"        # member variable
        self.age = 32
        print("Player Initialized......")

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

ply1 = Player()
ply1.get_details()
print("-" * 60)

ply2 = Player()

# only in python
ply2.name = "Rahul"
ply2.age = 29

ply2.get_details()
