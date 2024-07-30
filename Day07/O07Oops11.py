
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'Dotnet', 'SharePoint', 'Angular', 'React']


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("David", 25000)
print(emp1)

print("-" * 60)

print(len(emp1))

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)

emp1.append("Python")
print([emp for emp in emp1])

print("-" * 60)

x = emp1[2]
print(f"x :{x}")

print("-" * 60)

emp1[3] = "Sql Server"
print([emp for emp in emp1])
