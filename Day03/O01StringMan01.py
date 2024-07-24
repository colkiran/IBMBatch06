
print("find".center(60, "-"))
st = "hello world"
print(f"st :{st}")

indx = st.find("w")
print(f"index :{indx}")

indx = st.find("l")
print(f"index '3' :{indx}")

indx = st.find("l", st.find("l")+1)
print(f"index '3' :{indx}")

indx = st.find("l", st.find('l', st.find("l")+1)+1)
print(f"index '3' :{indx}")

st1 = "the quick brown fox jumps over the lazy dog"
print(st1)
res = st1.find('brown')
print(f"res :{res}")

print("replace".center(60, "-"))
st = "hello world"
res= st.replace("w", "W")
print(f"res :{res}")

res = st.replace("l",  "L")
print(f"res :{res}")

res = st.replace("l",  "L", 1)
print(f"res :{res}")

res = st[0:6] + st[6:11].replace("l", "L")
print(f"res :{res}")

print("count".center(60, "-"))
st = "hello world"
res = st.count("l")
print(f"count of 'l' :{res}")

st1 = "the quick brown fox jumps over the lazy dog"
print(f"st1 :{st1}")

res = st1.count("o")
print(f"count of 'o' :{res}")

res = st1.count("e")
print(f"count of 'e' :{res}")

print("index".center(60, "-"))
st = "hello world"
print(f"st :{st}")

res = st.index("l")
print(f"res: {res}")

# res = st.index("a")
# print(f"res :{res}")

res = st.find("a")
print(f"res :{res}")

print("-" * 60)
st = "hello"

# uppercase
print(st.upper())

# sentence case
print(st.capitalize())

st = "****hello****"

# left side
print(st.lstrip("*"))

# right side
print(st.rstrip("*"))

# both side
print(st.strip("*"))

st = "hello"
print(st.isalpha())
print(st.isnumeric())
print(st.islower())