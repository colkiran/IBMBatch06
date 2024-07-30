from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name :{self.name}\nSalary :{self.salary}"

    # it works even for not equal to (!=)
    def __eq__(self, other):
        return self.salary == other.salary


    # it will work for less than
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("David", 3500)
print(emp1)

print("-" * 60)

emp2 = Employee("Tina", 2500)
print(emp2)

print("-" * 60)

# coparing the addresses where it is stored by default

if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if emp1 < emp2:
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

# it works on salary
print(emp1 >= emp2)
