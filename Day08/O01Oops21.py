
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):

    def doJob(self):
        print("Developer's Job......")


def BankFun(emp):
    print("Bank job started.......")
    emp.doJob()
    print("Bank job completed.....")
    print("-" * 60)

Mike = Manager()
Dave = Developer()

BankFun(Mike)
BankFun(Dave)