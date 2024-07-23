
print("Arithmetic Operators".center(60, "-"))
print(f"Add : 10 + 3 = {10 + 3}")
print(f"Sub : 10 - 3 = {10 - 3}")
print(f"Mul : 10 * 3 = {10 * 3}")
print(f"Div : 10 / 3 = {10 / 3}")
print(f"FlrDiv : 10 // 3 = {10 // 3}")
print(f"Mod : 10 % 3 = {10 % 3}")
print(f"Pow : 10 ** 3 = {10 ** 3}")

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5      # x = x + 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operators".center(60,"-"))
# ==, >, >=, <, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"2 == 1 :{2 == 1}")
print(f"2 > 1 : {2 > 1}")
print(f"1 != 2 :{2 != 1}")

print("Logical Operators".center(60, "-"))
# and, or, not
print(f"1 == 1 and  2 == 2 :{1 == 1 and 2 == 2}")
print(f"2 == 1 and  2 == 2 :{2 == 1 and 2 == 2}")

print("-" * 60)
# or
print(f"1 == 1 or 2 == 1: {1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 1: {1 == 2 or 2 == 1}")

print("-" * 60)
# not
print(f"not(1 == 1 or 2 == 1): {not(1 == 1 or 2 == 1)}")
print(f"not(1 == 2 or 2 == 1): {not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")  # integer representation of unicode char
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1  :{5 << 1}")
print(f"8 << 1  :{8 << 1}")
print(f"5 << 2  :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60, "-"))
a = 18
print("Eligeble" if a >= 18 else "Not Eligeble")
