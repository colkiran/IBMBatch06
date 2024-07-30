
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):
        super().__init__()          # calls the parent class Ctor
        self.weight = '1k'
        print("Bird Ctor......")

    def fly(self):
        print("Birds fly.....")

cuckoo = Bird()
cuckoo.fly()
print(cuckoo.__dict__)

