
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 60)

ply2 = Player("Sourav", 35)
ply2.get_details()

print("-" * 60)

print("ply1 :", ply1.__dict__)
print("ply2 :", ply2.__dict__)

print("-" * 60)
ply2.runs = 150
print("ply2 :", ply2.__dict__)
print("ply1 :", ply1.__dict__)


"""
self - self will have the name of the object that called the method

def get_detials(self)
    print(self.Name => ply1.Name
    print(self.age  => ply1.age  
    
ply1.get_details() 

self = ply1

every object has a dictionary - __dict__ 
__dict__ = used to store member variables

"""