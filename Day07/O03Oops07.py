
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @staticmethod
    def StrikeRate(runs, balls):
        return  round((runs / balls) * 100, 2)



ply1 = Player("Dhoni",  37)
ply1.get_details()

print("Strike Rate :", Player.StrikeRate(150, 89))
