
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fname, lname, age):
        print("Factory.....")
        # calls the constructor
        return cls(f"{fname + ' ' + lname}", age)



ply1 = Player("Dhoni",  37)
ply1.get_details()

print("-" * 60)

# create another player wher-e name is like Fname and Lname
ply2 = Player.createPlayer("Sourav", "Ganguly", 34)
ply2.get_details()