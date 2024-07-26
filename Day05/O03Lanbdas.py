
def add(x, y):
    return x + y

res = add(18, 34)
print(f"res :{res}")

a = add

res = a(45, 68)
print(f"res :{res}")

print("-" * 60)

b = lambda x, y: x + y

res = b(89, 34)
print(f"res :{res}")

print("-" * 60)
"""
lambdas are best used along with
1. map
2. filter
3. reduce (functools)
"""

print("map".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = list(map(lambda x : x ** 2, l1))
print(f"res :{res}")

print("-" * 60)
# expenses in rupees convert it into USD - write map and lambda function
expenses = [10000, 85000, 190000, 350000, 475000, 690000, 860000]
print(f"expenses  :{expenses}")

res = list(map(lambda x : round(x / 83.73, 2) , expenses))
print(f"res  :{res}")

print("-" * 60)
months = ['nov', 'aug', 'sep', 'jul', 'dec', 'jan', 'oct', 'mar', 'may', 'jun', 'apr', 'feb']
print(f"Months :{months}")

# sort these months
from calendar import month_abbr
# print(f"month_abbr :{list(month_abbr)}")
print("-" * 60)

sorted_months = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)
print(f"Sorted Months:{sorted_months}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

res = list(map(lambda x : x.upper(), sentence.split()))
# print(f"res :{res}")
st = " ".join(res)
print(st)

print("filter".center(60, "-"))
l1 = list(range(1, 26))
print(f"l1 :{l1}")

mul_of_3 = list(filter(lambda x : x % 3 == 0, l1))
print(f"Multiples of '3' :{mul_of_3}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("reduce".center(60, "-"))
from functools import reduce
l1 = [9, 7, 2, 8, 10, 1, 5, 3, 6, 4]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

