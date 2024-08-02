
n = int(input("Enter the number :"))
d = int(input("Enter the divisor :"))

try:

    res = n / d

except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)
except Exception as e:
    print("Exception :" + str(e))

else:
    print(f"The quotient is :{res}")

finally:
    print("Completed the task of division.....")