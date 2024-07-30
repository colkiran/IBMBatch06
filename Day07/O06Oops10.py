
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary
    def __sub__(self, other):
        return self.salary - other.salary
    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary
    def __floordiv__(self, other):
        return self.salary // other.salary


emp1 = Employee("Mike", 3000)
emp2 = Employee("Peter", 4000)
emp3 = Employee("John", 5000)
emp4 = Employee("Kevin", 6000)


print(emp3 + emp1)
print(emp4 - emp1)
print(emp3 * emp2)
print(emp3 / emp1)
print(emp4 // emp1)