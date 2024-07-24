"""
replace h - x
replace e - y
"""
# maketrans and translate
print("maketrans".center(60, "-"))

st = "hello world"
print(f"st :{st}")

a = "helowrd"       # find
b = "HELOWRD"       # replace

# length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("formatting".center(60, "-"))
a = 10
b = 20

# f string or format string
print(f"The value of a is {a} and value of b is {b}")
print(f"The sum of {a} and {b} is {a + b}")
print("-" * 60)

# C style
print("The value of a is %i and b is %i" % (10, 20))
print("The name of the guest is %s" % ("Lionel Messi"))
print("-" * 60)

# python Style
print("The value of a is {} and b is {}".format(10, 20))
print("The name of the player is {}".format("Lionel Messi"))

print("-" * 60)
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))
print("{num} {num} {num}".format(num = 39))
print("{num} {num:f} {num:b}".format(num = 39))

print("{num:10} {num:f} {num:b}".format(num = 39))
print("{num:5} {num:f} {num:b}".format(num = 39))
print("{num:5} {num:f} {num:b}".format(num = 3945345345))

print("{num:15} Sachin".format(num = 3))
print("{num:15} Sachin".format(num = "Ramesh"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))
print("{pi:010.2}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))


print("-" * 60)
print("{num:>15} Sachin".format(num = "Ramesh"))   # right align
print("{num:^15} Sachin".format(num = "Ramesh"))   # center align
print("{num:<15} Sachin".format(num = "Ramesh"))   # left align

print("-" * 60)
print("python".center(60, "-"))
print("{num:-^60}".format(num="python"))
