
import csv
from prettytable import PrettyTable

with open('Employee.csv', "r") as csvFile:
    emp_details = csv.reader(csvFile)
    prtyTbl = PrettyTable(next(emp_details))

    for row in emp_details:
        prtyTbl.add_row(row)

print(prtyTbl)



"""
    colnames = next(emp_details)
    print(*colnames)

    for row in emp_details:
        print(*row)

"""