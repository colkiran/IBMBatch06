
def greet():
    print("Greeting Mr.Sachin, Welcome to the event......")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city = default variable
# gname = non default variable
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mrffa.{gname} from {city}, Welcome to the event......")


greet()
print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admsn(fname, lname, dob, gender, cno, addr, city, qlf):
    print(f"Name :{fname + ' ' + lname}")
    print(f"DOB           :{dob}")
    print(f"Gender        :{gender}")
    print(f"Contact no.   :{cno}")
    print(f"Address       :{addr}")
    print(f"City          :{city}")
    print(f"Qualification :{qlf}")

admsn(cno="4534534", city="Hyderabad", gender="Male", qlf="M Tech", addr="8th cross, 12th main, Ameerpet", dob="19/03/1987", fname="David", lname="Slater")

print("-" * 60)
# variable length arguments - *args, **kwargs

def ProductAll(*numbers):  # *args - can store more than one value in it
    print(numbers)          # tuple
    print(*numbers)         # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = ProductAll(1, 2, 3, 4, 5)
print(f"res :{res}")

"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = [l1, l2]   => [[1, 2, 3], [4, 5, 6]]
l4 = [*l1, *l2] => [1, 2, 3, 4, 5, 6]

"""
print("-" * 60)
# **kwargs - will accept data into a dictionary
def extractDetail(**details):
    print(details)
    print()
    for k, v in details.items():
        print(k, "=>", v)

extractDetail(name='virat', age=34, runs=85, oppn='Aus', venue="Gabba")

print("-" * 60)

def multiplyME(x, y):
    return x * y

a = 10
b = 15

print(f"The product of {a} and {b} is {multiplyME(a, b)}")

# 1 factorial of a number, 2. fibanocci series

print("-" * 60)

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    "this is a doc string"
    # this is a comment
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    1. if x and y are integers then we get the sum of the numbers
    2. if x and y are strings then it results in concatenation of the
        strings
    3. if x is integer and y is a string (vice versa) then the function     will throw an error for mismatch of data types
    """
    return x + y

help(fun1)
