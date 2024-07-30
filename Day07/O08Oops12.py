
class Employee:
    def __init__(self, name):
        self.__name = name
        self.tech = ['C', 'C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'Angular', 'React']

    def __str__(self):
        return self.__name + " " + ", ".join([str(v) for v in self.tech])


emp1 = Employee("Richard")
print(emp1)

print("-" * 60)

print(emp1.__dict__)

emp1._Employee__name = "Kennedy"   # new property - Expando
print(emp1._Employee__name)

print("-" * 60)
print(emp1)

print("-" * 60)
print(emp1.__dict__)



