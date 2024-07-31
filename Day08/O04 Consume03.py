
import sys

# print(sys.path)     # pulls all path from then environment path

sys.path.append("C:\\Delhi")

for path in sys.path:
    print(path)

print("-" * 60)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

m.greet("Sachin Tendulkar")

emp1 = Employee("Jack", 50000)
print(emp1)
