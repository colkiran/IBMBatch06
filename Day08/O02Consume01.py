
import mymodule as m
from mymodule import greet, Employee

print(f"Guest Name :{m.gname}")

print(f"Sports :{m.sports}")

print("-" * 60)

# m.greet("Jack")

greet("Jack")

emp1 = Employee("Joseph", 25000)
print(emp1)