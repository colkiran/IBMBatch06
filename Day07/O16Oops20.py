
from abc import ABC, abstractmethod

class Account(ABC):

    def __int__(self):
        print("Account....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):
    def deposit(self):
        print("Amount credited.....")

    def getBalance(self):
        print("Amount in the account is #######")


sav1 = Savings()
sav1.getBalance()
sav1.deposit()