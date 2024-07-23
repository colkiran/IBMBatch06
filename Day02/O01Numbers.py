"""
int
float
complex
"""

a = 10
b = -10
print(f"a :{a}")    # f - format string or f string - interpolation
print(type(a))      # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.2
d = -10.5
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 10 + 3j
h = 10 - 3j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(89, 32, 45, 60, 27, 56))
print(min(89, 32, 45, 60, 27, 56))

print("-" * 60)
x = 2 + 3.5
print(type(x))

x = 2
y = 3.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11 :{11}")          # decimal number (Base 10)
print(f"0b11 :{0b11}")      # binary (Base 2)
print(f"0b101 :{0b101}")    # binary
print(f"0o11 :{0o11}")      # octal (Base 8)
print(f"0o111 :{0o111}")    # octal
print(f"0o15 :{0o15}")      # octal
print(f"0xe :{0xe}")        # hexa
print(f"0xa :{0xa}")        # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
print(f"bin(a) :{bin(a)}")
