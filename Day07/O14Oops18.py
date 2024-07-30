
class Animal:

    def eat(self):
        print('Animals eat......')

class Bird(Animal):
    def fly(self):
        print("Birds fly.......")

class Chicken(Bird):

    def fly(self):
        print("chickes seldom fly.....")


    def message(self):
        print("Chickens are breeded for consumption....")

chic = Chicken()
chic.eat()
chic.fly()
chic.message()
